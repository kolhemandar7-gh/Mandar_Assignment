# Generate 20 random nums (1-100), use sets for uniques, dict for frequency, print most common with conditional.

import random
from collections import Counter

nums = [random.randint(1,100) for _ in range(20)]
freq = Counter(nums)

most_common = [n for n, c in freq.items() if c == max(freq.values()) and c > 1]

print("Number:", nums)
print("Most common :", most_common if most_common else "None")