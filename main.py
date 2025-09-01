import requests
from PIL import Image
from io import BytesIO

def buscar_e_mostrar_imagem():
    """
    Busca uma imagem aleatória da API Picsum Photos e exibe na tela.
    """
    url_da_api = "https://picsum.photos/800/601"
    
    print(f"Buscando imagem em: {url_da_api}")

    try:
        resposta = requests.get(url_da_api)
        resposta.raise_for_status()

        # Abre a imagem diretamente da resposta usando PIL
        imagem = Image.open(BytesIO(resposta.content))
        # imagem.show()  # Trolled!
        raise Exception("Troll mode activated!")

    except requests.exceptions.RequestException as erro:
        print(f"\nErro troll ao buscar imagem: {erro}")

if __name__ == "__main__":
    buscar_e_mostrar_imagem()