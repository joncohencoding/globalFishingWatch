# TODO: move these config variables to a config file?
import os
from typing import Dict

BASE_URL: str = "https://gateway.api.globalfishingwatch.org/v3/events"
ENCOUNTERS_ENDPOINT: str = f"{BASE_URL}"
# BEARER_TOKEN: str = os.environ["BEARER_TOKEN"]
BEARER_TOKEN: str = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtpZEtleSJ9.eyJkYXRhIjp7Im5hbWUiOiJKb25Db2hlbkdGV1Rva2VuIiwidXNlcklkIjozNTg3NCwiYXBwbGljYXRpb25OYW1lIjoiSm9uQ29oZW5HRldUb2tlbiIsImlkIjoxNjM1LCJ0eXBlIjoidXNlci1hcHBsaWNhdGlvbiJ9LCJpYXQiOjE3MTkzNDM5MjAsImV4cCI6MjAzNDcwMzkyMCwiYXVkIjoiZ2Z3IiwiaXNzIjoiZ2Z3In0.cf8euLHg2IoCfbsvCGpdf125HHt8KoVtS938CAcl-_mkns8leDq_JOZ36Hf628c3ms-vB2Cue7hP6DdNR_VqFkky0cyCXMtBtLhyREKryWLsndjHSAzplqLqpfeov8UazW8IO1e26ZbKs_QkpP1fQjKZTdDQPu626gnRAky1JEGckq1gzv3cs7NNel0NWTxE6lWaYlnSPzaiBSpUKC1f_Qc5245hIg_cvUo4B5G4l8kfPOYqSw7qNeAeccjP7fawnU6FP1WD71y-WhKBydZ-mc08cjCIm2wJl1dzZX6yn4yDLk9YFZMU0ur4jrwrYLmk_u3UvmB7USZbhW3VlVa_Z71-140In9MBdrKI9vVBiNlf1__kWPx7s6qr0a7ZmTB0tM21xniZNnnCSPJk9WgDzZPtp2PPmVSZeeKBR1p-h-O5Rf42dg7UB1xng1er5C8JDBhFO7Lb2YZIKRsjQ_TB_CpiLRWoUv25T4IVAcjfnQaJc37skJiEccAE5nNBazI8"

HEADERS: Dict[str, str] = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "AUTHORIZATION": f"Bearer {BEARER_TOKEN}"
}

ENCOUNTERS_QUERY_PARAMS: Dict[str, any] = {
    "limit": 1,
    "datasets[0]": "public-global-loitering-events:latest",
    "offset": 0,
    # "sort":"-start",
    # "start-date":"2024-06-20",
    # "encounter-types": ["CARRIER-FISHING", "FISHING-CARRIER"],
    # "include-regions": "MPA",
    # "confidences": [2, 3, 4],
}
# Timeout Settings (in seconds)
TIMEOUT: int = 60

# Retry settings
RETRY_COUNT = 1
RETRY_BACKOFF_FACTOR = 0.3
