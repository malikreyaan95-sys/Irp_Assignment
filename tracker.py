"""Placement Readiness Tracker - IRP-II Assignment (CSE2596)."""

# Task 1: list of dictionaries, one per student
students = [
    {"name": "Aarav Sharma", "roll_no": 2301, "aptitude": 78, "verbal": 82, "coding": 90},
    {"name": "Diya Verma",   "roll_no": 2302, "aptitude": 55, "verbal": 62, "coding": 48},
    {"name": "Kabir Singh",  "roll_no": 2303, "aptitude": 35, "verbal": 40, "coding": 30},
    {"name": "Meera Nair",   "roll_no": 2304, "aptitude": 92, "verbal": 88, "coding": 95},
    {"name": "Rohan Gupta",  "roll_no": 2305, "aptitude": 60, "verbal": 45, "coding": 70},
]

# Task 2: functions
def average(student):
    """Return the mean of the three scores."""
    return (student["aptitude"] + student["verbal"] + student["coding"]) / 3


def grade(avg):
    """Return the grade for an average mark."""
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    return "Needs practice"


def top_scorer(students):
    """Return the student with the highest average."""
    return max(students, key=average)


def needs_practice(students, limit=40):
    """Return the students whose average is below limit."""
    return [s for s in students if average(s) < limit]


def read_score(subject):
    """Keep asking until the user enters an integer between 0 and 100."""
    while True:
        text = input(f"Enter {subject} score (0-100): ")
        try:
            value = int(text)          # input() gives str, so convert
        except ValueError:
            print("  Please enter a whole number.")
            continue
        if 0 <= value <= 100:
            return value
        print("  Score must be between 0 and 100. Try again.")


def add_student():
    """Read one student from the keyboard and append to the list."""
    name = input("Enter student name: ").strip()
    roll_no = int(input("Enter roll number: "))
    student = {
        "name": name,
        "roll_no": roll_no,
        "aptitude": read_score("aptitude"),
        "verbal": read_score("verbal"),
        "coding": read_score("coding"),
    }
    students.append(student)


if __name__ == "__main__":
    add_student()
    print(f"{len(students)} students loaded")
