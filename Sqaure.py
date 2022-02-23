import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def square_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(5.0)
    
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.1, 0.1)
    glVertex2f(0.1, 0.6)
    glColor3f(0.1, 0.1, 0.0)
    glVertex2f(0.6, 0.6)
    glColor3f(0.1, 0.1, 1.0)
    glVertex2f(0.6, 0.1)
    glColor3f(0.1, 0.3, 0.1)
    glVertex2f(0.1, 0.1)
    glEnd()
    
    glFlush()

def main():
	glutInit()
	glutInitDisplayMode(GLUT_RGB)
	glutCreateWindow("Line")
	glutInitWindowSize(500, 500)
	glutInitWindowPosition(500, 500)
	glutDisplayFunc(square_draw)
	glutMainLoop()

if __name__ == '__main__':
	main()
