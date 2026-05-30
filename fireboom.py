import os
import shutil

perfil = os.path.expanduser("~/Library/Application Support/Firefox/Profiles")

if not os.path.exists(perfil):
    print("Firefox não encontrado.")
    exit()

for pasta in os.listdir(perfil):
    caminho = os.path.join(perfil, pasta)
    historico = os.path.join(caminho, "places.sqlite")
    
    if os.path.exists(historico):
        os.remove(historico)
        print(f"Histórico apagado: {pasta}")

print("Feito! Abre o Firefox agora.")