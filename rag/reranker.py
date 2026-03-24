from sentence_transformers import CrossEncoder

reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

def rerank(pergunta, documentos):
    pairs = [(pergunta, doc) for doc in documentos]
    scores = reranker.predict(pairs)

    ranked = sorted(zip(documentos, scores), key=lambda x: x[1], reverse=True)
    return [doc for doc, _ in ranked[:3]]