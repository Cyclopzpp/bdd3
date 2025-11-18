import os
import json
import hashlib
from sentence_transformers import SentenceTransformer

CARPETA_DISCURSOS = "DiscursosOriginales"
ARCHIVO_SALIDA = "discursos-final.json"

model = SentenceTransformer("all-MiniLM-L6-v2")

def calcular_sha256(texto: str) -> str:
    h = hashlib.sha256()
    h.update(texto.encode("utf-8"))
    return h.hexdigest()

def procesar_discursos():
    documentos = []

    for nombre in sorted(os.listdir(CARPETA_DISCURSOS)):
        if not nombre.lower().endswith(".txt"):
            continue

        ruta_archivo = os.path.join(CARPETA_DISCURSOS, nombre)

        with open(ruta_archivo, "r", encoding="utf-8") as f:
            texto = f.read().strip()

        _id = calcular_sha256(texto)
        embedding = model.encode(texto).tolist()

        doc = {
            "_id": _id,
            "texto": texto,
            "embedding": embedding
        }

        documentos.append(doc)
        print(f"Procesado {nombre}")

    # Guardar como JSON en forma de ARRAY
    with open(ARCHIVO_SALIDA, "w", encoding="utf-8") as out:
        json.dump(documentos, out, ensure_ascii=False, indent=2)

    print(f"\nSe guardaron {len(documentos)} documentos en {ARCHIVO_SALIDA}")

if __name__ == "__main__":
    procesar_discursos()
