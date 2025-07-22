from .llm import call_llm


def retrieve_and_answer(query: str, index, chunks, embedder_model) -> str:
    query_vec = embedder_model.encode([query])
    _, I = index.search(query_vec, k=5)
    context = '\n\n'.join(chunks[i] for i in I[0])
    prompt = f'Context:\n{context}\n\nQuestion:{query}\nAnswer:'

    return call_llm(prompt)
