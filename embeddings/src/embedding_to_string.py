from numpy import ndarray


def stringify_embedding_for_postgres(embedding: ndarray[float]):
    return '['+(','.join(str(e) for e in embedding[0].tolist()))+']'
