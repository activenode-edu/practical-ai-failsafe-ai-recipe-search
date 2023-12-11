from InstructorEmbedding import INSTRUCTOR
from embedding_to_string import stringify_embedding_for_postgres

instructor_model = INSTRUCTOR('hkunlp/instructor-base')
instruction = "Summarize the type of recipe / dish as an overarching topic:"

recipeTextMultiline = """
Protein-packed edamame is the star of the show in this Garlicky Sesame Edamame Salad!

Edamame is tossed with sizzled garlic and toasted nuts and seeds before being finished with a savory, tangy tahini-soy sauce dressing and fresh herbs. The recipe is adapted from one of my favorites in my cookbook, Spicy Sesame Edamame, so there’s no shortage of magic in every bite.

This nutty, limey and crunchy edamame salad is the kind of lunch you look forward to all morning long. It’s good for you, too, but you’d never know it. The big and bold flavors pack a punch while the protein and fiber leave you feeling full and satisfied for hours! 
"""


def encode_recipe_to_embedding(inp: str):
    trimmed_string = inp.strip()
    embeddings = instructor_model.encode([[instruction, trimmed_string]])
    stringified_embeddings = stringify_embedding_for_postgres(embeddings)
    return stringified_embeddings


print(encode_recipe_to_embedding(recipeTextMultiline))
