import pandas as pd

df = pd.read_parquet("/home/josue/airflow-projeto/dags/resultados/saida.parquet")
print(df.head())