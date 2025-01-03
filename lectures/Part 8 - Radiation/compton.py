# repeated compton scattering of photons within a semi-infite homogeneous slab medium

import math
from rng import MCG

rng = MCG() # custom random number generator

e_rest_energy = 511.0 # keV: rest mass energy of electron
E_min = 1.0 # keV: threshold below which a photon is considered absorbed
E0 = 100 # keV: initial energy of photon
N_photons = 10000 # number of incident photons / histories to simulate
T = 30.0 # thickness of slab in number of mean free paths
mfp = 1.0 # mean free path of photons in arbitrary length units
num_scatters_cutoff = 1000 # stop history if number of scattering events reaches this

results = {
	"BACK": 0, # number of photons back-scattered out of slab
	"TRANS": 0, # number of photons transmitted through slab
	"ABS": 0, # number of photons absorbed in slab
	"MAXSCAT": 0 # highest number of scattering events in a single history
}

def sample_scatter_angle():
	# assume isotropic (equal probability of scatter in all directions)
	# this is not physically accurate; see Klein-Nishina differential cross-sections
	return rng.sample(-math.pi, math.pi) # 0 radians = incident angle

def sample_distance():
	# distance traveled between scattering events in number of mfps
	return -mfp * math.log(rng.sample(0, 1))

def compton_energy(E_in, dtheta):
	# energy of scattered photon emerging from a compton event
	alpha = E_in / e_rest_energy # dimensionless ratio
	denominator = 1.0 + alpha * (1.0 - math.cos(dtheta))
	# avoid division by zero
	if abs(denominator) < 1.0e-12:
		return 0.0 # effectively a large energy loss
	return E_in / denominator

if __name__ == '__main__':
	for i in range(N_photons):
		x = 0.0 # position of photon
		theta = 0.0 # initial incident angle of photon onto slab
		E = E0 # photon energy
		
		num_scatters = 0
		while E > E_min and num_scatters < num_scatters_cutoff:
			distance = sample_distance()
			x += distance * math.cos(theta) # may be negative if pi/2 < theta < 3pi/2
			dtheta = sample_scatter_angle()
			theta += dtheta
			if x < 0.0:
				# back-scattered through anterior wall
				results["BACK"] += 1
				break
			elif x > T:
				# transmitted through posterior wall
				results["TRANS"] += 1
				break
			else:
				# scattered in medium
				num_scatters += 1
				if num_scatters > results["MAXSCAT"]:
					results["MAXSCAT"] = num_scatters
				# energy of new photon
				E = compton_energy(E, dtheta)
				if E <= E_min:
					results["ABS"] += 1
					break

	num_abs = results["ABS"]
	num_back = results["BACK"]
	num_trans = results["TRANS"]
	max_scat = results["MAXSCAT"]

	print(f"Fraction of photons absorbed in slab: {round(num_abs / N_photons, 5)}")
	print(f"Fraction of photons back-scattered out of slab: {round(num_back / N_photons, 5)}")
	print(f"Fraction of photons transmitted through slab: {round(num_trans / N_photons, 5)}")
	print(f"Highest number of scatter events inside slab: {max_scat}")