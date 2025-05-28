'''
Build a student grade management system using the following Python concepts:
- List of dictionaries
- Function with required arguments, *args, **kwargs
- Function decorator
- Loops and control statements

Requirements
1. Use a **decorator** to log function activity.
2. Use a function to **add student data** using `*args` and `**kwargs`.
3. Store student records in a **list of dictionaries**.
4. Use **loops and conditionals** to calculate and display results.
'''

import datetime

def log_action(fn):
    def inner(*args, **kwargs):
        print(f"[{datetime.datetime.now()}] Executing: {fn.__name__}")
        result = fn(*args, **kwargs)
        print(f"[{datetime.datetime.now()}] Finished: {fn.__name__}\n")
        return result
    return inner

student_list = []

@log_action
def register_student(fullname, sid, *scores, **details):
    record = {
        "fullname": fullname,
        "sid": sid,
        "scores": scores,
        "details": details
    }
    student_list.append(record)

@log_action
def show_results():
    for rec in student_list:
        name = rec["fullname"]
        sid = rec["sid"]
        scores = rec["scores"]
        total_score = sum(scores)
        avg_score = total_score / len(scores) if scores else 0

        if avg_score >= 90:
            grade = "A+"
        elif avg_score >= 75:
            grade = "A"
        elif avg_score >= 60:
            grade = "B"
        elif avg_score >= 50:
            grade = "C"
        else:
            grade = "F"

        print(f"Student: {name} | ID: {sid}")
        print(f"Scores: {scores} | Total: {total_score} | Average: {avg_score:.2f} | Grade: {grade}")
        if rec["details"]:
            print("Other Details:", rec["details"])
        print("-" * 50)

register_student("Priya", 201, 91, 87, 93, city="Hyderabad", age=19)
register_student("Arya", 202, 74, 69, 78)
register_student("Latha", 203, 52, 49, 55, city="Pune", age=20)

show_results()
