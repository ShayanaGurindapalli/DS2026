import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.special import comb

# 1. Define Binomial parameters
n = 10    # total number of trials
p = 0.5   # probability of success per trial

# 2. Generate possible outcomes (0 to n)
k = np.arange(0, n + 1)


# 3. Explicit mathematical formula calculation
pmf = comb(n, k) * (p**k) * ((1 - p)**(n - k))
cdf = np.cumsum(pmf)


# 3. Python Scipy functions for PMF and CDF
# pmf = binom.pmf(k, n, p)
# cdf = binom.cdf(k, n, p)

# 4. Plot PMF
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.bar(k, pmf, color='skyblue', edgecolor='black')
plt.title('Binomial PMF')
plt.xlabel('Number of Successes (k)')
plt.ylabel('Probability P(X = k)')

# 5. Plot CDF
plt.subplot(1, 2, 2)
plt.step(k, cdf, color='red', where='post', marker='o')
plt.title('Binomial CDF')
plt.xlabel('Number of Successes (k)')
plt.ylabel('Cumulative Probability P(X <= k)')

plt.tight_layout()
plt.show()