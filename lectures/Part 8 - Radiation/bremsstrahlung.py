import numpy as np
import matplotlib.pyplot as plt

e_charge = 1.602e-19  # elementary electron charge (C)
e_mass = 9.109e-31  # electron mass (kg)
c = 3e8  # speed of light (m/s)

initial_energy_keV = 100  # initial kinetic energy of the electron (keV)
initial_energy_J = initial_energy_keV * 1.602e-16  # convert to joules
num_photons = 100000  # number of photons to simulate

# generate photon energies based on a simplified bremsstrahlung spectrum
def bremsstrahlung_spectrum(energy_keV, num_samples):
    photon_energies = np.random.uniform(0, energy_keV, num_samples)  # uniform sampling
    intensity = 1 / photon_energies  # intensity inversely proportional to energy
    probabilities = intensity / np.sum(intensity)  # normalize to get probabilities
    return np.random.choice(photon_energies, size=num_samples, p=probabilities)

photon_energies_keV = bremsstrahlung_spectrum(initial_energy_keV, num_photons)

# generate spectrum histogram
spectrum, bins = np.histogram(photon_energies_keV, bins=50, range=(0, initial_energy_keV))
bin_centers = 0.5 * (bins[:-1] + bins[1:])

# plot spectrum
plt.figure(figsize=(8, 6))
plt.semilogy(bin_centers, spectrum, drawstyle='steps-mid')
plt.xlabel('Photon Energy (keV)')
plt.ylabel('Intensity (Dimensionless)')
plt.title('Bremsstrahlung X-ray Spectrum')
plt.grid()
plt.savefig("bremsstrahlung_spectrum.png", dpi=100)
plt.show()