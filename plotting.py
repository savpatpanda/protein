#imports
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

#init

coords = extractCoord("4pcw.pdb", alpha = True)
x, y, z = getXYZ(coords)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax.scatter(x,y,zs=z, s= 15)
ax.plot(x, y, zs = z)
plt.show()