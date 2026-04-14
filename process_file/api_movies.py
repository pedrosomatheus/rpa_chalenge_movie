import os
import requests
from typing import Any
from dotenv import load_dotenv

# ============================================================
# API / FILMES
# ============================================================
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

def search_movies_tmdb(query: str) -> list[dict[str, Any]]:
    """
    Busca todos os filmes na API do TMDB para o termo informado.
    Traz paginação completa.
    """
    url = "https://api.themoviedb.org/3/search/movie"
    page = 1
    all_results: list[dict[str, Any]] = []

    while True:
        params = {
            "api_key": TMDB_API_KEY,
            "query": query,
            "page": page,
        }

        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()

        data = response.json()

        results = data.get("results", [])
        total_pages = data.get("total_pages", 1)

        all_results.extend(results)

        print(f"Página {page}/{total_pages} processada. Registros acumulados: {len(all_results)}")

        if page >= total_pages:
            break

        page += 1

    return all_results
