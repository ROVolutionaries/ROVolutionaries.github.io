import json
import requests
import os

json_file_path = "Ophiuroidea.json"
images_directory = "images/"

os.makedirs(images_directory, exist_ok=True)

with open(json_file_path, "r") as file:
    data = json.load(file)

for file in data:
    filename = file["uuid"]
    url = file["url"]
    image_path = os.path.join(images_directory, filename + ".png")

    if not os.path.exists(image_path):
        response = requests.get(url)

        if response.status_code == 200:
            with open(image_path, "wb") as img_file:
                img_file.write(response.content)
            print(f"Image {filename} downloaded successfully.")
        else:
            print(f"Failed to retrieve the image {filename}.")
    else:
        print(f"Image {filename} already exists. Skipping download.")
