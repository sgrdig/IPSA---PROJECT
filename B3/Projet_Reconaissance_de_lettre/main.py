import pickle
import numpy as np
from PIL import Image
from sklearn.linear_model import LinearRegression
import os
import csv

def transform_coefficients(a):
    if a == 0:
        return 0, 1
    a_prime = (2 * a) / (1 + a**2)
    b_prime = (1 - a**2) / (1 + a**2)
    return a_prime, b_prime

def process_and_save_image_to_csv(csv_path, image_path, square_size=64):

    with Image.open(image_path) as image:
        width, height = image.size
        row_data = [image_path] 

        for j in range(0, height, square_size):
            for i in range(0, width, square_size):
                box = (i, j, i + square_size, j + square_size)
                square = image.crop(box)

                square_array = np.array(square.convert("L"))
                mask = square_array < 128  
                y_coords, x_coords = np.where(mask)

                if len(x_coords) > 10:
                    x_data = x_coords.reshape(-1, 1)
                    model = LinearRegression().fit(x_data, y_coords)
                    slope, intercept = model.coef_[0], model.intercept_
                    slope_transformed, intercept_transformed = transform_coefficients(slope)
                else:
                    slope_transformed, intercept_transformed = 0, 1 

                row_data.append(f"{i},{j},{slope_transformed},{intercept_transformed}")


        write_header = not os.path.exists(csv_path)
        with open(csv_path, mode='a', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            if write_header:
                writer.writerow(["image_name", "cubes_info"])
            writer.writerow(row_data)

        print(f"Les données de l'image {image_path} ont été enregistrées dans {csv_path}.")



def load_model(pkl_path):
    with open(pkl_path, 'rb') as file:
        model_load = pickle.load(file)
        model = model_load["model"]
    return model

def load_csv_and_predict(csv_path, model, square_size=64):

    coefficients = []

    with open(csv_path, mode='r') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader) 

        for row in reader:
            cubes_info = row[1:]  
            for cube_data in cubes_info:
                i, j, slope_transformed, intercept_transformed = map(float, cube_data.split(","))
                coefficients.extend([i, j, slope_transformed, intercept_transformed])

    # il faut retirer ça 
    expected_features = model.n_features_in_
    if len(coefficients) > expected_features:
        coefficients = coefficients[:expected_features]
    elif len(coefficients) < expected_features:
        coefficients.extend([0] * (expected_features - len(coefficients)))


    coefficients_array = np.array(coefficients).reshape(1, -1)
    return coefficients_array


def predict_letter(image_path, model, csv_path, square_size=64):
    process_and_save_image_to_csv(csv_path, image_path, square_size)
    coefficients_array = load_csv_and_predict(csv_path, model, square_size)
    prediction = model.predict(coefficients_array)
    return prediction[0]



def start():
    
    model_path = "best_mlp_model.pkl"
    image_path = "image/image.png"
    csv_path = "output_data.csv"
    
    loaded_model = load_model(model_path)
    predicted_letter = predict_letter(image_path, loaded_model, csv_path)
    
    return predicted_letter
