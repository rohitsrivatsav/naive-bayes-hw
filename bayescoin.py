import random
from scipy.stats import bernoulli


class BayesCoin:
    # ------------------------------------------------------------ #
    def __init__(self):
        self.coins = [0, 1, 2]
        self.biases = [0.30, 0.45, 0.75]
        self.likelihood = {c: b for c, b in zip(self.coins, self.biases)}
        self.priors = {c: 1 / 3 for c in self.coins}
    # ------------------------------------------------------------ #

    def choose_coin(self):
        self.coin = random.choice(self.coins)
    # ------------------------------------------------------------ #

    def flip_coin(self):
        return bernoulli(self.likelihood[self.coin]).rvs(1)[0]
    # ------------------------------------------------------------ #

    def update_priors(self, flip):
        evidence = [abs((not flip) - self.likelihood[c]) * self.priors[c] for c in self.coins]
        self.priors = {i: e / sum(evidence) for i, e in enumerate(evidence)}
    # ------------------------------------------------------------ #
