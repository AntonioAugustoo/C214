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


---

## 🧪 Testes Unitários

### 🇧🇷 Português

O projeto inclui 20 testes unitários em `test_main.py` usando `pytest` e `unittest.mock`:

- **10 testes positivos:**
	- Verificam sucesso na busca, abertura e exibição da imagem, chamadas corretas de funções, mensagens de sucesso e execução sem exceções.
- **10 testes negativos:**
	- Simulam erros como URL inválida, timeout, resposta HTTP diferente de 200, conteúdo inválido, falha ao abrir/exibir imagem, erros da API e exceções inesperadas.

#### Como executar os testes:
```bash
pytest test_main.py
```

Todos os testes são comentados e cobrem cenários de sucesso e falha.

---

### 🇺🇸 English

The project includes 20 unit tests in `test_main.py` using `pytest` and `unittest.mock`:

- **10 positive tests:**
	- Check success in fetching, opening and displaying the image, correct function calls, success messages and execution without exceptions.
- **10 negative tests:**
	- Simulate errors such as invalid URL, timeout, non-200 HTTP response, invalid content, failure to open/display image, API errors and unexpected exceptions.

#### How to run the tests:
```bash
pytest test_main.py
```

All tests are commented and cover both success and failure scenarios.

---
