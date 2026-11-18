# Placement Readiness Tracker

Student: Reyaan Malik
Roll number: 2481100

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

## Task 3 test cases

| Input | Expected output | Actual output |
| --- | ---: | ---: |
| `5` then `70 85 85 60 90` | `85` | `85` |
| `6` then `10 20 20 30 40 40` | `30` | `30` |
| `4` then `100 100 90 80` | `90` | `90` |

The third case repeats the top score, so it verifies that the runner-up is distinct.

## Task 5 analysis

The program begins in the new/ready state when the operating system creates its
process. It moves to the running state while Python executes the program and
then becomes blocked (waiting) whenever `input()` waits for keyboard data. After
the user supplies valid data, it returns to running, calculates the averages,
prints the table and finally exits; the operating system then releases its
resources. Invalid scores keep the process running while the validation loop
requests another value.

For 200 students, I would host a web version on a PaaS such as Azure App
Service. PaaS provides the runtime, deployment, scaling and monitoring without
requiring us to manage virtual machines or operating-system patches. The
application could expose a small Python web API and use managed storage for
student records. This is a better fit than IaaS for a small academic tool
because it reduces administration, while SaaS is unsuitable because we are
building and controlling the application ourselves.

## AI declaration

I used ChatGPT to help understand the assignment requirements, review the
Python implementation and prepare test cases and explanatory documentation.

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
