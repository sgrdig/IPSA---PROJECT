import json    

data = [json.loads(line) for line in open('D:\Bin111\extraction\yelp_academic_dataset_business.json', 'r',encoding="utf8")]

def get_adress():
    id = input("Id resto: ")
    for i in range (0, len(data)):
        if id == data[i]['business_id']: 
            print(data[i]['address'],"ligne",[i])
            return data[i]['address']


def get_name():
    id = input("Id resto: ")
    for i in range (0, len(data)):
        if id == data[i]['business_id']: 
            print(data[i]['name'],"ligne",[i])
            return data[i]['name']



def get_id():
    name = input("Nom resto: ")
    for i in range (0, len(data)):
        if name == data[i]['name']: 
            print(data[i]['business_id'],"ligne",[i])
            return data[i]['business_id']


def restaurant_metadata(data, triplet):
    resultats = []
    for i in range (0, len(data)):
        attribut = triplet[0]
        operateur = triplet[1]
        valeur = triplet[2]
        insert =[]
        if attribut == "stars" :
            if operateur == ">":
                if float(data[i][attribut]) > float(valeur):
                    insert.append(data[i]['business_id'])
                    insert.append(data[i]['name'])
                    resultats.append(insert)
            if operateur == "<":
                if float(data[i][attribut]) < float(valeur):
                    insert.append(data[i]['business_id'])
                    insert.append(data[i]['name'])
                    resultats.append(insert)
        elif attribut == "state":
            if data[i][attribut] == valeur:
                insert.append(data[i]['business_id'])
                insert.append(data[i]['name'])
                resultats.append(insert)
    return resultats

triplet = ["stars", "=", "2"]
print(restaurant_metadata(data, triplet))
