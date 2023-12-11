import os
from dotenv import load_dotenv
from supabase import create_client, Client
from instructor_embeddings import encode_recipe_to_embedding

load_dotenv()


def get_supabase_client():
    url: str = os.getenv("SUPABASE_URL")
    key: str = os.getenv("SUPABASE_KEY")

    supabase: Client = create_client(url, key)
    return supabase
