import numpy as np
from NEAT import NEAT

DinoShape = np.array([60, 40] * PopulationSize)
DinoScore = np.array([0] * PopulationSize)
HighScore = 0

DinoAlive = np.array([True] * PopulationSize, dtype=bool)

InToHid1 = NEAT(4, 6, MutationRate=0.1, PopulationSize=1000)
Hid1ToOut = NEAT(6, 3, MutationRate=0.1, PopulationSize=1000)

for Generation in range(100):
  while np.sum(DinoAlive) != 0:
    # Hi

  HighScore = np.max(np.array(DinoScore + [HighScore]))
  DinoAlive = np.array([True] * PopulationSize, dtype=bool)
  DinoScore = np.array([0] * PopulationSize)
  DinoShape = np.array([60, 40] * PopulationSize)