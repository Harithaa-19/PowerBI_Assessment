# Dictionary holding student records
student_info = {
    "ST101": {
        "sname": "Raj",
        "branch": "Computer Science",
        "subjects": {
            "Python101": {"mid": 88, "final": 92, "proj": 94},
            "Math201": {"mid": 78, "final": 85, "proj": 80}
        }
    },
    "ST102": {
        "sname": "Neha",
        "branch": "Mathematics",
        "subjects": {
            "Math201": {"mid": 90, "final": 93, "proj": 88},
            "Stats101": {"mid": 84, "final": 80, "proj": 85}
        }
    },
    "ST103": {
        "sname": "Asha",
        "branch": "Physics",
        "subjects": {
            "Physics101": {"mid": 75, "final": 82, "proj": 78},
            "Math201": {"mid": 70, "final": 72, "proj": 68}
        }
    }
}

# Q1: Print all student names and their branches
print("Student Names and Branches:")
for sid, data in student_info.items():
    print(f"{data['sname']} - {data['branch']}")

# Q2: Print average score per subject per student
print("\nAverage Score Per Subject Per Student:")
for sid, data in student_info.items():
    print(f"{data['sname']}:")
    for sub, marks in data['subjects'].items():
        avg = sum(marks.values()) / len(marks)
        print(f"  {sub}: {avg:.2f}")

# Q3: Find students who scored more than 90 in the final exam of Python101
print("\nStudents Scoring >90 in Python101 Final:")
for sid, data in student_info.items():
    py_data = data['subjects'].get("Python101")
    if py_data and py_data.get("final", 0) > 90:
        print(f"{data['sname']} scored {py_data['final']} in Python101 final")

# Q4: Add new subject AI101 for student ST101
print("\nAdding new subject AI101 for ST101")
student_info["ST101"]["subjects"]["AI101"] = {"mid": 85, "final": 90, "proj": 88}
print(f"Updated subjects for {student_info['ST101']['sname']}:")
print(student_info["ST101"]["subjects"])

# Q5: Calculate and print average score for each subject across all students
from collections import defaultdict

print("\nAverage Score for Each Subject Across All Students:")

# Dictionary to accumulate average scores per subject
subject_scores = defaultdict(list)

# Compute average per student and store in subject_scores
for data in student_info.values():
    for sub, marks in data["subjects"].items():
        avg_score = sum(marks.values()) / len(marks)
        subject_scores[sub].append(avg_score)

# Compute and display overall average per subject
for sub, scores in subject_scores.items():
    overall = sum(scores) / len(scores)
    print(f"{sub}: {overall:.2f}")
