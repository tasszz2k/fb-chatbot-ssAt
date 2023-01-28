import os
from dotenv import load_dotenv

load_dotenv()
# OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPEN_AI_MODEL = "text-curie-001"

# Spotify
SPOTIFY_USERNAME = 'dhyxi2nynfg8ix3ddcmmhhl6u'
SPOTIFY_SCOPE = 'user-library-read'
SPOTIFY_CLIENT_ID = 'db2735761229484685c1e719a8940998'
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_PLAYLIST_ID = '3IhDh1G4c4JoqaDUQtxIdv'

# Facebook
FACEBOOK_ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS_TOKEN")
FACEBOOK_VERIFY_TOKEN = os.getenv("FACEBOOK_VERIFY_TOKEN")