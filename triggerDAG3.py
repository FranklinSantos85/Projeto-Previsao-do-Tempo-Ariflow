from airflow import DAG
from airflow.operators.bash import BashOperator  # Import correto no Airflow 2.x
from datetime import datetime

# Definição da DAG
dag = DAG('trigger_dag3', description='Trigger3',
    schedule_interval=None, start_date=datetime(2024, 9, 28),
    catchup=False)

# Definição das Task1
task1 = BashOperator(task_id='task1', bash_command='exit 1', dag=dag) # "EXIT 1" para forçar a falha na task 1, de forma a executar a task 3 
task2 = BashOperator(task_id='task2', bash_command='exit 1', dag=dag) # "EXIT 1" para forçar a falha na task 1, de forma a executar a task 3 
task3 = BashOperator(task_id='task3', bash_command='sleep 5', dag=dag,
                         trigger_rule='all_failed' ) # all_failed, espera que todas as tasks anteriores falharem para ser executada a tastk 3

[task1,task2] >> task3
