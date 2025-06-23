from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
from datetime import datetime
import pandas as pd
import os
import requests
from dotenv import dotenv_values
from config import BOT_TOKEN, CHAT_ID

env_vars = dotenv_values("/opt/airflow/dags/.env")
os.environ.update(env_vars)



def converter_csv_para_parquet():
    csv_path = "/opt/airflow/dags/dados/dados.csv"
    parquet_path = "/opt/airflow/dags/resultados/saida.parquet"

    df = pd.read_csv(csv_path)
    df.to_parquet(parquet_path, index=False)

    print("Visualização do DataFrame:")
    print(df.head().to_string())

    mensagem = f"""
    ✅ Conversão finalizada com sucesso!
    📁 Arquivo salvo: {parquet_path}
    👇 Preview:
    {df.head().to_string(index=False)}
    """

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": mensagem
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

with DAG(
    dag_id="tratar_csv_para_parquet",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["exemplo", "csv", "parquet"]
) as dag:

    tarefa_converter = PythonOperator(
        task_id="converter_csv",
        python_callable=converter_csv_para_parquet
    )
