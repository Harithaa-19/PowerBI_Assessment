"""
Q). Create a class with name of dept which has id, name, loc, HOD through
the constructor initialize the department  attributes
create  a method to display the dept. info, display total dept in your organization.

-Get the input from the user no.of dept, create list/dict to store the no.of dept
-use for loop to get the dept information
-for every dept info u get, add that into list/dict,
-display all dept info in the list/dict
-search dept by dept_id, if it is there show details else  it is not available
-add a fun. to search for dept by dept_name
"""
class Dept:
    total = 0

    def __init__(self, did, dname, dloc, dhod):
        self.did = did
        self.dname = dname
        self.dloc = dloc
        self.dhod = dhod
        Dept.total += 1

    def show(self):
        print("\nDepartment Details:")
        print("--------------------")
        print(f"ID        : {self.did}")
        print(f"Name      : {self.dname}")
        print(f"Location  : {self.dloc}")
        print(f"HOD       : {self.dhod}")

    @classmethod
    def count(cls):
        print(f"Total Departments: {cls.total}")

dept_list = []
num = int(input("Enter number of departments: "))
for i in range(num):
    print(f"\nEnter details for department {i + 1}:")
    did = input("Department ID: ")
    dname = input("Department Name: ")
    dloc = input("Location: ")
    dhod = input("HOD Name: ")
    d = Dept(did, dname, dloc, dhod)
    dept_list.append(d)

for d in dept_list:
    d.show()

Dept.count()

search_id = input("\nSearch by Department ID: ")
found = False
for d in dept_list:
    if d.did == search_id:
        print("\nMatch Found:")
        d.show()
        found = True
        break
if not found:
    print("Department ID not found.")

search_name = input("\nSearch by Department Name: ")
found = False
for d in dept_list:
    if d.dname.lower() == search_name.lower():
        print("\nMatch Found:")
        d.show()
        found = True
if not found:
    print("Department name not found.")
