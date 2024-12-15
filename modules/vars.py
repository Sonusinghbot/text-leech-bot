import os

API_ID    = os.environ.get("API_ID", "23260899")
API_HASH  = os.environ.get("API_HASH", "f5db562dce15813ec1180fd22e3e30af")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7617539638:AAG0eoy581sxtbxz5t7Z4YLAzLTqzIcClB0") 
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
