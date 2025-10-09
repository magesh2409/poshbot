from openai import OpenAI
import requests
import os
import time
from app.commands.service_commands import get_service_cmd


def get_openai_client(api_key):
    client = OpenAI(api_key=api_key)
    return client

def get_listings_data(listing_id):
    response = requests.get("https://api.goshposh.com/listings/" + listing_id)
    return response.json()


def upload_file_to_openai(file_path, api_key):
    client = get_openai_client(api_key)
    file = client.files.create(
        file = open(file_path, "rb"),
        purpose = "user_data"
    )
    if os.path.exists(file_path):
        os.remove(file_path)
    return file.id


def download_cloudfront_image(data):
    response = requests.get(data["s3_url"])
    file_name = str(data["service_id"]) + "_" + str(int(time.time())) + ".jpg"
    with open(file_name, "wb") as file:
        file.write(response.content)
    return file_name

def handle_listing_file(data):
    file_name = download_cloudfront_image(data)
    service = get_service_cmd(data["service_id"])
    file_id = upload_file_to_openai(file_name, service.get("api_key"))
    data["file_id"] = file_id
    return data
