def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def assign_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def find_subject_toppers(students_dict):
    subject_toppers = {}
    for student, marks in students_dict.items():
        for subject, score in marks.items():
            if subject not in subject_toppers or score > subject_toppers[subject][1]:
                subject_toppers[subject] = (student, score)
    return subject_toppers

def display_student_report(student_name, marks_dict):
    average = calculate_average(marks_dict)
    grade = assign_grade(average)
    print(f"\nReport for {student_name}:")
    print(f"Subjects and Marks: {marks_dict}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")

def students_above_90(students_dict):
    high_scorers = set()
    for student, marks in students_dict.items():
        for score in marks.values():
            if score > 90:
                high_scorers.add(student)
                break
    return high_scorers

def store_as_tuples(students_dict):
    tuple_data = []
    for student, marks in students_dict.items():
        for subject, score in marks.items():
            tuple_data.append((student, subject, score))
    return tuple_data

def rank_students_by_total(students_dict):
    return sorted(students_dict.items(), key=lambda item: sum(item[1].values()), reverse=True)

def generate_subject_avg(students_dict):
    subject_totals = {}
    subject_counts = {}
    for marks in students_dict.values():
        for subject, score in marks.items():
            subject_totals[subject] = subject_totals.get(subject, 0) + score
            subject_counts[subject] = subject_counts.get(subject, 0) + 1
    return {subject: subject_totals[subject] / subject_counts[subject] for subject in subject_totals}


students = {}


num_students = int(input("Enter number of students: "))
for _ in range(num_students):
    name = input("\nEnter student name: ")
    marks = {}
    for subject in ['Math', 'English', 'Science']:
        marks[subject] = int(input(f"Enter marks for {subject}: "))
    students[name] = marks


for name, marks in students.items():
    display_student_report(name, marks)


print("\nSubject-wise Toppers:")
toppers = find_subject_toppers(students)
for subject, (student, score) in toppers.items():
    print(f"{subject}: {student} ({score})")


print("\nStudents scoring above 90 in any subject:")
print(students_above_90(students))


print("\nImmutable Tuple Records:")
for record in store_as_tuples(students):
    print(record)


print("\nRanking Students by Total Score:")
ranked = rank_students_by_total(students)
for i, (name, marks) in enumerate(ranked, 1):
    print(f"{i}. {name} - Total: {sum(marks.values())}")

print("\nSubject-wise Class Average:")
averages = generate_subject_avg(students)
for subject, avg in averages.items():
    print(f"{subject}: {avg:.2f}")
