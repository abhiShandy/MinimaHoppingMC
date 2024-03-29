#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import sys

def plotTrajectory(fname='trajectory.dat'):
	trajectory = np.loadtxt(fname)
	print "Reading trajectories from", fname
	nElectrons = 1 + int(np.max(trajectory[:,0]))
	print "Read trajectory with", len(trajectory), "hops and", nElectrons, "electrons"

	# Create time grid
	tMax = trajectory[:,1].max()
	nSteps = 1e2
	deltaTime = tMax / nSteps
	timeGrid = np.linspace(0, tMax, nSteps+1)
	zPos = np.zeros((nElectrons, len(timeGrid))) #z-poistions of electrons in time grid
	print "Divided", tMax, "s into", nSteps, "intervals"

	#--- Trajectories --
	print "Analyzing Trajectories..."
	plt.figure(1, figsize=(10,6))
	# Iterate over all electrons and plot its displacement in z-direction
	for i in range(nElectrons):
		sel = np.where(trajectory[:,0]==i)[0]
		time = trajectory[sel,1]
		dz = trajectory[sel,4]
		zPos[i] = dz[np.minimum(np.searchsorted(time, timeGrid), len(dz)-1)]
		plt.plot(time, dz)
	plt.xlabel('Time [s]')
	plt.ylabel('Displacement in z-dir [nm]')
	#plt.savefig('trajectory.pdf', bbox_inches='tight') # uncomment to save the figure

	#--- Avg. Displacement and Avg. Velocity ---
	avgZpos = np.mean(zPos, axis=0)
	avgVel = (avgZpos[1:] - avgZpos[:-1])/deltaTime
	timeGridMid = 0.5*(timeGrid[1:] + timeGrid[:-1])

	plt.figure(2, figsize=(5,6))
	plt.subplot(211)
	plt.semilogx(timeGrid, np.array(avgZpos))
	plt.ylabel("Average Displacement in z-dir [nm]")
	plt.xlabel("Time [s]")

	plt.subplot(212)
	avgVel = np.array(avgVel)*1e-9 # convert from nm/s to m/s
	plt.semilogx(timeGridMid, avgVel)
	plt.ylabel("Average Velocity in z-dir [m/s]")
	plt.xlabel("Time [s]")
	v = np.median(avgVel)
	plt.axhline(v, c='k', ls='--')
	print("Velocity: {:.2e} [m/s]".format(v))
	#plt.savefig("avgDist.pdf", bbox_inches='tight') # uncomment to save the figure
	
	# uncomment to save the data
	#np.savetxt("avgZpos.dat", np.array([timeGrid, avgZpos]).T)
	#np.savetxt("avgVel.dat", np.array([timeGridMid, avgVel]).T)

	plt.show()

#--- Test Code ---
if __name__ == "__main__":
	if len(sys.argv)==1:
		plotTrajectory()
	else:
		plotTrajectory(sys.argv[1])