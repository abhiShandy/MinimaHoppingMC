from MinimaHoppingMC import *
from common import *

## Model parameters
params = { 
	"L": [ 1, 1e3, 1e3 ], #box size in nm
	"h": 1., #grid spacing in nm
	"Efield": 0.06, #electric field in V/nm
	"dosSigma": 0.224, #dos standard deviation in eV
	"dosMu": 0.0, #dos center in eV
	"T": 298., #temperature in Kelvin
	"hopDistance": 1., #average hop distance in nm
	"hopFrequency": 1e12, #attempt frequency in Hz
	"nElectrons": 16, #number of electrons to track
	"maxHops": 5e4, #maximum hops per MC runs
	"nRuns": 16, #number of MC runs
	"tMax": 1e3, #stop simulation at this time from start in seconds
	"epsBG": 2.5, #relative permittivity of polymer
	"useCoulomb": True, #whether to include e-e Coulomb interactions
	#--- Nano-particle parameters
	"epsNP": 10., #relative permittivity of nanoparticles
	"trapDepthNP": -1.1, #trap depth of nanoparticles in eV
	"radiusNP": 2.5, #radius of nanoparticles in nm
	"volFracNP": 0.02, #volume fraction of nanoparticles
	"nClusterMu": 30, #mean number of nanoparticles in each cluster (Gaussian distribution)
	"nClusterSigma": 5, #cluster size standard deviation in nm
	"clusterShape": "random",
	"shouldPlotNP": False #plot the electrostatic potential from PeriodicFD
}

## Execute the model
#mhmc = MinimaHoppingMC(params)

#nRuns = params["nRuns"]
#trajectory = np.concatenate(parallelMap(mhmc.run, cpu_count(), range(nRuns))) #Run in parallel and merge trajectories
#np.savetxt("trajectory.dat", trajectory, fmt="%d %e %d %d %d", header="iElectron t[s] ix iy iz") #Save trajectories together

## Analyze electron trajectory
import analyze
analyze.plotTrajectory("trajectory.dat")