project_id = 'uva-sensor-data'
gs_bucket_name = 'sensor-data'
bigquery_dataset_id = 'sensordata'
bigquery_table_id = 'logs'
bigquery_schema = [
    {
        "name":"temperature",
        "type":"FLOAT",
        "mode":"REQUIRED",
    },
    {
        "name":"humidity",
        "type":"FLOAT",
        "mode":"REQUIRED",
    },
    {
        "name":"dewpoint",
        "type":"FLOAT",
        "mode":"REQUIRED",
    },
    {
        "name":"pressure",
        "type":"FLOAT",
        "mode":"REQUIRED",
    },
    {
        "name":"light",
        "type":"FLOAT",
        "mode":"REQUIRED",
    },
    {
        "name":"wind_speed",
        "type":"FLOAT",
        "mode":"REQUIRED",
    },
    {
        "name":"wind_direction",
        "type":"FLOAT",
        "mode":"REQUIRED",
    },
    {
        "name":"rainfall",
        "type":"FLOAT",
        "mode":"REQUIRED"
    },
    {
        "name":"battery",
        "type":"FLOAT",
        "mode":"REQUIRED"
    },
    {
        "name":"unit_id",
        "type":"STRING",
        "mode":"REQUIRED"
    }
]
