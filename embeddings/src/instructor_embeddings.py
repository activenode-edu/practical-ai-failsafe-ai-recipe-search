from InstructorEmbedding import INSTRUCTOR
from embedding_to_string import stringify_embedding_for_postgres

instructor_model = INSTRUCTOR('hkunlp/instructor-base')
instruction = "Summarize the type of recipe / dish as an overarching topic:"


def encode_recipe_to_embedding(inp: str):
    trimmed_string = inp.strip()
    embeddings = instructor_model.encode([[instruction, trimmed_string]])

    stringified_embeddings = stringify_embedding_for_postgres(embeddings)
    return stringified_embeddings
