# 🤖 RAG Multi-Agente com FastAPI + pgvector + Ollama

Sistema de **Recuperação Aumentada por Geração (RAG)** com múltiplos agentes, capaz de:

* 📥 Receber arquivos (PDF, CSV, TXT)
* 🧠 Gerar embeddings automaticamente
* 🗄️ Armazenar no PostgreSQL com pgvector
* 🔎 Recuperar contexto relevante
* 🔥 Reordenar resultados com reranking (CrossEncoder)
* 💬 Responder perguntas com memória (estilo ChatGPT)
* 🌐 Disponibilizar API via FastAPI

---

# 🚀 Arquitetura do Sistema

```
Usuário
  ↓
FastAPI
  ↓
Upload → Ingestão → Embeddings → PostgreSQL (pgvector)
  ↓
Pergunta
  ↓
Retriever (vetorial)
  ↓
Reranker 🔥
  ↓
Memória (histórico)
  ↓
LLM (Ollama)
  ↓
Resposta
```

---

# 🧠 Tecnologias Utilizadas

* Python
* FastAPI
* PostgreSQL + pgvector
* LangChain
* Ollama (LLM local)
* Hugging Face (embeddings)
* Sentence Transformers (reranking)

---

# 📦 Estrutura do Projeto

```
app_rag_API/
│
├── main.py
├── db/
│   └── connection.py
│
├── rag/
│   ├── embeddings.py
│   ├── llm.py
│   ├── ingest.py
│   ├── retriever.py
│   ├── reranker.py
│   ├── agents.py
│   └── pipeline.py
```

---

# ⚙️ Instalação

## 1. Clonar repositório

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

---

## 2. Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

---

## 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 4. Instalar dependências principais manualmente (caso necessário)

```bash
pip install fastapi uvicorn
pip install sqlalchemy psycopg2-binary
pip install langchain langchain-ollama langchain-huggingface
pip install sentence-transformers
pip install PyPDF2 pandas
```

---

# 🗄️ Configuração do Banco (pgvector)

## 1. Criar extensão

```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

---

## 2. Criar tabela

```sql
CREATE TABLE documentos (
    id SERIAL PRIMARY KEY,
    conteudo TEXT,
    embedding VECTOR(384)
);
```

---

# 🤖 Configurar Ollama

## 1. Instalar Ollama

https://ollama.com

---

## 2. Rodar modelo

```bash
ollama run llama3.2:1b
```

---

# 🔐 (Opcional) Hugging Face Token

Evita limites de download:

```bash
export HF_TOKEN=seu_token
```

---

# ▶️ Executar API

```bash
uvicorn main:app --reload
      ou
fastapi dev main.py
```

Acesse:

👉 http://127.0.0.1:8000/docs

---

# 📥 Endpoint: Upload de Arquivo

### POST `/upload`

Upload de arquivos PDF, CSV ou TXT

### Exemplo:

```bash
curl -X POST \
  -F "file=@dados.pdf" \
  http://localhost:8000/upload
```

---

# 💬 Endpoint: Chat com RAG

### POST `/chat`

Parâmetros:

* `pergunta`
* `session_id`

### Exemplo:

```bash
curl -X POST "http://localhost:8000/chat?pergunta=Qual produto vendeu mais?&session_id=user1"
```

---

# 🔥 Funcionalidades Avançadas

## ✅ RAG (Retrieval Augmented Generation)

Busca semântica com embeddings

## 🔥 Reranking (CrossEncoder)

Melhora precisão dos resultados

## 🧠 Memória de Conversa

Histórico por usuário (`session_id`)

## 📄 Suporte a múltiplos arquivos

* PDF
* CSV
* TXT

---

# 🧪 Exemplo de Fluxo

1. Upload de arquivo
2. Texto é quebrado em chunks
3. Embeddings são gerados
4. Dados são salvos no pgvector
5. Usuário faz pergunta
6. Sistema busca contexto relevante
7. Reranker melhora resultados
8. LLM gera resposta final

---

# ⚠️ Problemas Comuns

## Erro de dimensão (768 vs 384)

```sql
VECTOR(384)
```

---

## Ollama não rodando

```bash
ollama run llama3.2:1b
```

---

## HF Token warning

Pode ignorar ou configurar variável de ambiente

---

# 🚀 Melhorias Futuras

* [ ] Memória persistente (PostgreSQL)
* [ ] Streaming de resposta
* [ ] Interface web (React/Flutter)
* [ ] Deploy com Docker
* [ ] Hybrid Search (SQL + vector)
* [ ] RAG multi-documento avançado

---

# 🧠 Inspiração

Arquiteturas modernas de IA baseadas em:

* RAG
* LLMs locais
* Sistemas multi-agente

---

# 📜 Licença

MIT

---

# 👨‍💻 Autor

Projeto desenvolvido para estudo avançado de Engenharia de IA.

---

# ⭐ Contribuição

Pull requests são bem-vindos!

Se esse projeto te ajudou, deixe uma ⭐ no repositório 🚀
