import sqlite3

def rate_product(user_id: int, conn: sqlite3.Connection, product_id: int, rate: float, cursor: sqlite3.Cursor, update: bool):
    try:
        if update:
            cursor.execute(
                "UPDATE amazon_table SET rating = ? WHERE user_id = ? AND item_id = ?",
                (rate, user_id, product_id)
            )
            print(f"Mise à jour de la note pour l'utilisateur {user_id} et le produit {product_id}")
        else:
            cursor.execute(
                "INSERT INTO amazon_table (user_id, item_id, rating) VALUES (?, ?, ?)",
                (user_id, product_id, rate)
            )
            print(f"Insertion de la note pour l'utilisateur {user_id} et le produit {product_id}")

        conn.commit()
        return {"message": "Opération réussie"}
    except Exception as e:
        print("Erreur lors de l'opération sur la base de données:", e)
        return {"error": f"Une erreur s'est produite: {e}"}