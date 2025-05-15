# Visualizador-de-Imagens

Este é um aplicativo simples com interface gráfica para aplicar filtros em imagens, utilizando a biblioteca PySimpleGUI. O processamento de imagem é feito com OpenCV e Pillow.

![Editor de Imagens](/img/imagemInicio.png)

## Descrição

Este aplicativo permite que usuários carreguem, manipulem e salvem imagens usando uma interface gráfica. O programa oferece a utilização de filtros e transformações para edição de imagens.

[Link do video explicativo](https://drive.google.com/file/d/1GmbIP_AzMtxDcDksXWRGF8UptM6OmmFl/view?usp=sharing)

## Funcionalidades

### Filtros
- **Escala de Cinza**: Converte a imagem para preto e branco
- **Inversão de Cores**: Inverte todas as cores da imagem
- **Aumento de Contraste**: Melhora o contraste da imagem
- **Desfoque**: Aplica um efeito de desfoque gaussiano
- **Nitidez**: Aumenta a nitidez da imagem
- **Detecção de Bordas**: Destaca as bordas dos objetos na imagem

### Transformações
- **Rotação**: Rotacionar a imagem em 90°, 180° ou 270°
- **Redimensionamento**: Redimensionar a imagem para 50% ou 200% do tamanho original

## Instalação

1. Clone este repositório ou baixe os arquivos
   ```
   git clone https://github.com/seu-usuario/editor-de-imagens.git
   cd editor-de-imagens
   ```

2. Crie e ative um ambiente virtual 
   ```
   python -m venv venv
   
   # No Windows
   venv\Scripts\activate
   
   # No macOS/Linux
   source venv/bin/activate
   ```

3. Instale as dependências

   ```
   pip install opencv-python numpy PySimpleGUI pillow
   ```

## Como Usar

1. Execute o arquivo principal
   ```
   python app.py
   ```

2. Clique em "Procurar" para selecionar uma imagem do seu computador

3. Clique em "Carregar Imagem" para abrir a imagem selecionada

4. Selecione os filtros desejados

5. Clique em "Aplicar Filtros" para ver o resultado

6. Para transformações (rotação ou redimensionamento):
   - Selecione a opção desejada
   - Clique no botão correspondente ("Aplicar Rotação" ou "Aplicar Redimensionamento")

7. Para salvar a imagem processada, clique em "Salvar Imagem" e escolha o local

## Exemplos de Uso

### Aplicando filtros
1. Carregue uma imagem
2. Marque "Escala de Cinza" e "Detecção de Bordas"
3. Clique em "Aplicar Filtros"
4. A imagem exibirá as bordas detectadas em escala de cinza

![Exemplo 1](/img/ex1.png)

### Transformando uma imagem
1. Carregue uma imagem
2. Selecione "180°" nas opções de rotação
3. Clique em "Aplicar Rotação"
4. Selecione "200%" nas opções de redimensionamento
5. Clique em "Aplicar Redimensionamento"
6. Salve a imagem transformada

![Exemplo 2](/img/ex2.png)