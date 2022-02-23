import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def main():
	glutInit()
	glutInitDisplayMode(GLUT_RGB)
	glutCreateWindow("Demo")
	glutInitWindowSize(500, 500)
	glutInitWindowPosition(50, 50)
	glutMainLoop()

if __name__ == '__main__':
	main()
