import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def line_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,1.0)
    glPointSize(5.0)
    
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(-0.65, 0.25)
    glEnd()
    
    glFlush()

def main():
	glutInit()
	glutInitDisplayMode(GLUT_RGB)
	glutCreateWindow("Line")
	glutInitWindowSize(500, 500)
	glutInitWindowPosition(50, 50)
	glutDisplayFunc(line_draw)
	glutMainLoop()

if __name__ == '__main__':
	main()
