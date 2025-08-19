from urllib.parse import quote_plus

POSTGRES_HOST = "192.168.1.62"
POSTGRES_PORT = 5555
POSTGRES_DB = "intellidb"
POSTGRES_USER = "intellidb"
POSTGRES_PASSWORD = quote_plus("IDBE@2025")
POSTGRES_SSL = False

DATABASE_URL = (
    f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

OPENAI_API_KEY = "24572426-372c-4214-a018-2e32e1f718aa"
OPENAI_API_BASE = "https://api.sambanova.ai/v1"
OPENAI_MODEL_NAME = "Llama-4-Maverick-17B-128E-Instruct"
