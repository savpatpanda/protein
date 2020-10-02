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

#init
pdb = open('4pcw.pdb')

#core
listOfAtoms = []

for line in pdb:
	elements = line.split()
	if elements[0] == "ATOM":
		coordinate = (float(elements[6]), float(elements[7]), float(elements[8]))
		listOfAtoms.append(coordinate)

x, y, z = getXYZ(listOfAtoms)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,zs=z, s= 15)
plt.show()