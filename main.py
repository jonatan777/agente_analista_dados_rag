# main.py

from fastapi import FastAPI, UploadFile, File
from rag.ingest import processar_arquivo
from rag.pipeline import run_rag, run_rag_pergunta

app = FastAPI()


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    content = await file.read()

    result = processar_arquivo(
        file_bytes=content,
        filename=file.filename
    )

    return result


@app.post("/perguntar")
async def perguntar_sem_memoria(pergunta: str):
    result = run_rag_pergunta(pergunta)
    return result


# precisa está logado
@app.post("/chat")
async def perguntar_com_memoria(pergunta: str, session_id: str):
    result = run_rag(pergunta, session_id)
    return result