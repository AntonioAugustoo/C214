import requests

def buscar_e_salvar_imagem():
    """
    Busca uma imagem aleatória da API Picsum Photos e a salva localmente.
    """
    url_da_api = "https://picsum.photos/800/600"
    
    print(f"Buscando imagem em: {url_da_api}")

    try:
        # Faz a requisição GET para a API
        resposta = requests.get(url_da_api)
        
        # Verifica se a requisição foi bem-sucedida (código 200)
        resposta.raise_for_status()

        # Abre um arquivo em modo de escrita binária ('wb') e salva o conteúdo da imagem
        with open("imagem_aleatoria.jpg", "wb") as arquivo_imagem:
            arquivo_imagem.write(resposta.content)
        
        print("\nSucesso! A imagem foi salva como 'imagem_aleatoria.jpg'")
        print("Este arquivo é o 'artefato' final do nosso processo de build.")

    except requests.exceptions.RequestException as erro:
        print(f"\nOcorreu um erro ao tentar buscar a imagem: {erro}")

# Ponto de entrada do script
if __name__ == "__main__":
    buscar_e_salvar_imagem()