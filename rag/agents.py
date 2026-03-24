# rag/agents.py

from rag.llm import get_llm


def analyst(pergunta, contexto):
    llm = get_llm()  # ✅ evita erro de client fechado

    prompt = f"""
	Você é um assistente especialista em análise de dados.

	Use SOMENTE o contexto abaixo para responder.

	Se não souber, diga claramente que não sabe.

	Contexto:
	{contexto}

	Pergunta:
	{pergunta}

	Resposta detalhada:
	"""

    return llm.invoke(prompt).content