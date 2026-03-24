# rag/ingest.py

import pandas as pd
from PyPDF2 import PdfReader
from sqlalchemy import text
from db.connection import engine
from rag.embeddings import get_embeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


# text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
# texts = text_splitter.split_text(document)



def extrair_texto_pdf(file):
    reader = PdfReader(file)
    texto = ""
    for page in reader.pages:
        texto += page.extract_text() or ""
    return texto


def extrair_texto_csv(file):
    df = pd.read_csv(file)
    return df.to_string()


# def chunk_text(texto, chunk_size=500):
#    return [texto[i:i+chunk_size] for i in range(0, len(texto), chunk_size)]

def chunk_text(texto):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    return splitter.split_text(texto)


def salvar_chunks(chunks, filename):
    embeddings = get_embeddings()  # ✅ CORRETO AGORA

    with engine.begin() as conn:  # 🔥 melhor que connect + commit
        for chunk in chunks:
            emb = embeddings.embed_query(chunk)
            emb_str = "[" + ",".join(map(str, emb)) + "]"

            conn.execute(
                text("""
                    INSERT INTO documentos (conteudo, embedding)
                    VALUES (:c, CAST(:e AS vector))
                """),
                {"c": chunk, "e": emb_str, "fonte": filename}
#               {"c": chunk, "e": emb_str}
                
            )


def processar_arquivo(file_bytes, filename):
    if filename.endswith(".pdf"):
        from io import BytesIO
        texto = extrair_texto_pdf(BytesIO(file_bytes))

    elif filename.endswith(".csv"):
        from io import StringIO
        texto = extrair_texto_csv(StringIO(file_bytes.decode()))

    else:
        texto = file_bytes.decode("utf-8")

    chunks = chunk_text(texto)
    salvar_chunks(chunks, filename)

    return {"status": "ok", "chunks": len(chunks)}