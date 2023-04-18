# Flask image grabber

Flask image grabberis a modern and lightweight Flask application that leverages the ipapi API to retrieve geolocation information based on the user's IP address. It also serves an image file specified in the URL.

## Prerequisites

Before running Flask image grabber, make sure you have the following prerequisites:

- Python 3.x installed
- Flask library installed (`pip install flask`)
- Requests library installed (`pip install requests`)

## Setup

To set up Flask image grabber, follow these steps:

1. Sign up for a free API key from [ipapi.com](https://ipapi.com/) if you don't have one already.
2. Replace the `API_KEY` variable in the code with your actual API key.
3. Make sure the image file (`image.png`) you want to serve is in the same directory as the Flask application file.
4. Provide appropriate permissions to the `info.txt` file so that the Flask application can write to it.

## Usage

To use Flask image grabber, follow these steps:

1. Start the Flask application by running the following command:
    ```
    python app.py
    ```

2. Access the Flask application in your web browser or via curl/wget commands with the following URL pattern:
    ```
    http://localhost:5000/<image_name>
    ```

    Replace `<image_name>` with the name of the image file you want to serve. For example:
    ```
    http://localhost:5000/image.png
    ```

3. The Flask application will retrieve the geolocation information for the user's IP address using the ipapi API and save it to the `info.txt` file.
4. The Flask application will then serve the image file to the user.

Note: If you access the Flask application locally using `127.0.0.1` as the IP address, it will display a message indicating that it's for testing purposes only. To get accurate geolocation information, upload the Flask application to a hosting environment.

## License

Flask image grabberis open source and available under the [MIT License](LICENSE).
