from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# 🔹 Load dataset
df = pd.read_csv("merojob_all_jobs.csv")

# 🔹 Root endpoint
@app.get("/")
def home():
    return {"message": "MeroJob API is running"}

# 🔹 Get all jobs
@app.get("/jobs")
def get_jobs():
    return df.to_dict(orient="records")

# 🔹 Get limited jobs
@app.get("/jobs/limit/{n}")
def get_limited_jobs(n: int):
    return df.head(n).to_dict(orient="records")