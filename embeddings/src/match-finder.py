from database import get_supabase_client
from instructor_embeddings import encode_recipe_to_embedding

# input = 'Salty, savory main dish with a lot of vegetables.'
# input = 'A sweet dessert with a lot of chocolate.'
# input = 'Vegan main dish, savory.'

input = 'Potatoes'

embedding = encode_recipe_to_embedding(input)

db = get_supabase_client()
res = db.rpc('match_recipes', {'query_embedding': embedding,
             'match_threshold': 0.82, 'match_count': 2}).execute()

tableData = res.data
for row in tableData:
    print(row.get('title'))
    print('---------------------')
