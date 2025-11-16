from os import environ
from FlaskWebProject import app

# Required for Azure App Service to detect the Flask app
application = app

# Optional: Run locally with HTTPS if executed directly
if __name__ == "__main__":
    HOST = environ.get("SERVER_HOST", "localhost")
    try:
        PORT = int(environ.get("SERVER_PORT", "5555"))
    except ValueError:
        PORT = 5555
    application.run(HOST, PORT, ssl_context="adhoc")