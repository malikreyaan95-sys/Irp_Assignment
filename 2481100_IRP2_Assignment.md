# IRP-II Assignment Submission

**Student:** Reyaan Malik  
**Roll number:** 2481100  
**Repository:** Placement Readiness Tracker

## Included work

- `tracker.py` implements Tasks 1 and 2: student dictionaries, validated input,
  averages, grades, top scorer and students needing practice.
- `runner_up.py` implements Task 3 and prints the second-highest distinct score.
- `README.md` contains the run instructions, sample output, test-case table and
  Task 5 analysis.

## Task 3 test-case results

| Input | Expected output | Actual output |
| --- | ---: | ---: |
| `5` / `70 85 85 60 90` | `85` | `85` |
| `6` / `10 20 20 30 40 40` | `30` | `30` |
| `4` / `100 100 90 80` | `90` | `90` |

The final case repeats the highest score and confirms that the runner-up is
distinct.

## Task 5 answers

The process starts in the new/ready state, enters running while Python executes,
and enters the blocked or waiting state while `input()` waits for keyboard data.
After valid input it returns to running, prints the results and exits. Invalid
input is handled by the validation loop, which keeps the process running until
valid data is entered.

For 200 users, PaaS is the best choice. A service such as Azure App Service can
run a Python web application while managing the operating system, runtime
patches, deployment, scaling and monitoring. IaaS would require more server
administration, and SaaS would not fit because the placement cell is developing
its own application.

## Git submission

The repository contains more than five meaningful commits and a merged
`feature-grades` branch. Run `git log --oneline --decorate --all` to display the
history.

## AI declaration

I used ChatGPT to understand the assignment requirements, review the Python
implementation, prepare test cases and draft explanatory documentation.
