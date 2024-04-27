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
    glEnd()

    # Janela
    glColor3f(0.7, 0.7, 1.0)  # Cor azul clara para as janelas
    glBegin(GL_QUADS)  #indicando o início de uma sequência de primitivas gráficas que serão desenhadas nesse caso, um quadrado
    glVertex2f(0.1, -0.25) # Vertice 1
    glVertex2f(0.5, -0.25)  # Vertice 2
    glVertex2f(0.5, 0.05) # Vertice 3
    glVertex2f(0.1, 0.05) # Vertice 4
    glEnd()

#-------------------------------------------------------------------------

    # Parede porta
    glColor3f(0.3, 0.0, 1.0)  # Cor azul
    glBegin(GL_QUADS) #indicando o início de uma sequência de primitivas gráficas que serão desenhadas nesse caso, um quadrado
    glVertex2f(-0.6, -0.5) # Vertice 1
    glVertex2f(-0.2, -0.5) # Vertice 2
    glVertex2f(-0.2, 0.2)# Vertice 3
    glVertex2f(-0.6, 0.2)# Vertice 4
    glEnd()

    # Porta
    glColor3f(0.3, 0.3, 0.3)  # Cor cinza para a porta
    glBegin(GL_QUADS) #indicando o início de uma sequência de primitivas gráficas que serão desenhadas nesse caso, um quadrado
    glVertex2f(-0.5, -0.5) # Vertice 1
    glVertex2f(-0.3, -0.5) # Vertice 2
    glVertex2f(-0.3, 0.0) # Vertice 3
    glVertex2f(-0.5, 0.0) # Vertice 4
    glEnd()

    # Maçaneta    
    glColor3f(0.7, 0.7, 1.0)  # Cor azul clara para as janelas
    glBegin(GL_QUADS) #indicando o início de uma sequência de primitivas gráficas que serão desenhadas nesse caso, um quadrado
    glVertex2f(-0.38, -0.25) # Vertice 1
    glVertex2f(-0.32, -0.25) # Vertice 2
    glVertex2f(-0.32, -0.27) # Vertice 3
    glVertex2f(-0.38, -0.27) # Vertice 4
    glEnd()
#---------------------------------------------------------------------------
    
    # Telhado da porta
    glColor3f(0.6, 0.3, 0.1)  # Cor marrom escura para o telhado
    glBegin(GL_TRIANGLES) #indicando o início de uma sequência de primitivas gráficas que serão desenhadas nesse caso, um quadrado
    glVertex2f(-0.6, 0.2) # Vertice 1
    glVertex2f(-0.2, 0.2)
    glVertex2f(-0.4, 0.55)
    glEnd()

    # Telhado maior
    glColor3f(0.3, 0.0, 1.0)  # Cor azul
    glBegin(GL_QUADS)
    glVertex2f(-0.2, 0.2)
    glVertex2f(0.8, 0.2)
    glVertex2f(0.55,  0.55)
    glVertex2f(-0.4, 0.55)
    glEnd()

#---------------------------------------------------------------------------
    # Chão
    glColor3f(0.6, 0.3, 0.1)  # Cor marrom para as paredes
    glBegin(GL_QUADS)
    glVertex2f(-1.0, -1.0)
    glVertex2f(1.0, -1.0)
    glVertex2f(1.0, -0.5)
    glVertex2f(-1.0, -0.5)
    glEnd()


def draw_day():
    # ceu
    glClearColor(0.5, 0.6, 1.0, 1.0)  # Cor de fundo azul (R, G, B, Alpha)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glutPostRedisplay()

    # sol
    glColor3f(1.0, 1.0, 0.0)  # Cor amarela do ceu
    glBegin(GL_QUADS)
    glVertex2f(0.75, 0.65)
    glVertex2f(0.98, 0.65)
    glVertex2f(0.98, 0.95)
    glVertex2f(0.75, 0.95)
    glEnd()

    # nuvem 1
    glColor3f(1.0, 1.0, 1.0)  # Cor branca das nuvens
    glBegin(GL_QUADS)
    glVertex2f(-0.9, 0.7)
    glVertex2f(-0.3, 0.7)
    glVertex2f(-0.3, 0.85)
    glVertex2f(-0.9, 0.85)
    glEnd()
    
    # nuvem 2
    glColor3f(1.0, 1.0, 1.0)  # Cor branca das nuvens
    glBegin(GL_QUADS)
    glVertex2f(0.5, 0.75)
    glVertex2f(-0.1, 0.75)
    glVertex2f(-0.1, 0.9)
    glVertex2f(0.5, 0.9)
    glEnd()

def draw_night():
    # ceu
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Cor de fundo azul (R, G, B, Alpha)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glutPostRedisplay()

    # lua
    glColor3f(1.0, 1.0, 1.0)  # Cor amarela do ceu
    glBegin(GL_QUADS)
    glVertex2f(0.75, 0.65)
    glVertex2f(0.98, 0.65)
    glVertex2f(0.98, 0.95)
    glVertex2f(0.75, 0.95)
    glEnd()

    #estrela 1
    glColor3f(1.0, 1.0, 1.0)  # Cor branca
    glBegin(GL_QUADS)
    glVertex2f(-0.9, 0.9)
    glVertex2f(-0.89, 0.9)
    glVertex2f(-0.89, 0.92)
    glVertex2f(-0.9, 0.92)
    glEnd()

    #estrela 2
    glColor3f(1.0, 1.0, 1.0)  # Cor branca
    glBegin(GL_QUADS)
    glVertex2f(-0.8, 0.7)
    glVertex2f(-0.81, 0.7)
    glVertex2f(-0.81, 0.72)
    glVertex2f(-0.8, 0.72)
    glEnd()

    #estrela 3
    glColor3f(1.0, 1.0, 1.0)  # Cor branca
    glBegin(GL_QUADS)
    glVertex2f(-0.84, -0.1)
    glVertex2f(-0.85, -0.1)
    glVertex2f(-0.85, -0.12)
    glVertex2f(-0.84, -0.12)
    glEnd()

    #estrela 4
    glColor3f(1.0, 1.0, 1.0)  # Cor branca
    glBegin(GL_QUADS)
    glVertex2f(0.0, 0.84)
    glVertex2f(0.01, 0.84)
    glVertex2f(0.01, 0.86)
    glVertex2f(0.0, 0.86)
    glEnd()

    #estrela 5
    glColor3f(1.0, 1.0, 1.0)  # Cor branca
    glBegin(GL_QUADS)
    glVertex2f(0.2, 0.76)
    glVertex2f(0.21, 0.76)
    glVertex2f(0.21, 0.78)
    glVertex2f(0.2, 0.78)
    glEnd()

    #estrela 6
    glColor3f(1.0, 1.0, 1.0)  # Cor branca
    glBegin(GL_QUADS)
    glVertex2f(0.4, 0.88)
    glVertex2f(0.41, 0.88)
    glVertex2f(0.41, 0.9)
    glVertex2f(0.4, 0.9)
    glEnd()

    #estrela 7
    glColor3f(1.0, 1.0, 1.0)  # Cor branca
    glBegin(GL_QUADS)
    glVertex2f(-0.4, 0.78)
    glVertex2f(-0.41, 0.78)
    glVertex2f(-0.41, 0.8)
    glVertex2f(-0.4, 0.8)
    glEnd()

    #estrela 8
    glColor3f(1.0, 1.0, 1.0)  # Cor branca
    glBegin(GL_QUADS)
    glVertex2f(-0.7, 0.2)
    glVertex2f(-0.71, 0.2)
    glVertex2f(-0.71, 0.22)
    glVertex2f(-0.7, 0.22)
    glEnd()



def keyboard( key, x, y ):
    d_byte = bytes([100])
    n_byte = bytes([110])
    global render_day
    global render_night

    if key == d_byte:
        print("teste")
        render_day = True
        render_night = False
        glutPostRedisplay()
        
    elif key == n_byte:
        render_day = False
        render_night = True
        glutPostRedisplay()
          

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    draw_house()

    if render_day:
        draw_day()
    if render_night:
        draw_night()
    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def init():
    glClearColor(0.5, 0.6, 1.0, 1.0)  # Cor de fundo azul (R, G, B, Alpha)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
glutInitWindowSize(800, 600)
glutCreateWindow("Casa em 2D")
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
init()
glutMainLoop()