"""Task 3: print the second-highest distinct score (reads stdin)."""

import sys


data = list(map(int, sys.stdin.read().split()))
n = data[0]
scores = data[1:1 + n]

# A set removes duplicates; sorting then makes the second-highest value clear.
distinct_scores = sorted(set(scores))
print(distinct_scores[-2])
