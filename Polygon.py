import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

points = []

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

def pointCollect():
	global points
	n = int(input("Enter the degree of polygon: "))
	for i in range(n):
		print("Point ",i+1,":")
		x = int(input("Enter the x co-ordinate: "))
		y = int(input("Enter the x co-ordinate: "))
		points.append([x,y])
	
def draw():
	global points
	
	glClear(GL_COLOR_BUFFER_BIT)
	
	glBegin(GL_POLYGON)
	
	for i in range(len(points)):
		glVertex2i(points[i][0],points[i][1])
		
	glEnd()
	
	glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Polygon")
    glutDisplayFunc(draw)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse)
    glutMainLoop()
    
if __name__ == '__main__':
	pointCollect()
	main()
    
