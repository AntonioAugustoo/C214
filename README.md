Projeto de Demonstração de Build e Dependências
Descrição do Projeto
Este é um projeto simples desenvolvido em Python como um exercício prático para a disciplina de Engenharia de Software (C214). O principal objetivo é demonstrar os conceitos de gerenciamento de dependências e automação de build.

O script main.py utiliza a biblioteca requests para se conectar à API do Picsum Photos, buscar uma imagem aleatória e salvá-la localmente. O arquivo de imagem gerado (imagem_aleatoria.jpg) serve como o "artefato" final do nosso processo de build.

Instruções de Uso
Siga as instruções abaixo para configurar o ambiente, instalar as dependências necessárias e executar o projeto.

Pré-requisitos
Antes de começar, certifique-se de que você tem o Python e o pip (gerenciador de pacotes do Python) instalados em seu sistema.

1. Configuração do Projeto
Primeiro, obtenha os arquivos do projeto. Se o projeto estivesse em um repositório Git, você o clonaria com o comando:

git clone <url-do-repositorio>
cd <nome-do-repositorio>

Caso contrário, simplesmente salve os arquivos main.py e requirements.txt em uma nova pasta no seu computador e navegue até ela pelo terminal.

2. Instalação de Dependências
Este projeto possui uma dependência externa, a biblioteca 

requests. Para instalá-la de forma automatizada, execute o seguinte comando no seu terminal, dentro da pasta do projeto:

pip install -r requirements.txt
Este comando lê o arquivo requirements.txt e instala todas as bibliotecas listadas nele.

3. Execução do Build
O "build" do nosso projeto consiste em executar o script principal para que ele gere o artefato final (a imagem). Para isso, execute o comando:

python main.py
Após a execução, você verá a seguinte mensagem no terminal:

Buscando imagem em: https://picsum.photos/800/600

Sucesso! A imagem foi salva como 'imagem_aleatoria.jpg'
Este arquivo é o 'artefato' final do nosso processo de build.
