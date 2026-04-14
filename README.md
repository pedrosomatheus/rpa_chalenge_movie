# 🎬 RPA Challenge - Movie Search Automation

Automação desenvolvida para o desafio do RPA Challenge (Movie Search), com foco em robustez, boas práticas e organização de código.

---

## 🚀 Objetivo

Automatizar o fluxo de:

1. Buscar filmes utilizando API
2. Persistir dados em banco de dados
3. Navegar no site do desafio
4. Baixar invoices específicas
5. Gerar um arquivo ZIP com os documentos

---

## 🧠 Abordagem

A solução foi construída com foco em **qualidade de código, escalabilidade e robustez**, indo além da simples automação via Selenium.

Principais decisões:

- Uso de **API (TMDB)** para obter dados de filmes (mais eficiente que scraping)
- Separação do projeto em módulos
- Uso de variáveis de ambiente (`.env`)
- Download de arquivos via `requests` (mais confiável que clique em navegador)
- Persistência em banco de dados (MySQL)

---

## 🏗️ Estrutura do Projeto

```
RPA_ChalengeMovies/
│
├── process_file/
│   ├── api_movies.py
│   ├── database.py
│   ├── navigation.py
│   ├── utils.py
│
├── downloads/
├── output/
│
├── bot.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Tecnologias Utilizadas

- Python 3.x
- Selenium
- Requests
- MySQL
- python-dotenv

---

## 🔐 Configuração do Ambiente

### 1. Criar ambiente virtual

```
python -m venv venv
venv\Scripts\activate
```

---

### 2. Instalar dependências

```
pip install -r requirements.txt
```

---

### 3. Configurar `.env`

```
BASE_URL=https://rpachallenge.com/
TMDB_API_KEY=SUA_API_KEY
MOVIE_QUERY=Avengers

HEADLESS=False

MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_DATABASE=wellbe_challenge

EDGE_DRIVER_PATH=C:\RPA\drivers\msedgedriver.exe
```

---

## 🗄️ Banco de Dados

O sistema cria automaticamente o banco e a tabela `movies`, evitando duplicidade através do `tmdb_id`.

---

## 🌐 Automação Web

A automação utiliza Selenium para navegação e interação com o site do desafio.

---

## 📥 Download das Invoices

Os downloads são realizados via `requests`, garantindo maior confiabilidade.

---

## 📦 Geração do ZIP

Os arquivos são compactados em:

```
output/invoices_2_4.zip
```

---

## ▶️ Execução

```
python bot.py
```

---

## 🧠 Diferenciais

- Arquitetura modular
- Uso de API
- Download robusto
- Persistência em banco
- Uso de .env

---

## 👨‍💻 Autor

Projeto desenvolvido para estudo e avaliação técnica.
