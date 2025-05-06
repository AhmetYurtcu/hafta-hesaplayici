from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from datetime import datetime, timedelta
from utils import tarih_to_hafta_bilgisi
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=FileResponse)
def get_index():
    return FileResponse(os.path.join("static", "index.html"))

@app.get("/hafta")
def hafta_no_getir(tarih: str = Query(...)):
    try:
        dt = datetime.strptime(tarih, "%Y-%m-%d")
        return tarih_to_hafta_bilgisi(dt)
    except ValueError:
        return {"hata": "Tarih formatı YYYY-MM-DD şeklinde olmalı."}

@app.get("/haftalar_arasi")
def haftalar_arasi(baslangic: str = Query(...), bitis: str = Query(...)):
    try:
        t1 = datetime.strptime(baslangic, "%Y-%m-%d")
        t2 = datetime.strptime(bitis, "%Y-%m-%d")

        if t1 > t2:
            t1, t2 = t2, t1

        haftalar = []
        tarih = t1

        while tarih <= t2:
            bilgi = tarih_to_hafta_bilgisi(tarih)
            haftalar.append(bilgi)
            tarih += timedelta(days=7)

        return {"adet": len(haftalar), "haftalar": haftalar}

    except ValueError:
        return {"hata": "Tarih formatı YYYY-MM-DD olmalıdır."}
