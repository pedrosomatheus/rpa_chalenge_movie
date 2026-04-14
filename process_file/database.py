import os
import mysql.connector
from typing import Any
from dotenv import load_dotenv
# ============================================================
# BANCO DE DADOS
# ============================================================
load_dotenv()

MYSQL_CONFIG = {
    "host": os.getenv("MYSQL_HOST"),
    "port": int(os.getenv("MYSQL_PORT")),
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "database": os.getenv("MYSQL_DATABASE"),
}


def create_database_if_not_exists() -> None:
    """Cria o banco caso ele não exista."""
    conn = None
    try:
        conn = mysql.connector.connect(
            host=MYSQL_CONFIG["host"],
            port=MYSQL_CONFIG["port"],
            user=MYSQL_CONFIG["user"],
            password=MYSQL_CONFIG["password"],
        )
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {MYSQL_CONFIG['database']}")
        conn.commit()
        cursor.close()
    finally:
        if conn and conn.is_connected():
            conn.close()


def get_db_connection():
    """Abre conexão com o banco."""
    return mysql.connector.connect(**MYSQL_CONFIG)


def create_movies_table() -> None:
    """Cria a tabela de filmes."""
    query = """
    CREATE TABLE IF NOT EXISTS movies (
        id INT AUTO_INCREMENT PRIMARY KEY,
        movie_name VARCHAR(255) NOT NULL,
        description TEXT,
        release_date DATE NULL,
        tmdb_id INT NULL UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        cursor.close()
    finally:
        if conn and conn.is_connected():
            conn.close()


def insert_movies(movies: list[dict[str, Any]]) -> None:
    if not movies:
        print("Nenhum filme encontrado para inserir.")
        return

    query = """
    INSERT INTO movies (movie_name, description, release_date, tmdb_id)
    VALUES (%s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        movie_name = VALUES(movie_name),
        description = VALUES(description),
        release_date = VALUES(release_date);
    """

    values = [
        (
            movie.get("title"),
            movie.get("overview"),
            movie.get("release_date") or None,
            movie.get("id"),
        )
        for movie in movies
    ]

    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.executemany(query, values)
        conn.commit()
        print(f"{cursor.rowcount} registro(s) processado(s) com sucesso.")
        cursor.close()
    finally:
        if conn and conn.is_connected():
            conn.close()
