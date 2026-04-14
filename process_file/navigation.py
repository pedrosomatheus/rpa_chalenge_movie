import os
import requests
from pathlib import Path
from urllib.parse import urlparse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
DOWNLOAD_DIR = Path.cwd() / "downloads"


def open_site(driver) -> None:
    driver.get(BASE_URL)

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    print("Site aberto com sucesso.")


def click_movie_search_tab(driver) -> None:
    possible_locators = [
        (By.LINK_TEXT, "Movie Search"),
        (By.PARTIAL_LINK_TEXT, "Movie Search"),
        (By.XPATH, "//a[contains(., 'Movie Search')]"),
        (By.XPATH, "//button[contains(., 'Movie Search')]"),
    ]

    for by, locator in possible_locators:
        try:
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((by, locator))
            )
            element.click()
            print("Aba Movie Search acessada.")
            return
        except Exception:
            continue

    raise RuntimeError("Não foi possível localizar a aba Movie Search.")


def click_invoice_extraction_tab(driver) -> None:
    possible_locators = [
        (By.LINK_TEXT, "Invoice Extraction"),
        (By.PARTIAL_LINK_TEXT, "Invoice Extraction"),
        (By.XPATH, "//a[contains(., 'Invoice Extraction')]"),
        (By.XPATH, "//button[contains(., 'Invoice Extraction')]"),
    ]

    for by, locator in possible_locators:
        try:
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((by, locator))
            )
            element.click()
            print("Aba Invoice Extraction acessada.")
            return
        except Exception:
            continue

    raise RuntimeError("Não foi possível localizar a aba Invoice Extraction.")


def download_invoice_by_number(driver, invoice_number: int) -> Path:
    """
    Baixa a invoice pelo href e retorna o caminho salvo.
    """
    xpath = f"//table/tbody/tr[{invoice_number}]/td[4]/a"

    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )

    file_url = element.get_attribute("href")

    if not file_url:
        raise RuntimeError(f"Não foi possível obter o link da invoice {invoice_number}")

    print(f"Baixando invoice {invoice_number}: {file_url}")

    response = requests.get(file_url, timeout=30)
    response.raise_for_status()

    parsed = urlparse(file_url)
    suffix = Path(parsed.path).suffix.lower()

    if suffix not in [".jpg", ".jpeg", ".png", ".webp", ".pdf"]:
        suffix = ".jpg"

    file_path = DOWNLOAD_DIR / f"invoice_{invoice_number}{suffix}"

    with open(file_path, "wb") as f:
        f.write(response.content)

    print(f"Invoice {invoice_number} salva em: {file_path}")
    return file_path