import os    

credential_path = r"C:\Users\hi\Downloads\vijay-project-01-02377a19fe28.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


from google.cloud import bigquery
def hello_gcs():
    client = bigquery.Client()
    table_id = "vijay-project-01.Amazon_product_reviews.updated_sample_data"
  
    job_config = bigquery.LoadJobConfig(
        autodetect=True,
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
        write_disposition = 'WRITE_TRUNCATE'
    )
    uri = "gs://clean_json/*.ndjson"

    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )  
    load_job.result()  


hello_gcs()
print(f"File uploaded..")