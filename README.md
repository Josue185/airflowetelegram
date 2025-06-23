Este projeto demonstra como orquestrar um pipeline simples de dados utilizando Apache Airflow, com execução containerizada via Docker, e recursos adicionais como envio de notificações automáticas via Telegram.

🔧 Tecnologias utilizadas
Apache Airflow 2.9.1 (via Docker)

Python 3.12

Pandas

PyArrow (suporte a arquivos Parquet)

Requests

Dotenv

Telegram Bot API

airflow-projeto/
├── dags/
│   ├── tratar_csv_para_parquet.py       # DAG principal
│   ├── abrindo_parquet.py               # Leitura e tratamento adicional do Parquet
│   ├── dados/                           # CSV de entrada
│   │   └── dados.csv
│   ├── resultados/                      # Arquivos Parquet gerados
│   └── .env                             # Variáveis de ambiente sensíveis (TOKEN, CHAT_ID)
├── docker-compose.yml
└── requirements.txt

Requisitos
Docker e Docker Compose

Bibliotecas Python no container:

pandas

pyarrow

requests

python-dotenv
