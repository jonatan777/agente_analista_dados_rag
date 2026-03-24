from sqlalchemy import text
from db.connection import engine
from rag.llm import get_llm


def salvar_mensagem(session_id, role, message):
    with engine.begin() as conn:
        conn.execute(
            text("""
                INSERT INTO chat_history (session_id, role, message)
                VALUES (:s, :r, :m)
            """),
            {"s": session_id, "r": role, "m": message}
        )


def buscar_historico(session_id, limite=10):
    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT role, message
                FROM chat_history
                WHERE session_id = :s
                ORDER BY created_at DESC
                LIMIT :l
            """),
            {"s": session_id, "l": limite}
        )

        rows = result.fetchall()

    # inverter (mais antigo → mais recente)
    rows.reverse()

    return [f"{r[0].upper()}: {r[1]}" for r in rows]
#    return [f"{r[0]}: {r[1]}" for r in rows]


def resumir_historico(session_id):
    history = buscar_historico(session_id, limite=20)

    llm = get_llm()

    prompt = f"Resuma a conversa:\n{history}"
    return llm.invoke(prompt).content