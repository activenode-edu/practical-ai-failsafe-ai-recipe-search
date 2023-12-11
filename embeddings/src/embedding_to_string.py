from numpy import ndarray


def stringify_embedding_for_postgres(embedding: ndarray[float]):
    print(len(embedding[0]))
    return '['+(','.join(str(e) for e in embedding[0].tolist()))+']'
