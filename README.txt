Final ETL portfolio (Airflow + Postgres + dbt + Streamlit)

Run:
1. Extract this folder to a short path, e.g. C:\etl_portfolio_final
2. Start Docker Desktop
3. In PowerShell: cd C:\etl_portfolio_final
   docker compose build --no-cache
   docker compose up

Airflow UI: http://localhost:8080 (user: airflow / airflow)
Streamlit Dashboard: http://localhost:8501

Steps to present:
- Trigger DAG 'etl_sales_dag' in Airflow to load CSV and run dbt.
- After DAG completes, open the Streamlit dashboard to show charts and table.
