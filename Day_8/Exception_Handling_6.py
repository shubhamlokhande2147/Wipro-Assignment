class Project:
    def __init__(self, employee_list):
        self.__employee_list = employee_list

    def validate_employee(self, employee_id):
        try:
            if employee_id not in self.__employee_list:
                raise Exception
                print("1")
        except Exception:
            print("2")

project1 = Project([1001, 1002, 1003])
project1.validate_employee(1005)
print("3")
