# Placement Readiness Tracker

Command-line tool (IRP-II, CSE2596, IILM University) that records students'
practice-test scores (aptitude, verbal, coding), computes averages and grades,
finds the top scorer and flags students who need extra practice.

## Files
- `tracker.py` - main program (Tasks 1 and 2)
- `runner_up.py` - second-highest distinct score (Task 3)

## How to run
```
python3 tracker.py        # enter one more student when prompted
python3 runner_up.py      # then: n on line 1, n scores on line 2
```
Requires Python 3.8+. No external libraries.

## Sample output
```
Roll  Name              Apt  Verb  Code     Avg  Grade
----------------------------------------------------------
2301  Aarav Sharma       78    82    90   83.33  A
2302  Diya Verma         55    62    48   55.00  C
2303  Kabir Singh        35    40    30   35.00  Needs practice
2304  Meera Nair         92    88    95   91.67  A
2305  Rohan Gupta        60    45    70   58.33  C
2306  Isha Patel         70    65    72   69.00  B

Top scorer: Meera Nair (average 91.67)
Students needing extra practice:
  - Kabir Singh (average 35.00)
```
