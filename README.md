**BOT ROLADOR DE DADOS PARA O SISTEMA VERBUM**
  # Funções:
    - /hello
      - Testa o bot dando um Olá.
    - /roll-one 
      - Rola um dado para o Narrador
    - /roll-nr4
      - Rola 3 dados com dificuldade padrão com sucessos em resultados 4 ou 8
    - /roll-nr7
      - Rola 3 dados com dificuldade alta com sucessos em resultados 7 ou 8

  # Para criar um executável é necessário instalar o pyinstaller globalmente e executar o comando:
    - pyinstaller --hidden-import CONSTANTS --onefile main.py

