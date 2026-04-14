import os
import time
from pathlib import Path
from mysql.connector import Error
from dotenv import load_dotenv

from process_file.api_movies import search_movies_tmdb
from process_file.database import create_database_if_not_exists, create_movies_table, insert_movies
from process_file.navigation import (
    click_invoice_extraction_tab,
    click_movie_search_tab,
    download_invoice_by_number,
    open_site,
)
from process_file.utils import clean_directory, create_zip_from_files, ensure_directories, setup_driver

load_dotenv()

MOVIE_QUERY = os.getenv("MOVIE_QUERY", "Avengers")
DOWNLOAD_DIR = Path.cwd() / "downloads"
OUTPUT_DIR = Path.cwd() / "output"
ZIP_NAME = OUTPUT_DIR / "invoices_2_4.zip"


def main() -> None:
    driver = None

    try:
        print("Preparando ambiente...")
        ensure_directories()
        clean_directory(DOWNLOAD_DIR)
        clean_directory(OUTPUT_DIR)

        print("Preparando banco de dados...")
        create_database_if_not_exists()
        create_movies_table()

        print("Buscando filmes via API...")
        movies = search_movies_tmdb(MOVIE_QUERY)
        insert_movies(movies)

        print("Iniciando navegação com Selenium...")
        driver = setup_driver()
        open_site(driver)

        print("Acessando Movie Search...")
        click_movie_search_tab(driver)
        time.sleep(2)

        print("Acessando Invoice Extraction...")
        click_invoice_extraction_tab(driver)
        time.sleep(2)

        print("Baixando invoice 2...")
        invoice_2_path = download_invoice_by_number(driver, 2)

        print("Baixando invoice 4...")
        invoice_4_path = download_invoice_by_number(driver, 4)

        files_to_zip = [invoice_2_path, invoice_4_path]

        for file_path in files_to_zip:
            if not file_path.exists():
                raise RuntimeError(f"Arquivo não encontrado para compactação: {file_path}")

        print("Gerando ZIP final...")
        create_zip_from_files(files_to_zip, ZIP_NAME)

        print("\nProcesso concluído com sucesso.")
        print(f"ZIP final: {ZIP_NAME}")

    except Error as db_error:
        print(f"Erro de banco de dados: {db_error}")
        raise
    except Exception as e:
        print(f"Erro na execução: {e}")
        raise
    finally:
        if driver:
            driver.quit()


if __name__ == "__main__":
    main()