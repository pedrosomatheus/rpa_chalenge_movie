# 🎬 RPA Challenge - Movie Search Automation

Automação desenvolvida para o desafio do RPA Challenge (Movie Search), com foco em robustez, boas práticas e organização de código.

---

## 🚀 Objetivo

Automatizar o fluxo completo de:

1. Acessar o site do desafio
2. Navegar até a aba **Movie Search**
3. Buscar filmes relacionados a "Avengers"
4. Persistir os dados em banco de dados (nome e descrição)
5. Navegar até a aba **Invoice Extraction**
6. Realizar o download dos arquivos 2 e 4
7. Gerar um arquivo ZIP contendo os documentos

---

## 🧠 Abordagem

A solução foi construída com foco em **qualidade de código, escalabilidade e robustez**, indo além da simples automação via Selenium.

Principais decisões:

- Uso de **API (TMDB)** para obter dados de filmes (mais eficiente e confiável que scraping)
- Separação do projeto em módulos (arquitetura organizada)
- Uso de variáveis de ambiente (`.env`)
- Download de arquivos via `requests` (mais confiável que interação via navegador)
- Persistência em banco de dados (MySQL)
- Controle de duplicidade via `tmdb_id`

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
├── sql/
│   ├── dump_movies.sql
│   ├── create_database.sql
│   ├── create_table_movies.sql
│
├── output/
│   └── invoices_2_4.zip
│
├── bot.py
├── .env.example
├── requirements.txt
├── README.md
└── .gitignore
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

Crie um arquivo `.env` baseado no `.env.example`:

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

O sistema:

- Cria automaticamente o banco
- Cria a tabela `movies`
- Insere os dados dos filmes
- Evita duplicidade utilizando `tmdb_id`

---

## 🌐 Automação Web

A automação utiliza Selenium para:

- Acessar o site do desafio
- Navegar entre as abas
- Identificar elementos dinamicamente

---

## 📥 Download das Invoices

Os downloads são realizados via requisições HTTP (`requests`), evitando dependência do comportamento do navegador.

### ✔️ Vantagens:
- Maior estabilidade
- Independente de pop-ups ou novas abas
- Melhor performance

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
- Uso de API externa
- Download robusto via HTTP
- Persistência em banco
- Controle de duplicidade
- Separação de configuração (`.env`)

---

## 👨‍💻 Autor

Projeto desenvolvido para estudo e avaliação técnica.
