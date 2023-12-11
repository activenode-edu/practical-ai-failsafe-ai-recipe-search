import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()


def get_supabase_client():
    url: str = os.getenv("SUPABASE_URL")
    key: str = os.getenv("SUPABASE_KEY")

    supabase: Client = create_client(url, key)
    return supabase


db = get_supabase_client()
# all_recipes = db.table('recipes').select('*').execute()
