"""
Ponto de entrada principal para o Editor de Imagens
"""

from src.app import ImageFilterApp

def main():
    """Função principal que inicia a aplicação"""
    app = ImageFilterApp()
    app.run()

if __name__ == '__main__':
    main()