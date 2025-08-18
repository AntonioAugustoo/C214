import requests

def buscar_e_salvar_imagem():
    """
    Busca uma imagem aleatória da API Picsum Photos e a salva localmente.
    Gera um erro proposital alterando o protocolo da URL.
    """
    url_da_api = "htttp://picsum.photos/800/600"  # Erro proposital: 'htttp' ao invés de 'http'
    
    print(f"Buscando imagem em: {url_da_api}")

    try:
        resposta = requests.get(url_api)
        resposta.raise_for_status()

        with open("imagem_aleatoria.jpg", "wb") as arquivo_imagem:
            arquivo_imagem.write(resposta.content)
        
        print("\nSucesso! A imagem foi salva como 'imagem_aleatoria.jpg'")
        print("Este arquivo é o 'artefato' final do nosso processo de build.")

    except requests.exceptions.RequestException as erro:
        print(f"\nOcorreu um erro ao tentar buscar a imagem: {erro}")

if __name__ == "__main__":
    buscar_e_salvar_imagem()