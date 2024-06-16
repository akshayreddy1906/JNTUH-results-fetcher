import requests
from tabulate import tabulate

def main():
    htNo = input("Enter Hallticket Number:  ")
    url = 'https://jntuhresults.up.railway.app/api/academicresult?htno='+ htNo
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        print(data["Details"]["NAME"])
        while True:
            user_choice = input("Enter 1 to display total GPA, 2 to display semester details, or 3 to display semester CGPA and credits or E to end loop: ")
            if user_choice == '1':
                print(display_total_gpa(data))
            elif user_choice == '2':
                print(display_semester_details(data))
            elif user_choice == '3':
                print(display_cgpa_credits(data))
            elif user_choice.lower() == 'e' :
                break
            else:
                print("Invalid choice. Please try again.")
    elif r.status_code == 500:
        print("500 - Internal Server Error")
    else:
        print("Failed to retrieve data")

def display_total_gpa(data):
    total_gpa = data["Results"]["Total"]
    return f"Total GPA: {total_gpa}"

def display_semester_details(data):
    while True:
        semester_input = input("Enter the semesters (e.g.1-1 1-2) separated by space or ALL for all semesters : ")
        if semester_input.lower() == "all" :
            semester_input = " 1-1 1-2 2-1 2-2 3-1 3-2 4-1 4-2"
        semesters = [sem.strip() for sem in semester_input.split(' ')]
        valid_semesters = [sem for sem in semesters if sem in data["Results"]]
        if valid_semesters:
            rows = []
            for semester in valid_semesters:
                subjects = data['Results'][semester]
                headers = ['Semester','Subject Code', 'Subject Name', 'Internal Marks', 'External Marks', 'Total Marks', 'Grade', 'Credits']
                for subject_code, details in subjects.items():
                    if isinstance(details, dict):
                        rows.append([
                            semester,
                            subject_code,
                            details.get('subject_name', ''),
                            str(details.get('subject_internal', '')),
                            str(details.get('subject_external', '')),
                            str(details.get('subject_total', '')),
                            details.get('subject_grade', ''),
                            details.get('subject_credits', '')
                        ])
            return tabulate(rows, headers=headers)
        else:
            print("Invalid semester. Please try again.")

def display_cgpa_credits(data):
    while True:
        semester_input = input("Enter the semesters (e.g.1-1 1-2) separated by space or ALL for all semesters : ")
        if semester_input.lower() == "all" :
            semester_input = " 1-1 1-2 2-1 2-2 3-1 3-2 4-1 4-2"
        semesters = [sem.strip() for sem in semester_input.split(' ')]
        valid_semesters = [sem for sem in semesters if sem in data["Results"]]
        if valid_semesters:
            results = []
            for semester in valid_semesters:
                credit = data["Results"][semester]["credits"]
                sem_CGPA = data["Results"][semester]["CGPA"]
                results.append([semester, credit ,sem_CGPA])
            return tabulate(results, headers= ['Semester','credits','CGPA'])
        else:
            print("No valid semesters entered. Please try again.")

if __name__ == "__main__":
    main()
