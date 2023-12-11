from database import get_supabase_client
from instructor_embeddings import encode_recipe_to_embedding


db = get_supabase_client()
all_recipes = db.table('recipes').select('*').execute()

all_recipes = all_recipes.data
for recipe in all_recipes:
    recipe_id = recipe.get('id')
    recipe_content = recipe.get('content')
    recipe_title = recipe.get('title')

    title_then_content = recipe_title + "\n\n" + recipe_content
    embedding = encode_recipe_to_embedding(title_then_content)
    db.table('recipes').update({'embedding': embedding}).eq(
        'id', recipe_id).execute()
    print(recipe_id)
