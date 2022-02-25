import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def reshape(w,h):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 30.0, 0.0, 35.0, -1.0, 1.0)
    
def mouse(button,state,x,y):
	x=0
	y=0
	state=0
	
	if button==GLUT_LEFT_BUTTON:
		glutLeaveMainLoop()


def square_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.1, 0.1)
    glVertex3i(10,10,0)
    glColor3f(0.1, 0.1, 0.0)
    glVertex3i(10,30,0)
    glColor3f(0.1, 0.1, 1.0)
    glVertex3i(30,30,0)
    glColor3f(0.1, 0.3, 0.1)
    glVertex3i(30, 10,0)
    glEnd()
    
    glFlush()

def main():
	glutInit()
	glutInitDisplayMode(GLUT_RGB)
	glutCreateWindow("Square")
	glutDisplayFunc(square_draw)
	glutReshapeFunc(reshape)
	glutMouseFunc(mouse)
	glutMainLoop()

if __name__ == '__main__':
	main()
