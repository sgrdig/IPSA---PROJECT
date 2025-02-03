import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import sqlite3
from utils.recommendation import recommend_items , recommend_based_on_item
from utils.rate import rate_product

app = FastAPI()

user_id_ = []

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return RedirectResponse(url="/login")

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(user_id: int = Form(...)):
    print(f"ID Utilisateur soumis : {user_id}")
    user_id_.append(user_id)
    return RedirectResponse(url="/index", status_code=303)



@app.get("/index", response_class=HTMLResponse)
async def profile(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/submit_number", response_class=HTMLResponse)
async def submit_number_page(request: Request):
    return templates.TemplateResponse("item_input.html", {"request": request})




@app.get("/recommend_item", response_class=HTMLResponse)
async def get_recommendations(request: Request):
    # Ici, l'utilisateur est récupéré d'une autre manière, par exemple via une session
    user_id = user_id_[-1]  # Exemple d'ID d'utilisateur
    conn = sqlite3.connect('amazon.db')  # Connexion à la base de données
    recommendations = recommend_based_on_item(user_id=user_id, conn=conn)  # Appel de la fonction de recommandation
    
    recommendations = [{"product_id": item[0], "product_name": f"Produit {item[0]}", "rating": item[1]} for item in recommendations]
    
    return templates.TemplateResponse("recommendations.html", {"request": request, "recommendations": recommendations, "user_id": user_id})



@app.get("/profile", response_class=HTMLResponse)
async def profile(request: Request):
    user_id = user_id_[-1]
    conn = sqlite3.connect('amazon.db')
    r_i = recommend_items(user_id, conn)
    r_i = [{"product_id": item[0], "product_name": f"Produit {item[0]}", "rating": item[1]} for item in r_i]

    print(r_i)
    return templates.TemplateResponse("profile.html", {"request": request, "user_id": user_id, "recommended_items": r_i})


@app.get("/product/{product_id}", response_class=HTMLResponse)
async def product(request: Request, product_id: int):
    return templates.TemplateResponse("product.html", {"request": request, "product_id": product_id})

@app.get("/evaluation", response_class=HTMLResponse)
async def evaluation(request: Request):
    return templates.TemplateResponse("evaluation.html", {"request": request})

@app.get("/search", response_class=HTMLResponse)
async def search(request: Request , item_num: int = Form(...)):
    return templates.TemplateResponse("search.html", {"request": request})

@app.post("/get_note", response_class=HTMLResponse)
async def search(request: Request, item_num: int = Form(...)):
    with sqlite3.connect('amazon.db') as conn:
        print("Connexion ouverte")

        cursor = conn.cursor()
        cursor.execute('SELECT item_id, rating FROM amazon_table WHERE item_id = ?', (item_num,))
        results = cursor.fetchall()  # Fetch the results as a list of tuples
        
        # Add the index to the results
        indexed_results = [{"index": idx + 1, "item_id": result[0], "rating": result[1]} for idx, result in enumerate(results)]
        
        # Print the indexed results for debugging purposes
        print(indexed_results)
        
    # Pass the indexed results to the template
    return templates.TemplateResponse("get_note.html", {"request": request, "existing_notes": indexed_results})


@app.post("/submit-review")
async def submit_review(
    request: Request,
    product_id: int = Form(...),
    rate: int = Form(...),
):
    user_id = user_id_[-1]  # Utilisation de user_id_ comme tu l'as définie ailleurs
    print(f"Produit ID: {product_id}, Note: {rate}, User ID: {user_id}")
    try:
        with sqlite3.connect('amazon.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT item_id, user_id FROM amazon_table WHERE user_id = ? AND item_id = ?",
                (user_id, product_id),
            )
            existing_review = cursor.fetchall()
            if existing_review:
                message = "Vous avez déjà évalué ce produit."
                rate_product(user_id=user_id, conn=conn, product_id=product_id, rate=rate, cursor=cursor, update=True)
            else:
                rate_product(user_id=user_id, conn=conn, product_id=product_id, rate=rate, cursor=cursor, update=False)
                message = "Évaluation soumise avec succès"
    except Exception as e:
        print(f"Erreur lors de l'accès à la base de données: {e}")
        message = "Une erreur s'est produite lors de la soumission de l'évaluation."
    
    return templates.TemplateResponse(
        "evaluation.html",
        {"request": request, "message": message},
    )




# async def submit_review(
#     request: Request,
#     product_id: int = Form(...),
#     rate: int = Form(...),
# ):
#     print(f"Produit ID: {product_id}, Note: {rate}")
#     with sqlite3.connect('amazon.db') as conn:

#         print("in")

#         # cursor.execute(f"SELECT rating , user_id FROM amazon_table WHERE user_id = {user_id_[-1]} and item_id = {product_id}")
#         cursor.execute("SELECT rating, user_id FROM amazon_table WHERE user_id = ? AND item_id = ?", 
#                (user_id_[-1], product_id))
#         print("query done")
#         existing_review = cursor.fetchone()
#         print(existing_review)

#         if existing_review:
#             message = "Vous avez déjà évalué ce produit."
#         else:
#             cursor = conn.cursor()
#             rate_product(user_id=user_id_[-1], conn=conn, product_id=product_id, rate=rate)
#             message = "Évaluation soumise avec succès"

    # except Exception as e:
    #     print(f"Erreur lors de l'accès à la base de données: {e}")
    #     message = "Une erreur s'est produite lors de la soumission de l'évaluation."

    # finally:
    #     conn.close()


if __name__ == '__main__':
    uvicorn.run(app, port=8000)
