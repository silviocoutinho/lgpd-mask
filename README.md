# Mascarar LGPD - Aplicativo para Remover Dados Sensíveis de PDFs

Este é um aplicativo simples desenvolvido em Python usando a biblioteca Tkinter e PyMuPDF (PyMuPDF é uma biblioteca para trabalhar com arquivos PDF) que permite mascarar informações sensíveis, como CPF e RG, em documentos PDF. O aplicativo oferece uma interface gráfica amigável para facilitar a remoção desses dados sensíveis de arquivos PDF de forma eficiente.

## Funcionalidades

O projeto oferece as seguintes funcionalidades:

- Inserção de números de CPF e RG em campos de entrada de texto.
- Seleção de um arquivo PDF no sistema de arquivos.
- Escolha de uma pasta de destino para salvar o arquivo PDF mascarado.
- Máscara para formatar e ocultar números de CPF e RG.
- Limpeza dos campos preenchidos.
- Interface gráfica intuitiva e de fácil utilização.

## Como Usar

Para usar o aplicativo, siga estas etapas:

1. **Requisitos**: Você precisará ter o Python instalado em seu sistema. Este aplicativo foi desenvolvido com o Python 3.

2. **Bibliotecas**: Instale as bibliotecas `tkinter` e `PyMuPDF` se elas não estiverem instaladas no seu sistema. Você pode instalá-lo usando o seguinte comando:

    pip install tkinter

    pip install PyMuPDF    

3. **Baixe o Código-Fonte**: Clone este repositório para sua máquina local:

    git clone [URL do Repositório]

4. **Execute o Aplicativo**:
   - Abra um terminal ou prompt de comando.
   - Navegue até a pasta onde você baixou o código deste aplicativo:

    cd #projeto...#

    - Execute o aplicativo com o seguinte comando:
     ```
     python main.py

     ou
     ```
    - Execute o arquivo Python `main.py` para iniciar a aplicação.

5. **Interface Gráfica**:
   - Na interface gráfica, você verá os seguintes campos e botões:

     - **CPF e RG**: Insira os números de CPF e RG nos campos de entrada apropriados.
     - **Arquivo PDF**: Clique no campo de entrada e selecione um arquivo PDF para processar.
     - **Pasta de Destino**: Clique no campo de entrada e selecione a pasta de destino onde o PDF mascarado será salvo.
     - **Mascarar**: Clique neste botão para aplicar a máscara aos números de CPF e RG inseridos.
     - **Limpar**: Clique neste botão para limpar todos os campos e recomeçar.

6. **Mascarar Informações**: Após inserir CPF, RG e selecionar um arquivo PDF e uma pasta de destino, clique no botão "Mascarar" para aplicar a máscara aos números de CPF e RG. O PDF mascarado será salvo na pasta de destino selecionada.

7. **Limpar Campos**: Se desejar, você pode limpar todos os campos preenchidos clicando no botão "Limpar".

## Personalização

Você pode personalizar este aplicativo de acordo com suas necessidades, incluindo a implementação das funções de máscara para CPF e RG.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para melhorar este aplicativo e enviar solicitações de pull com novos recursos ou correções de bugs.

-----------------------------------------------------------

Feito por 🚀 NN 🚀