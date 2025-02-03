
import csv
import numpy as np
from PIL import Image
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def transform_coefficients(a):
    if a == 0:
        return 0, 1
    a_prime = (2 * a) / (1 + a**2)
    b_prime = (1 - a**2) / (1 + a**2)
    return a_prime, b_prime

def split_and_process_image(image, save_dir, csv_filename, image_name, extra_variable, square_size=64):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    row_data = [image_name]
    width, height = image.size
    regression_results = []

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

                x_start, x_end = 0, square_size
                y_start, y_end = slope_transformed * x_start + intercept_transformed, slope_transformed * x_end + intercept_transformed
                x_start_global, y_start_global = x_start + i, y_start + j
                x_end_global, y_end_global = x_end + i, y_end + j

                regression_results.append((x_start_global, y_start_global, x_end_global, y_end_global))
            else:
                slope_transformed, intercept_transformed = 0, 1

            row_data.append(f"{i},{j},{slope_transformed},{intercept_transformed}")

    write_header = not os.path.exists(csv_filename)
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        if write_header:
            writer.writerow(["image_name", "cubes_info"])
        writer.writerow(row_data)

def load_db(path):
    for lettres in os.listdir(path):
        letter_path = os.path.join(path, lettres)
        for lettre in os.listdir(letter_path):
            file_path = os.path.join(letter_path, lettre)
            with Image.open(file_path) as img:
                split_and_process_image(img, "squares", "cubes_info.csv", lettres, "sample_variable")

load_db(path='data')