import flask
import os
import binascii
import requests
from flask import Flask, render_template, request, redirect, send_file

def generate_secret_key():
    """
    Generates a random secret key for Flask application.
    """
    secret_key = os.urandom(32)
    return binascii.hexlify(secret_key).decode('utf-8')

app = Flask(__name__)
app.secret_key = generate_secret_key()

# ipapi API endpoint
IP_GEOLOCATION_API = 'http://api.ipapi.com/'
API_KEY = "-"  # Replace with your actual API key

# with image
# NOTE: you could remove this part of code if you don't want it.
@app.route("/<string:image_name>")
def site(image_name: str):
    """
    Route for serving image file based on image name provided in URL.

    Args:
        image_name (str): The name of the image file.

    Returns:
        Response: The image file as a response.
    """
    if not image_name.endswith(".png") or not os.path.exists(image_name):
        return "Please enter a valid image."
    # Get user IP address
    # user_ip = request.remote_addr
    user_ip = request.remote_addr
    if user_ip == "127.0.0.1":
        # just says that we are testing
        return "If you are trying to test, upload it to a hosting."
    # Make request to ipapi API
    response = requests.get(f'{IP_GEOLOCATION_API}/{user_ip}?access_key={API_KEY}')

    if response.status_code == 200:
        # Extract country and city information from the response
        geolocation_data = response.json()
        country = geolocation_data.get('country_name')
        city = geolocation_data.get('city')

        # Save the country and city information to a file
        with open("info.txt", 'a') as f:
            f.write(f"New IP visited: {user_ip}\n{user_ip}'s Country: {country}\n{user_ip}'s City: {city}\n\n")

    return send_file(image_name,  mimetype="image/png")

# without user giving the image url
@app.route("/")
def withoutImage():
    """
    Route for serving a default image file when no image name is provided in URL.

    Returns:
        Response: The default image file as a response.
    """
    # Get user IP address
    # user_ip = request.remote_addr
    user_ip = request.remote_addr
    if user_ip == "127.0.0.1":
        # just says that we are testing
        return "If you are trying to test, upload it to a hosting."
    # Make request to ipapi API
    response = requests.get(f'{IP_GEOLOCATION_API}/{user_ip}?access_key={API_KEY}')

    if response.status_code == 200:
        # Extract country and city information from the response
        geolocation_data = response.json()
        country = geolocation_data.get('country_name')
        city = geolocation_data.get('city')

        # Save the country and city information to a file
        with open("info.txt", 'a') as f:
            f.write(f"New IP visited: {user_ip}\n{user_ip}'s Country: {country}\n{user_ip}'s City: {city}\n\n")

    return send_file("image.png",  mimetype="image/png")

# the run, must be EDITED before deploying
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
