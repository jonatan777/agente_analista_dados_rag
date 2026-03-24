from rag.retriever import retriever
from rag.reranker import rerank
from rag.llm import get_llm
from rag.memory import salvar_mensagem, resumir_historico


def run_rag(pergunta, session_id):
    # 🔹 recuperar histórico do banco
    history = resumir_historico(session_id)

    # 🔹 RAG
    docs = retriever(pergunta)
    docs = rerank(pergunta, docs)

    contexto = "\n".join(docs)
    historico = "\n".join(history)

    llm = get_llm()

    prompt = f"""
	Você é um assistente especialista.

	Use o contexto abaixo e o histórico da conversa.

	Histórico:
	{historico}

	Contexto:
	{contexto}

	Pergunta:
	{pergunta}

	Se não souber, diga claramente.
	"""

    resposta = llm.invoke(prompt).content

    # 🔥 salvar no banco
    salvar_mensagem(session_id, "user", pergunta)
    salvar_mensagem(session_id, "ai", resposta)

    return {
        "contexto": docs,
        "resposta": resposta
    }



def run_rag_pergunta(pergunta):
    # 🔹 RAG
    docs = retriever(pergunta)
    docs = rerank(pergunta, docs)

    contexto = "\n".join(docs)

    llm = get_llm()

    prompt = f"""
		Você é um assistente especialista.

		Use o contexto abaixo e o histórico da conversa.

		Contexto:
		{contexto}

		Pergunta:
		{pergunta}

		Se não souber, diga claramente.
		"""

    resposta = llm.invoke(prompt).content

    # 🔥 salvar no banco
   # salvar_mensagem(session_id, "user", pergunta)
   # salvar_mensagem(session_id, "ai", resposta)

    return {
        "contexto": docs,
        "resposta": resposta
    }