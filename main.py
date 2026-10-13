import os
from fastapi import FastAPI, HTTPException
import pandas as pd

# Object FastAPI
app = FastAPI(
    title="BikeShare API",
    description="API untuk mengakses data perjalanan sepeda.",
    version="1.0.0"
)

# Endpoint - Beranda
@app.get('/')
def handleHome():
    username = (
        os.environ.get("USER")
        or os.environ.get("USERNAME")
        or "User"
    )

    return {
        "status": "success",
        "pesan": f"Halo, {username}! 👋😊",
        "selamat_datang": "Selamat datang di BikeShare API 🚲",
        "deskripsi": "Layanan API untuk mengakses data perjalanan sepeda.",
        "fitur": {
            "beranda": "/",
            "semua_data": "/data",
            "data_berdasarkan_id": "/data/{id}",
            "dokumentasi": "/docs"
        },
        "developer": "Abdurrahman Assgaf 👨‍💻",
        "versi": "1.0.0 --> masih awal awal 😅🤭"
    }


# Endpoint - Mengambil semua data
@app.get("/data")
def handleData():
    df = pd.read_csv("bikeshare_trips.csv")

    return {
        "data": df.to_dict(orient="records")
    }


# Endpoint - Mengambil data berdasarkan ID
@app.get("/data/{id}")
def handleDataFilter(id: int):
    df = pd.read_csv("bikeshare_trips.csv")

    hasil = df[df.trip_id == id]

    if len(hasil) == 0:
        # berikan error dengan fungsi raise bedanya return ngembalikan data
        # tapi kalo raise berupa objek yaitu adalah error yang di ambil dari
        # fungsi HTTPException di library FastAPI
        raise HTTPException(status_code=404, detail="🫢 datanya gak ada")
     
    return {
        "data": hasil.to_dict(orient="records")
    }