def get_employee_department(employee_dict, employee_id):
    """
    Returns the department of the employee with the given employee_id.
    If the employee_id does not exist in the dictionary, return 'Unknown'.
    """


employees = {
    101: 'Sales',
    102: 'Engineering',
    103: 'Marketing',
    104: 'HR'
}


department_1 = get_employee_department(employees, 101)
print(department_1)  # 'Sales' expected

department_3 = get_employee_department(employees, 103)
print(department_3)  # 'Marketing' expected

department_4 = get_employee_department(employees, 104)
print(department_4)  # 'HR' expected

department_4 = get_employee_department(employees, 144)
print(department_4)  # KeyError expected


"""
To complete this exercise:
--------------------------
No any implementation notes.


Exercise Breakdown:
-------------------
The keys in a dictionary must be unique, while the values can be of any data type.

To access a value in a dictionary, you use the key:
department = mydict[some_key]

If the key does not exist in the dictionary, a KeyError is thrown.
"""
