from fastapi import FastAPI, HTTPException
import pandas as pd
import psycopg2 

# create object
app = FastAPI()

# create connection
conn = psycopg2.connect(
    dbname="neondb", user="neondb_owner", password="npg_sLfVg8iW4EwO",
    host="ep-steep-water-a102fmjl-pooler.ap-southeast-1.aws.neon.tech",
)

@app.get('/profiles')
def getProfiles():
    df = pd.read_sql("select * from profiles;", conn)

    return {
        "data": df.to_dict(orient="records")
    }

# create endpoint
@app.get("/")
def handleData():
    return {"message": "hello"}


@app.get("/dataset")
def getData():
    df = pd.read_csv("bikeshare_trips.csv")

    return {"data": df.to_dict(orient="records")}


@app.get("/dataset/{trip_id}")
def getData(trip_id: int):
    df = pd.read_csv("bikeshare_trips.csv")

    # filter
    result = df[df["trip_id"] == trip_id]

    # handling error
    if len(result) == 0:
        raise HTTPException(status_code=404, detail="Data not found")

    return {"data": result.to_dict(orient="records")}
