from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv('BOT_TOKEN')
PHOTOS = [
    f'photos/photo_{num}.jpg' for num in range(1, 8)
]
min_index = 0
max_index = len(PHOTOS) - 1
