#imports
import numpy as np
from enum import Enum
import collections

#constants
class AtomType(Enum):
	C = (5, "gray")
	O = (5, "red")
	N = (5, "blue")

Rotation = collections.namedtuple('Rotation', ['x','y','z'])

#functions
def normalize(listOfAtoms):
	firstResidue = listOfAtoms[0]
	for i in range(len(listOfAtoms)):
		listOfAtoms[i] = np.subtract(listOfAtoms[i],firstResidue)
	return listOfAtoms

def extractCoord(pdbFile, alpha = False):
	pdb = open(pdbFile)
	listOfAtoms = []

	for line in pdb:
		elements = line.split()
		if elements[0] == "ATOM":
			if alpha and elements[2] != "CA":
				continue
			coordinate = [float(elements[6]), float(elements[7]), float(elements[8])]
			listOfAtoms.append(coordinate)

	listOfAtoms = normalize(listOfAtoms)
	return listOfAtoms

def rotationMatrix(a, b, g):
	zRot = np.matrix([[np.cos(a/180*np.pi), -1*np.sin(a/180*np.pi), 0],[np.sin(a/180*np.pi), np.cos(a/180*np.pi), 0],[0, 0, 1]])
	yRot = np.matrix([[np.cos(b/180*np.pi), 0, np.sin(b/180*np.pi)],[0, 1, 0],[-1*np.sin(b/180*np.pi), 0, np.cos(b/180*np.pi)]])
	xRot = np.matrix([[1, 0, 0],[0, np.cos(g/180*np.pi), -1*np.sin(g/180*np.pi)],[0, np.sin(g/180*np.pi), np.cos(g/180*np.pi)]])
	endRot = np.matmul(np.matmul(zRot, yRot),xRot)
	return endRot

def rotate(coords, matrix):
	setOfCoords = []
	for i in range(len(coords)):
		vector = [[coords[i][0]],[coords[i][1]],[coords[i][2]]]
		output = matrix*vector
		transpose = [0]*len(vector)
		for i in range(len(transpose)):
			transpose[i] = float(output[i][0])
		setOfCoords.append(np.array(transpose))
	return setOfCoords

#init
def rotateFile(fileName:str, rotation:Rotation):
	coords = extractCoord(fileName, alpha = True)
	rotateMatrix = rotationMatrix(rotation.z, rotation.y, rotation.x)
	resulting = rotate(coords,rotateMatrix)
	print(resulting)

if __name__ == '__main__':
	pass
	#rotateFile("4pcw.pdb", Rotation(x = 0, y = 0, z = 30))
