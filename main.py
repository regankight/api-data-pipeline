# main.py
from fetch_api_data import fetch_api_data
from transform_clean import clean_data
from snapshot_kpis import snapshot_kpis

df_raw = fetch_api_data()
df_clean = clean_data(df_raw)
snapshot_kpis(df_clean)
