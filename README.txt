Final ETL portfolio 

This project demonstrates a full end-to-end Data Engineering ETL pipeline for e-commerce sales using:

Apache Airflow → Workflow Orchestration

PostgreSQL → Data Warehouse

dbt → Transformations & Data Modeling

Streamlit → Interactive Analytics Dashboard

Docker Compose → Containerization and automated setup

Run:
1. Extract this folder to a short path, e.g. C:\etl_portfolio_final
2. Start Docker Desktop
3. In PowerShell: cd C:\etl_portfolio_final
   docker compose build --no-cache
   docker compose up

Airflow UI: http://localhost:8080 
Streamlit Dashboard: http://localhost:8501

