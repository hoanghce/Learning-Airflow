from airflow import DAG, Dataset
from airflow.decorators import task
from datetime import date, datetime

my_file = Dataset("/tmp/my_file.txt")
my_file2 = Dataset("/tmp/my_file2.txt")

with DAG(
    dag_id = "producer",
    schedule = [my_file,my_file2],
    start_date = datetime(2023,1,1),
    catchup = False
):
    
    @task(outlets=[my_file])

    def update_dataset():
        with open(my_file.uri,"a+") as f:
            f.write("producer update")
    
    update_dataset()
