#Aluno: Jonas de Moura Teixeia 
#Matrícula: 01023673

#OBS 1:
#Ao inciar o programa, eu defini o ceu na cor azul, e ao clicar as teclas "n" ou "d" é renderizado os elementos que
#definem o dia ou noite. Eu fiz assim, pois não entendi em qual estado o ceu se iniciaria.

#OBS 2:
#Eu utilizei uma abordagem diferente, onde a Api do OpenGl disponibiliza funções que abstraem a configuração e criação de objetos.

from OpenGL.GL import *
from OpenGL.GLUT import *

render_day = False  #variavel de controle para a condição de dia
render_night = False  #variavel de controle para a condição de noite

#Função que desenha a casa
def draw_house():
    # Parede Janela
    glColor3f(0.8, 0.6, 0.4)  # Cor marrom para as paredes
    glBegin(GL_QUADS)  #indicando o início de uma sequência de primitivas gráficas que serão desenhadas nesse caso, um quadrado
    glVertex2f(-0.2, -0.5) # Vertice 1
    glVertex2f(0.8, -0.5)   # Vertice 2
    glVertex2f(0.8, 0.2)    # Vertice 3
    glVertex2f(-0.2, 0.2) # Vertice 4
    glEnd() #indicando o término da sequência de definição de primitivas gráficas

    # Janela
    glColor3f(0.7, 0.7, 1.0)  # Cor azul clara para as janelas
    glBegin(GL_QUADS)  #indicando o início de uma sequência de primitivas gráficas que serão desenhadas nesse caso, um quadrado
    glVertex2f(0.1, -0.25) # Vertice 1
    glVertex2f(0.5, -0.25)  # Vertice 2
    glVertex2f(0.5, 0.05) # Vertice 3
    glVertex2f(0.1, 0.05) # Vertice 4
    glEnd() #indicando o término da sequência de definição de primitivas gráficas

#-------------------------------------------------------------------------

    # Parede porta
    glColor3f(0.3, 0.0, 1.0)  # Cor azul
    glBegin(GL_QUADS) #indicando o início de uma sequência de primitivas gráficas que serão desenhadas nesse caso, um quadrado
    glVertex2f(-0.6, -0.5) # Vertice 1
    glVertex2f(-0.2, -0.5) # Vertice 2
    glVertex2f(-0.2, 0.2)# Vertice 3
    glVertex2f(-0.6, 0.2)# Vertice 4
    glEnd() #indicando o término da sequência de definição de primitivas gráficas

    # Porta
    glColor3f(0.3, 0.3, 0.3)  # Cor cinza para a porta
    glBegin(GL_QUADS) #indicando o início de uma sequência de primitivas gráficas que serão desenhadas nesse caso, um quadrado
    glVertex2f(-0.5, -0.5) # Vertice 1
    glVertex2f(-0.3, -0.5) # Vertice 2
    glVertex2f(-0.3, 0.0) # Vertice 3
    glVertex2f(-0.5, 0.0) # Vertice 4
    glEnd() #indicando o término da sequência de definição de primitivas gráficas

    # Maçaneta    
    glColor3f(0.7, 0.7, 1.0)  # Cor azul clara para as janelas
    glBegin(GL_QUADS) #indicando o início de uma sequência de primitivas gráficas que serão desenhadas nesse caso, um quadrado
    glVertex2f(-0.38, -0.25) # Vertice 1
    glVertex2f(-0.32, -0.25) # Vertice 2
    glVertex2f(-0.32, -0.27) # Vertice 3
    glVertex2f(-0.38, -0.27) # Vertice 4
    glEnd() #indicando o término da sequência de definição de primitivas gráficas
#---------------------------------------------------------------------------
    
    # Telhado da porta
    glColor3f(0.6, 0.3, 0.1)  # Cor marrom escura para o telhado
    glBegin(GL_TRIANGLES) #indicando o início de uma sequência de primitivas gráficas que serão desenhadas nesse caso, um triangulo
    glVertex2f(-0.6, 0.2) # Vertice 1
    glVertex2f(-0.2, 0.2) # Vertice 2
    glVertex2f(-0.4, 0.55) # Vertice 3
    glEnd() #indicando o término da sequência de definição de primitivas gráficas

    # Telhado maior
    glColor3f(0.3, 0.0, 1.0)  # Cor azul
    glBegin(GL_QUADS) #indicando o início de uma sequência de primitivas gráficas que serão desenhadas nesse caso, um quadrado
    glVertex2f(-0.2, 0.2) # Vertice 1
    glVertex2f(0.8, 0.2) # Vertice 2
    glVertex2f(0.55,  0.55) # Vertice 3
    glVertex2f(-0.4, 0.55) # Vertice 4
    glEnd() #indicando o término da sequência de definição de primitivas gráficas

#---------------------------------------------------------------------------
    # Chão
    glColor3f(0.6, 0.3, 0.1)  # Cor marrom para as paredes
    glBegin(GL_QUADS) #indicando o início de uma sequência de primitivas gráficas que serão desenhadas nesse caso, um quadrado
    glVertex2f(-1.0, -1.0) # Vertice 1
    glVertex2f(1.0, -1.0) # Vertice 2
    glVertex2f(1.0, -0.5) # Vertice 3
    glVertex2f(-1.0, -0.5) # Vertice 4
    glEnd() #indicando o término da sequência de definição de primitivas gráficas


#função para desenhar o cenário do dia 
def draw_day():
    # ceu
    glClearColor(0.5, 0.6, 1.0, 1.0)  # Cor de fundo azul (R, G, B, Alpha)
    glutPostRedisplay() #dando reload na tela para pegar as atualizações do ceu

    # sol
    glColor3f(1.0, 1.0, 0.0)  # Cor amarela do ceu
    glBegin(GL_QUADS) #indicando o início de uma sequência de primitivas gráficas que serão desenhadas nesse caso, um quadrado
    glVertex2f(0.75, 0.65) # Vertice 1
    glVertex2f(0.98, 0.65) # Vertice 2
    glVertex2f(0.98, 0.95) # Vertice 3
    glVertex2f(0.75, 0.95) # Vertice 4
    glEnd() #indicando o término da sequência de definição de primitivas gráficas

    # nuvem 1
    glColor3f(1.0, 1.0, 1.0)  # Cor branca das nuvens
    glBegin(GL_QUADS) #indicando o início de uma sequência de primitivas gráficas que serão desenhadas nesse caso, um quadrado
    glVertex2f(-0.9, 0.7) # Vertice 1
    glVertex2f(-0.3, 0.7) # Vertice 2
    glVertex2f(-0.3, 0.85) # Vertice 3
    glVertex2f(-0.9, 0.85) # Vertice 4
    glEnd() #indicando o término da sequência de definição de primitivas gráficas
    
    # nuvem 2
    glColor3f(1.0, 1.0, 1.0)  # Cor branca das nuvens
    glBegin(GL_QUADS) #indicando o início de uma sequência de primitivas gráficas que serão desenhadas nesse caso, um quadrado
    glVertex2f(0.5, 0.75) # Vertice 1
    glVertex2f(-0.1, 0.75) # Vertice 2
    glVertex2f(-0.1, 0.9) # Vertice 3
    glVertex2f(0.5, 0.9) # Vertice 4
    glEnd() #indicando o término da sequência de definição de primitivas gráficas

def draw_night():
    # ceu
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Cor de fundo azul (R, G, B, Alpha)
    glutPostRedisplay() #dando reload na tela para pegar as atualizações do ceu

    # lua
    glColor3f(1.0, 1.0, 1.0)  # Cor amarela do ceu
    glBegin(GL_QUADS) #indicando o início de uma sequência de primitivas gráficas que serão desenhadas nesse caso, um quadrado
    glVertex2f(0.75, 0.65) # Vertice 1
    glVertex2f(0.98, 0.65) # Vertice 2
    glVertex2f(0.98, 0.95) # Vertice 3
    glVertex2f(0.75, 0.95) # Vertice 4
    glEnd() #indicando o término da sequência de definição de primitivas gráficas

    #estrela 1
    glColor3f(1.0, 1.0, 1.0)  # Cor branca
    glBegin(GL_QUADS) #indicando o início de uma sequência de primitivas gráficas que serão desenhadas nesse caso, um quadrado
    glVertex2f(-0.9, 0.9) # Vertice 1
    glVertex2f(-0.89, 0.9) # Vertice 2
    glVertex2f(-0.89, 0.92) # Vertice 3
    glVertex2f(-0.9, 0.92) # Vertice 4
    glEnd() #indicando o término da sequência de definição de primitivas gráficas

    #estrela 2
    glColor3f(1.0, 1.0, 1.0)  # Cor branca
    glBegin(GL_QUADS) #indicando o início de uma sequência de primitivas gráficas que serão desenhadas nesse caso, um quadrado
    glVertex2f(-0.8, 0.7) # Vertice 1
    glVertex2f(-0.81, 0.7) # Vertice 2
    glVertex2f(-0.81, 0.72) # Vertice 3
    glVertex2f(-0.8, 0.72) # Vertice 4
    glEnd() #indicando o término da sequência de definição de primitivas gráficas

    #estrela 3
    glColor3f(1.0, 1.0, 1.0)  # Cor branca
    glBegin(GL_QUADS) #indicando o início de uma sequência de primitivas gráficas que serão desenhadas nesse caso, um quadrado
    glVertex2f(-0.84, -0.1) # Vertice 1
    glVertex2f(-0.85, -0.1) # Vertice 2
    glVertex2f(-0.85, -0.12) # Vertice 3
    glVertex2f(-0.84, -0.12) # Vertice 4
    glEnd() #indicando o término da sequência de definição de primitivas gráficas

    #estrela 4
    glColor3f(1.0, 1.0, 1.0)  # Cor branca
    glBegin(GL_QUADS) #indicando o início de uma sequência de primitivas gráficas que serão desenhadas nesse caso, um quadrado
    glVertex2f(0.0, 0.84) # Vertice 1
    glVertex2f(0.01, 0.84) # Vertice 2
    glVertex2f(0.01, 0.86) # Vertice 3
    glVertex2f(0.0, 0.86) # Vertice 4
    glEnd() #indicando o término da sequência de definição de primitivas gráficas

    #estrela 5
    glColor3f(1.0, 1.0, 1.0)  # Cor branca
    glBegin(GL_QUADS) #indicando o início de uma sequência de primitivas gráficas que serão desenhadas nesse caso, um quadrado
    glVertex2f(0.2, 0.76) # Vertice 1
    glVertex2f(0.21, 0.76) # Vertice 2
    glVertex2f(0.21, 0.78) # Vertice 3
    glVertex2f(0.2, 0.78) # Vertice 4
    glEnd() #indicando o término da sequência de definição de primitivas gráficas

    #estrela 6
    glColor3f(1.0, 1.0, 1.0)  # Cor branca
    glBegin(GL_QUADS) #indicando o início de uma sequência de primitivas gráficas que serão desenhadas nesse caso, um quadrado
    glVertex2f(0.4, 0.88) # Vertice 1
    glVertex2f(0.41, 0.88) # Vertice 2
    glVertex2f(0.41, 0.9)  # Vertice 3
    glVertex2f(0.4, 0.9) # Vertice 4
    glEnd() #indicando o término da sequência de definição de primitivas gráficas

    #estrela 7
    glColor3f(1.0, 1.0, 1.0)  # Cor branca
    glBegin(GL_QUADS) #indicando o início de uma sequência de primitivas gráficas que serão desenhadas nesse caso, um quadrado
    glVertex2f(-0.4, 0.78) # Vertice 1
    glVertex2f(-0.41, 0.78) # Vertice 2
    glVertex2f(-0.41, 0.8) # Vertice 3
    glVertex2f(-0.4, 0.8) # Vertice 4
    glEnd() #indicando o término da sequência de definição de primitivas gráficas

    #estrela 8
    glColor3f(1.0, 1.0, 1.0)  # Cor branca
    glBegin(GL_QUADS) #indicando o início de uma sequência de primitivas gráficas que serão desenhadas nesse caso, um quadrado
    glVertex2f(-0.7, 0.2) # Vertice 1
    glVertex2f(-0.71, 0.2) # Vertice 2
    glVertex2f(-0.71, 0.22) # Vertice 3
    glVertex2f(-0.7, 0.22) # Vertice 4
    glEnd() #indicando o término da sequência de definição de primitivas gráficas



def keyboard( key, x, y ):
    d_byte = bytes([100])  #byte correspondente a tecla "d"
    n_byte = bytes([110]) #byte correspondente a tecla "n"
    global render_day #carregando a variavel como global para ter visibilidade dentro da funcao
    global render_night #carregando a variavel como global para ter visibilidade dentro da funcao

    if key == d_byte: #verificando se a tecla apertada é igual a "n"
        render_day = True #definindo a variavel render_day = true
        render_night = False #definindo a variavel render_night = false
        glutPostRedisplay() #dando reload na tela para pegar as atualizações do ceu
        
    elif key == n_byte:
        render_day = False #definindo a variavel render_day = false
        render_night = True #definindo a variavel render_night = true
        glutPostRedisplay() #dando reload na tela para pegar as atualizações do ceu
          

def display(): 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #limpando os buffers de cor e de profundidade antes de renderizar uma nova cena.
    glLoadIdentity() #carregando matriz de identidade
    draw_house() #chamando a função que desenha o shape da casa

    if render_day: #verificando se a variavel que armazena se a tecla d foi pressionada está com valor "True"
        draw_day() #chamando a função que altera a tela desenhando os componentes do dia
    if render_night: #verificando se a variavel que armazena se a tecla n foi pressionada está com valor "True"
        draw_night() #chamando a função que altera a tela desenhando os componentes da noite
    glutSwapBuffers() #trocando os buffers de vídeo

def reshape(w, h):
    glViewport(0, 0, w, h) #definindo a área de visualização igual ao tamanho da janela de renderização

def init():
    glClearColor(0.5, 0.6, 1.0, 1.0)  # Cor de fundo azul (R, G, B, Alpha)
    glutPostRedisplay() #dando reload na tela para pegar as atualizações

# Cria contexto OpenGL e configura janela
glutInit() #inciando o ambiente OpenGL e o GLUT
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)  #especificando a exibição da janela
glutInitWindowSize(800, 600) #definindo o tamanho da janela
glutCreateWindow("Casa em 2D") #titulo da tela

# Chama funcoes Callback
glutDisplayFunc(display) #indicando qual função que terá os parametros para exibição
glutReshapeFunc(reshape) #indicando a função que define a visualizaçãoda da janela de renderização
glutKeyboardFunc(keyboard) #indicando qual função é responsável por definir ações com teclado

init() #chamando as configurações iniciais para a tela
glutMainLoop() #chamando a função de loop para capturar ações como cliques no teclado e mouse e atualizar a janela 