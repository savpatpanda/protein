#imports
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from enum import Enum

#constants
class AtomType(Enum):
	C = (5, "gray")
	O = (5, "red")
	N = (5, "blue")

#functions
def getXYZ(atomlist):
	x, y, z = [], [], []
	for i in atomlist:
		x.append(i[0])
		y.append(i[1])
		z.append(i[2])
	return x, y, z

def extractCoord(pdbFile, alpha = False):
	pdb = open(pdbFile)
	listOfAtoms = []

	for line in pdb:
		elements = line.split()
		if elements[0] == "ATOM":
			if alpha and elements[2] != "CA":
				continue
			coordinate = (float(elements[6]), float(elements[7]), float(elements[8]))
			listOfAtoms.append(coordinate)

	return listOfAtoms

def plotSpheres(atomList, axesObject, radius = 2):
	for i in atomList:
		u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:20j]
		x = radius*np.cos(u)*np.sin(v) + i[0]
		y = radius*np.sin(u)*np.sin(v) + i[1]
		z = radius*np.cos(v) + i[2]
		axesObject.plot_surface(x, y, z, color="grey")


#init
def pltFile(fileName:str):
	coords = extractCoord(fileName, alpha = True)
	x, y, z = getXYZ(coords)

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	#ax.scatter(x,y,zs=z, s= 15)
	#ax.plot(x, y, zs = z)
	plotSpheres(coords, ax)
	plt.show()

if __name__ == '__main__':
	pltFile("./data/4pcw.pdb")
