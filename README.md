# comp-grafica
Repositório destinado à disciplina de Computação Gráfica - PUC MG


# Estrutura

O arquivo é estruturado em um arquivo main *main.py* onde é concentrado toda a lógica de código da interface funcional. Requisitos:

O arquivo *image_workspace.py* contém a lógica funcional do canvas, que permite desenhar, apagar e trocar de cores, além de atualizar as coordenadas (x,y) do usuário.

## Tecnologias 

As tecnologias utilizadas nesse projeto são:

- Python 3+
- Pip3 

A biblioteca utilizada nesse projeto é a biblioteca *tkinter*, que permite a criação de interfaces a partir de código escrito em python. 

# Para gerar um executável do projeto

Necessário instalar o PyInstaller:

`pip install Pyinstaller`

Para gerar o executável:

`pyinstaller -w -F main.py`

Para executar:

`./dist/main.exe`

# Como executar

O código fonte pode ser executado com `python3 main.py`.

Outra alternativa é executar o arquivo executável `main` presente no diretório principal do projeto.


# Algoritmo DDA

[DDA Line generation Algorithm in Computer Graphics](https://www.geeksforgeeks.org/dda-line-generation-algorithm-computer-graphics/)

O algoritmo DDA é descrito na literatura com um algoritmo de computacão gráfica para desenho de linhas. Os atributos de entrada do algoritmo são os pontos (x1,y1) e (x2, y2), em que a linha será desenhada entre esses pontos.

O algoritmo funciona da seguinte forma:

1. Calcula a diferença entre as coordenadas x (dX) e coordenadas y (dY)  
2. Se dX > dY então incrementa-se o "passo" do algoritmo, ou seja, em que direção será incrementado com dX. Caso contrário incrementa-se com dY
3. Calcula-se o incremento em x e y, dividindo pelos passos. 
4. Arredonda-se os valores de x e y para pintar o pixel.
5. O valor do X atual é incrementado com o incremento com o incremento de X e Y com o incremento de Y

# Algoritmo Bresenham

O algoritmo de Bresenham é descrito como um algoritmo de rasterização utilizado, nesse projeto, para desenhar retas em um workspace. Par isso o algoritmo recebe de entrada os pontos: (x1, y1) inicias e (x2, y2) finais.

O algoritmo está implementado na classe **image_workspace** e disponível na interface do projeto.

# Algoritmo Flood 

O algoritmo de Flood Fill, também conhecido como algoritmo de preenchimento de área, é um algoritmo utilizado em processamento de imagens e computação gráfica para preencher uma área delimitada por contornos com uma cor específica. O objetivo principal do algoritmo é colorir todas as partes conectadas de uma área delimitada por uma borda, de modo que nenhum pixel dentro da área permaneça com sua cor original.

Nesse projeto, Flood Fill foi implementado utilizando iteração em uma pilha.

# Algoritmo Boundary

Boundary Fill é uma técnica essencial para preencher áreas delimitadas em gráficos e imagens, permitindo que as regiões sejam coloridas de maneira consistente e controlada pelo usuário. Sua implementação pode variar em termos de eficiência e detalhes específicos da linguagem de programação utilizada.

Nesse projeto, Boundary Fill foi implementado utilizando recursão e exige uma alteração de limite de stack da linguagem.