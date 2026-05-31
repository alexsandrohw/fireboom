import os

perfil = os.path.expanduser("~/Library/Application Support/Firefox/Profiles")

if not os.path.exists(perfil):
    print("Firefox não encontrado.")
    exit()

arquivos = [
    "places.sqlite",
    "places.sqlite-wal",
    "places.sqlite-shm",
    "cookies.sqlite",
    "cookies.sqlite-wal",
    "cookies.sqlite-shm",
]

for pasta in os.listdir(perfil):
    caminho = os.path.join(perfil, pasta)

    for arquivo in arquivos:
        caminho_arquivo = os.path.join(caminho, arquivo)

        if os.path.exists(caminho_arquivo):
            os.remove(caminho_arquivo)
            print(f"Apagado: {arquivo}")

print("Feito! Abre o Firefox agora.")
