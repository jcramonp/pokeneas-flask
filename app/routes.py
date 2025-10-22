import os
from flask import Blueprint, jsonify, render_template
from .data import random_pokenea
from .utils import public_s3_url, container_id

bp = Blueprint("main", __name__)

S3_BUCKET = os.getenv("S3_BUCKET", "")
AWS_REGION = os.getenv("AWS_REGION", os.getenv("AWS_DEFAULT_REGION", "us-east-1"))

@bp.get("/api/pokenea")
def api_pokenea():
    p = random_pokenea()
    payload = {
        "id": p["id"],
        "nombre": p["nombre"],
        "altura": p["altura"],
        "habilidad": p["habilidad"],
        "container_id": container_id()
    }
    return jsonify(payload), 200

@bp.get("/imagen")
def imagen():
    p = random_pokenea()
    img_url = public_s3_url(S3_BUCKET, AWS_REGION, p.get("imagen_key", ""))
    return render_template(
        "imagen.html",
        nombre=p.get("nombre","Pokenea"),
        frase=p.get("frase","¡Atrápalos todos!"),
        img_url=img_url,
        container_id=container_id()
    )