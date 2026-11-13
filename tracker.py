"""Placement Readiness Tracker - IRP-II Assignment (CSE2596)."""

# Task 1: list of dictionaries, one per student
students = [
    {"name": "Aarav Sharma", "roll_no": 2301, "aptitude": 78, "verbal": 82, "coding": 90},
    {"name": "Diya Verma",   "roll_no": 2302, "aptitude": 55, "verbal": 62, "coding": 48},
    {"name": "Kabir Singh",  "roll_no": 2303, "aptitude": 35, "verbal": 40, "coding": 30},
    {"name": "Meera Nair",   "roll_no": 2304, "aptitude": 92, "verbal": 88, "coding": 95},
    {"name": "Rohan Gupta",  "roll_no": 2305, "aptitude": 60, "verbal": 45, "coding": 70},
]

if __name__ == "__main__":
    print(f"{len(students)} students loaded")
