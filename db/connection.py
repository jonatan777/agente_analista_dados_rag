# db/connection.py
from sqlalchemy import create_engine

DB_URL = "postgresql://postgres:jonatan@172.18.0.3:5432/rag_agent_db"

engine = create_engine(DB_URL)
