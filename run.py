#!/usr/bin/env python
from MinimaHoppingMC import *
from CarrierHoppingMC import *
from common import *

## Model parameters
params = { 
	"L": [ 50, 1089, 1089], #box size in nm
	"h": 2., #grid spacing in nm
	"Efield": 0.06, #electric field in V/nm
	"dosSigma": 0.224, #dos standard deviation in eV
	"dosMu": 0.0, #dos center in eV
	"T": 298., #temperature in Kelvin
	"hopDistance": 1., #average hop distance in nm
	"hopFrequency": 1e12, #attempt frequency in Hz
	"nElectrons": 16, #number of electrons to track
	"maxHops": 1e5, #maximum hops per MC runs
	"nRuns": 16, #number of MC runs
	"tMax": 1e3, #stop simulation at this time from start in seconds
	"epsBG": 2.6, #relative permittivity of polymer
	"useCoulomb": True, #whether to include e-e Coulomb interactions
	#--- Nano-particle parameters
	"epsNP": 3.6, #relative permittivity of nanoparticles
	"trapDepthNP": -1.1, #trap depth of nanoparticles in eV
	"radiusNP": 7, #radius of nanoparticles in nm
	"volFracNP": 0.05, #volume fraction of nanoparticles
	"nClusterMu": 30, #mean number of nanoparticles in each cluster (Gaussian distribution)
	"nClusterSigma": 5, #cluster size standard deviation in nm
	"clusterShape": "file", #one of "round", "random", "line" or "sheet"
	"shouldPlotNP": False #plot the electrostatic potential from PeriodicFD
}

## Execute the model
nRuns = params["nRuns"]

#model = MinimaHoppingMC(params)
model = CarrierHoppingMC(params)
trajectory = np.concatenate(parallelMap(model.run, cpu_count(), range(nRuns))) #Run in parallel and merge trajectories

np.savetxt("trajectory.dat", trajectory, fmt="%d %e %d %d %d", header="iElectron t[s] ix iy iz") #Save trajectories together

## Analyze electron trajectory
import analyze
analyze.plotTrajectory("trajectory.dat")