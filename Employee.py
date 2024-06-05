class Employee:
    def __init__(self, id_number, department, job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title
    
    def set_name(self, val):
        self.name = val

    def set_id_number(self, val):
        self.id_number = val

    def set_department(self, val):
        self.department = val
    
    def set_job_title(self, val):
        self.job_title = val
    
    def __str__(self):
        return "Name: " + self.name + "\n" + "Department: " + self.department + "\n" + "Job Title: " + self.job_title + "\n"

emp_data = dict()
def Add():
    n = input("Name: ")
    i = input("ID Number: ")
    d = input("Department: ")
    j = input("Job Title: ")
    obj = Employee(n, i, d, j)

    if i in emp_data.keys():
        print("ID already exists")
    else:
        emp_data[i] = obj

def Look():
    i = input("ID Number: ")
    if i in emp_data.keys():
        print(emp_data[i])
    else:
        print("ID not found")

def Change():
    i = input("ID Number: ")
    if i in emp_data.keys():
        print("Enter Value to Update")
        n = input("Name: ")
        emp_data[i].set_name(n)
        d = input("Department: ")
        emp_data[i].set.department(d)
        j = input("Job Title: ")
        emp_data[i].set_job_title(j)
    else:
        print("ID not found")

def Del():
    i = input("ID Number: ")
    if i in emp_data.keys():
        del emp_data[i]

while True:
    print("\nEnter A to add a new employee\nEnter L to look up a new employee\nEnter C to change employee details\nEnter D to delete an employee\nEnter Q to quit\n")
    ch = input(":")
    if ch == 'a' or ch == 'A':
        Add()
        print()
    if ch == 'l' or ch == 'L':
        Look()
        print()
    if ch == 'c' or ch == 'C':
        Change()
        print()
    if ch == 'd' or ch == 'D':
        Del()
        print()
    if ch == 'q' or ch == 'Q':
        break