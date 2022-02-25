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

def line_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    
    glBegin(GL_LINES)
    glColor3f(0.45,0.75,1.0)
    glVertex3i(10, 10, 0)
    glColor3f(0.8,1.0,0.5)
    glVertex3i(80, 80, 0)
    glEnd()
    
    glFlush()

def main():
	glutInit()
	glutInitDisplayMode(GLUT_RGB)
	glutCreateWindow("Line")
	glutDisplayFunc(line_draw)
	glutReshapeFunc(reshape)
	glutMouseFunc(mouse)
	glutMainLoop()

if __name__ == '__main__':
	main()
