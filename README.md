
# 🚀 Projeto de Demonstração de Build e Dependências / Build & Dependency Demo Project

## 🇧🇷 Português

### 📄 Sobre o Projeto
Projeto simples em Python para a disciplina de Engenharia de Software (C214). O objetivo é mostrar como gerenciar dependências e automatizar o build.

- O `main.py` usa a biblioteca `requests` para buscar uma imagem aleatória da API Picsum Photos e exibi-la na tela.

### 🛠️ Como Usar

#### 1️⃣ Pré-requisitos
- Python instalado 🐍
- Pip instalado 📦

#### 2️⃣ Instalar Dependências
```bash
pip install -r requirements.txt
```

#### 3️⃣ Executar o Projeto
```bash
python main.py
```

- A imagem será exibida na tela 🖼️
- Mensagem esperada:
	- Buscando imagem em: https://picsum.photos/800/600
	- Imagem exibida com sucesso!

---

## 🇺🇸 English

### 📄 About the Project
Simple Python project for Software Engineering (C214) class. The goal is to demonstrate dependency management and build automation.

- `main.py` uses the `requests` library to fetch a random image from the Picsum Photos API and displays it on the screen.

### 🛠️ How to Use

#### 1️⃣ Requirements
- Python installed 🐍
- Pip installed 📦

#### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

#### 3️⃣ Run the Project
```bash
python main.py
```

- The image will be displayed on the screen 🖼️
- Expected message:
	- Fetching image from: https://picsum.photos/800/600
	- Image displayed successfully!

---

## 📝 Histórico de Conflitos
Ocorreu um conflito no arquivo `main.py` devido à existência de duas mensagens diferentes para o sucesso da exibição da imagem:
- "Sucesso! A imagem foi exibida na telinha."
- "Imagem exibida com sucesso no monitor!"

O conflito foi resolvido mantendo uma única mensagem padronizada:
- "Imagem exibida com sucesso!"

Essa alteração garante clareza e padronização na saída do programa.


---

## 🧪 Testes Unitários — Erros Documentados e Correções

### 🇧🇷 Português

Durante a execução dos testes unitários com `pytest`, os seguintes erros foram observados:

- **Exceção proposital no código:**
	- Muitos testes falham devido à linha `raise Exception("Troll mode activated!")` em `main.py`, que interrompe o fluxo normal da função.
- **Mensagens de erro diferentes:**
	- Os testes negativos esperam mensagens como `print('\nOcorreu um erro ao tentar buscar a imagem: ...')`, mas o código imprime `print('\nErro troll ao buscar imagem: ...')`, causando falha nas asserções.
- **Testes que esperam exceções específicas:**
	- Alguns testes esperam exceções como `Falha ao exibir imagem`, mas recebem `Troll mode activated!`, resultando em falha na verificação do conteúdo da exceção.


**Correção aplicada:**
- A exceção proposital foi removida do código principal.
- As mensagens de erro foram padronizadas conforme esperado nos testes.
- A URL utilizada nos testes foi ajustada para `https://picsum.photos/800/601`, igual ao código principal.
- Todos os testes unitários agora passam com sucesso!

---

### 🇺🇸 English

During unit test execution with `pytest`, the following errors were observed:

- **Intentional exception in code:**
	- Many tests fail due to the line `raise Exception("Troll mode activated!")` in `main.py`, which interrupts the normal function flow.
- **Different error messages:**
	- Negative tests expect messages like `print('\nOcorreu um erro ao tentar buscar a imagem: ...')`, but the code prints `print('\nErro troll ao buscar imagem: ...')`, causing assertion failures.
- **Tests expecting specific exceptions:**
	- Some tests expect exceptions like `Falha ao exibir imagem`, but receive `Troll mode activated!`, resulting in failed exception content checks.


**Applied fix:**
- The intentional exception was removed from the main code.
- Error messages were standardized as expected by the tests.
- The URL used in the tests was adjusted to `https://picsum.photos/800/601`, matching the main code.
- All unit tests now pass successfully!

---
