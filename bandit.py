import numpy as np
import matplotlib.pyplot as plt

def kBandit(k, epsilon, steps, stepSizeFN):
    rewardDistributions = list(map(lambda x : 0, range(k)))
    rewardEstimates = list(map(lambda x : 0, rewardDistributions));
    rewardN = list(map(lambda x : 0, rewardDistributions));
    rewardHistory = [ ]

    for i in range(steps):
        explore = np.random.binomial(1, epsilon) == 1
        kIndex = -1

        if explore:
            kIndex = np.random.randint(0, k)
        else:
            maxEstimates = [ ]

            for i, reward in enumerate(rewardEstimates):
                if not len(maxEstimates):
                    maxEstimates.append(i)
                elif reward > rewardEstimates[maxEstimates[0]]:
                    maxEstimates.clear()
                    maxEstimates.append(i)
                elif reward == rewardEstimates[maxEstimates[0]]:
                    maxEstimates.append(i)

            kIndex = maxEstimates[np.random.randint(0, len(maxEstimates))]

        reward = np.random.normal(rewardDistributions[kIndex], 1)
        rewardN[kIndex] += 1
        rewardEstimates[kIndex] = rewardEstimates[kIndex] + stepSizeFN(rewardN[kIndex]) * (reward - rewardEstimates[kIndex]);

        if not len(rewardHistory):
            rewardHistory.append(reward)
        else:
            rewardHistory.append(rewardHistory[-1] + (1 / (len(rewardHistory) + 1)) * (reward - rewardHistory[-1]))

        for i in range(k):
            if np.random.binomial(1, 0.2) == 1:
                rewardDistributions[i]  = np.random.normal(0, 2)

    return rewardHistory

def performBanditN(n, k, epsilon, steps, stepSizeFN):
    results = [ kBandit(k, epsilon, steps, stepSizeFN) for i in range(n) ]
    averaged_results = [ ]

    for i in range(steps):
        sum = 0

        for j in range(n):
            sum += results[j][i]

        averaged_results.append(sum / 1000)

    return averaged_results

results1 = performBanditN(2000, 10, 0.1, 1000, lambda n : 1 / n)
results2 = performBanditN(2000, 10, 0.1, 1000, lambda n : .1)

x = range(1, len(results1) + 1)
plt.plot(x, results1, 'r')
plt.plot(x, results2, 'g')
plt.show()
