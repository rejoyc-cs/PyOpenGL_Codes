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


def triangle_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    
    glBegin(GL_TRIANGLES)
    glVertex3f(5,5,0)
    glColor3f(0.75,0.5,0.4)
    glVertex3f(25,5,0)
    glColor3f(0.15,1.0,0.25)
    glVertex3i(15,15,0)
    glColor3f(0.1,0.55,0.45)
    glEnd()
    
    ''' 
    #If reshape is not applied
    glBegin(GL_TRIANGLES)
    glVertex3f(0.5,0.5,0)
    glColor3f(0.75,0.5,0.4)
    glVertex3f(0.25,0.5,0)
    glColor3f(0.15,1.0,0.25)
    glVertex3f(0.15,0.15,0)
    glColor3f(0.1,0.55,0.45)
    glEnd()
    '''
    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Triangle")
    glutDisplayFunc(triangle_draw)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse)
    glutMainLoop()
    
    
    
if __name__ == '__main__':
	main()
    
