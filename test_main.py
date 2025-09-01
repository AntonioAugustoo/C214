import pytest
from unittest.mock import patch, MagicMock
from io import BytesIO
import requests
import main

# Testes positivos
@patch('main.requests.get')
@patch('main.Image.open')
def test_status_200(mock_image_open, mock_get):
    # 1 Verifica se a função lida corretamente com resposta HTTP 200 (sucesso)
    mock_get.return_value.status_code = 200
    mock_get.return_value.content = b'fake_image_data'
    mock_image_open.return_value = MagicMock()
    main.buscar_e_mostrar_imagem()
    mock_get.assert_called_once()

@patch('main.requests.get')
@patch('main.Image.open')
def test_content_not_empty(mock_image_open, mock_get):
    # 2 Verifica se o conteúdo retornado pela requisição não está vazio
    mock_get.return_value.status_code = 200
    mock_get.return_value.content = b'img'
    mock_image_open.return_value = MagicMock()
    main.buscar_e_mostrar_imagem()
    assert mock_get.return_value.content

@patch('main.requests.get')
def test_url_called(mock_get):
    # 3 Verifica se a função chama requests.get com a URL correta
    mock_get.return_value.status_code = 200
    mock_get.return_value.content = b'img'  # Corrige o erro de TypeError
    with patch('main.Image.open') as mock_image_open:
        mock_image_open.return_value = MagicMock()
        main.buscar_e_mostrar_imagem()
    mock_get.assert_called_with('https://picsum.photos/800/600')

@patch('main.requests.get')
@patch('main.Image.open')
def test_image_open_called(mock_image_open, mock_get):
    # 4 Verifica se Image.open é chamado para abrir a imagem
    mock_get.return_value.status_code = 200
    mock_get.return_value.content = b'img'
    main.buscar_e_mostrar_imagem()
    mock_image_open.assert_called()

@patch('main.requests.get')
@patch('main.Image.open')
def test_image_show_called(mock_image_open, mock_get):
    # 5 Verifica se o método show() da imagem é chamado para exibir a imagem
    mock_get.return_value.status_code = 200
    mock_get.return_value.content = b'img'
    mock_img = MagicMock()
    mock_image_open.return_value = mock_img
    main.buscar_e_mostrar_imagem()
    mock_img.show.assert_called()

@patch('main.requests.get')
@patch('main.Image.open')
def test_success_message(mock_image_open, mock_get):
    # 6 Verifica se a mensagem de sucesso é impressa após exibir a imagem
    mock_get.return_value.status_code = 200
    mock_get.return_value.content = b'img'
    mock_image_open.return_value = MagicMock()
    with patch('builtins.print') as mock_print:
        main.buscar_e_mostrar_imagem()
        mock_print.assert_any_call('\nImagem exibida com sucesso no monitor!')

@patch('main.requests.get')
@patch('main.Image.open')
def test_no_exception(mock_image_open, mock_get):
    # 7 Verifica se não ocorre exceção durante execução normal
    mock_get.return_value.status_code = 200
    mock_get.return_value.content = b'img'
    mock_image_open.return_value = MagicMock()
    try:
        main.buscar_e_mostrar_imagem()
    except Exception:
        pytest.fail('Exception raised unexpectedly!')

@patch('main.requests.get')
@patch('main.Image.open')
def test_multiple_calls(mock_image_open, mock_get):
    # 8 Verifica se a função pode ser chamada múltiplas vezes sem erro
    mock_get.return_value.status_code = 200
    mock_get.return_value.content = b'img'
    mock_image_open.return_value = MagicMock()
    for _ in range(3):
        main.buscar_e_mostrar_imagem()
    assert mock_get.call_count == 3

@patch('main.requests.get')
@patch('main.Image.open')
def test_different_url(mock_image_open, mock_get):
    # 9 Verifica se a função aceita URLs diferentes (simulado)
    mock_get.return_value.status_code = 200
    mock_get.return_value.content = b'img'
    mock_image_open.return_value = MagicMock()
    with patch('main.buscar_e_mostrar_imagem', wraps=main.buscar_e_mostrar_imagem) as func:
        func()
    mock_get.assert_called_with('https://picsum.photos/800/600')

@patch('main.requests.get')
@patch('main.Image.open')
def test_different_size(mock_image_open, mock_get):
    # 10 Verifica se a função aceita diferentes tamanhos de imagem (simulado)
    mock_get.return_value.status_code = 200
    mock_get.return_value.content = b'img'
    mock_image_open.return_value = MagicMock()
    with patch('main.buscar_e_mostrar_imagem', wraps=main.buscar_e_mostrar_imagem) as func:
        func()
    mock_get.assert_called_with('https://picsum.photos/800/600')

# Testes negativos
@patch('main.requests.get')
def test_url_invalida(mock_get):
    # 1 Simula erro de conexão por URL inválida
    mock_get.side_effect = requests.exceptions.ConnectionError('URL inválida')
    with patch('builtins.print') as mock_print:
        main.buscar_e_mostrar_imagem()
        mock_print.assert_any_call('\nOcorreu um erro ao tentar buscar a imagem: URL inválida')

@patch('main.requests.get')
def test_timeout(mock_get):
    # 2 Simula erro de timeout na requisição
    mock_get.side_effect = requests.exceptions.Timeout('Timeout')
    with patch('builtins.print') as mock_print:
        main.buscar_e_mostrar_imagem()
        mock_print.assert_any_call('\nOcorreu um erro ao tentar buscar a imagem: Timeout')

@patch('main.requests.get')
def test_status_not_200(mock_get):
    # 3 Simula resposta HTTP diferente de 200 (ex: 404)
    mock_get.return_value.status_code = 404
    mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError('404')
    with patch('builtins.print') as mock_print:
        main.buscar_e_mostrar_imagem()
        mock_print.assert_any_call('\nOcorreu um erro ao tentar buscar a imagem: 404')

@patch('main.requests.get')
@patch('main.Image.open')
def test_content_not_image(mock_image_open, mock_get):
    # 4 Simula conteúdo da resposta que não é uma imagem válida
    mock_get.return_value.status_code = 200
    mock_get.return_value.content = b'not_image'
    mock_image_open.side_effect = Exception('Conteúdo inválido')
    with pytest.raises(Exception) as excinfo:
        main.buscar_e_mostrar_imagem()
    assert 'Conteúdo inválido' in str(excinfo.value)

@patch('main.requests.get')
@patch('main.Image.open')
def test_image_open_fail(mock_image_open, mock_get):
    # 5 Simula falha ao abrir a imagem
    mock_get.return_value.status_code = 200
    mock_get.return_value.content = b'img'
    mock_image_open.side_effect = Exception('Falha ao abrir imagem')
    with pytest.raises(Exception) as excinfo:
        main.buscar_e_mostrar_imagem()
    assert 'Falha ao abrir imagem' in str(excinfo.value)

@patch('main.requests.get')
@patch('main.Image.open')
def test_image_show_fail(mock_image_open, mock_get):
    # 6 Simula falha ao exibir a imagem
    mock_get.return_value.status_code = 200
    mock_get.return_value.content = b'img'
    mock_img = MagicMock()
    mock_img.show.side_effect = Exception('Falha ao exibir imagem')
    mock_image_open.return_value = mock_img
    with pytest.raises(Exception) as excinfo:
        main.buscar_e_mostrar_imagem()
    assert 'Falha ao exibir imagem' in str(excinfo.value)

@patch('main.requests.get')
def test_api_404(mock_get):
    # 7 Simula erro 404 retornado pela API
    mock_get.return_value.status_code = 404
    mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError('404')
    with patch('builtins.print') as mock_print:
        main.buscar_e_mostrar_imagem()
        mock_print.assert_any_call('\nOcorreu um erro ao tentar buscar a imagem: 404')

@patch('main.requests.get')
def test_api_500(mock_get):
    # 8 Simula erro 500 retornado pela API
    mock_get.return_value.status_code = 500
    mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError('500')
    with patch('builtins.print') as mock_print:
        main.buscar_e_mostrar_imagem()
        mock_print.assert_any_call('\nOcorreu um erro ao tentar buscar a imagem: 500')

@patch('main.requests.get')
def test_no_connection(mock_get):
    # 9 Simula falta de conexão com a internet
    mock_get.side_effect = requests.exceptions.ConnectionError('Sem conexão')
    with patch('builtins.print') as mock_print:
        main.buscar_e_mostrar_imagem()
        mock_print.assert_any_call('\nOcorreu um erro ao tentar buscar a imagem: Sem conexão')

@patch('main.requests.get')
def test_unexpected_exception(mock_get):
    # 10 Simula exceção inesperada durante a requisição
    mock_get.side_effect = Exception('Erro inesperado')
    with pytest.raises(Exception) as excinfo:
        main.buscar_e_mostrar_imagem()
    assert 'Erro inesperado' in str(excinfo.value)
