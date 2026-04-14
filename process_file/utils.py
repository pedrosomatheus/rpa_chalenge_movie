import os
import zipfile
import shutil
from pathlib import Path

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager

load_dotenv()

HEADLESS = os.getenv("HEADLESS", "False") == "True"
DOWNLOAD_DIR = Path.cwd() / "downloads"
OUTPUT_DIR = Path.cwd() / "output"
ZIP_NAME = OUTPUT_DIR / "invoices_2_4.zip"
EDGE_DRIVER_PATH = os.getenv("EDGE_DRIVER_PATH")

def ensure_directories() -> None:
    """Cria os diretórios necessários."""
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def clean_directory(directory: Path) -> None:
    """Limpa arquivos e subpastas de um diretório."""
    if not directory.exists():
        return

    for item in directory.iterdir():
        if item.is_file():
            item.unlink(missing_ok=True)
        elif item.is_dir():
            shutil.rmtree(item, ignore_errors=True)


def setup_driver():
    """Configura o Microsoft Edge para automação."""
    if not EDGE_DRIVER_PATH:
        raise RuntimeError("Defina EDGE_DRIVER_PATH no arquivo .env")

    if not os.path.isfile(EDGE_DRIVER_PATH):
        raise RuntimeError(f"msedgedriver.exe não encontrado em: {EDGE_DRIVER_PATH}")

    options = Options()

    if HEADLESS:
        options.add_argument("--headless=new")

    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(executable_path=EDGE_DRIVER_PATH)
    return webdriver.Edge(service=service, options=options)


def create_zip_from_files(files: list[Path], zip_path: Path) -> None:
    """Compacta os arquivos em um único ZIP."""
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in files:
            zipf.write(file, arcname=file.name)

    print(f"ZIP criado com sucesso em: {zip_path}")