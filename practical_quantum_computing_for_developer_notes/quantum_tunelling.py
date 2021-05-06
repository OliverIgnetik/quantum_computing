import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import nano, Planck, electron_mass, electron_volt

# transistor data from the book
transistor_dataframe = pd.DataFrame({'Year': [1995, 2001, 2010, 2014, 2019, 2021, 2025, 2030],
                                     'Size (nm)': [20, 10, 6, 7, 8, 5, 3, 0.5]})


def engel_prob(E=4.5, V=5, N=1):
    """
    Set ups the probability function for quantum tunneling with:
    Barrier potential in eV
    Kinetic energy in eV
    """
    def aux(trans_thickness):
        a = trans_thickness*nano
        probability_wave_function = np.exp(-4*a * (N / Planck) * np.sqrt(
            2*electron_mass*(V-E)*electron_volt))
        return probability_wave_function

    return aux


# go through different kinetic energies
Kinetic_energies = np.linspace(4.5, 4.99, 4)
list_probabilities = []
KE_labels = []

for KE in Kinetic_energies:
    probability_function = engel_prob(KE)
    probability_vector = probability_function(
        transistor_dataframe.iloc[:, 1].values)*100
    list_probabilities.append(probability_vector)
    KE_labels.append(str(round(KE, 2)) + ' eV')

# turn probabilities into dataframe
probabilities_dataframe = pd.DataFrame(
    list_probabilities).transpose()
probabilities_dataframe.columns = KE_labels

# Set up final data frame
data = pd.concat([transistor_dataframe, probabilities_dataframe], axis=1)
data.set_index('Size (nm)', inplace=True)

# plot
data.iloc[:, 1:].plot()
plt.xlabel('transistor size (nm)')
plt.ylabel('Probability of tunneling (%)')
plt.title('Nanoscale transistors and quantum tunneling')
plt.show()
