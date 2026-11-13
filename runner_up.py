"""Task 3: print the second-highest distinct score (reads stdin)."""

n = int(input())
scores = set(map(int, input().split()))   # set removes duplicates
scores.discard(max(scores))               # drop the highest distinct score
print(max(scores))                        # next highest is the runner-up
