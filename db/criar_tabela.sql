CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE documentos (
    id SERIAL PRIMARY KEY,
    conteudo TEXT,
    embedding VECTOR(384);
);


-- DROP TABLE IF EXISTS public.chat_history;
CREATE TABLE chat_history (
    id SERIAL PRIMARY KEY,
    session_id TEXT,
    role TEXT, -- 'user' ou 'ai'
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



# Adicione contexto:
ALTER TABLE documentos ADD COLUMN fonte TEXT;
ALTER TABLE documentos ADD COLUMN pagina INT;


# indexar para performance
CREATE INDEX idx_session ON chat_history(session_id);

Salvar embeddings da conversa
ALTER TABLE chat_history ADD COLUMN embedding VECTOR(384);
