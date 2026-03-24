# rag/retriever.py

from sqlalchemy import text
from db.connection import engine
from rag.embeddings import get_embeddings


def retriever(pergunta):
    embeddings = get_embeddings()

    emb = embeddings.embed_query(pergunta)
    emb_str = "[" + ",".join(map(str, emb)) + "]"

    query = text("""
        SELECT conteudo
        FROM documentos
        ORDER BY embedding <-> CAST(:emb AS vector)
        LIMIT 5
    """)

    with engine.connect() as conn:
        result = conn.execute(query, {"emb": emb_str})
        return [row[0] for row in result]