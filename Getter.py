# Getter / Setter method
# Setter การกำหนดค่าให้ object
# Getter การดึงค่าจาก object

# Ex_Setter
# def setName(self, newname):
#   Self.__name = newname
# Ex_Getter
# def getName(self):
#   return self.__name

class Employee:
    def __init__(self, name, salary, department):
        # private attribute
        self.__name = name
        self.__salary = salary
        self.__department = department

        # private method

    def _showData(self):
        print('ชื่อพนักงาน = {}'.format(self.__name))
        print('เงินเดือน = {}'.format(self.__salary))
        print('แผนก = {}'.format(self.__department))

    # setter method
    def setName(self, newname):
        self.__name = newname

    def setSalary(self, newsalary):
        self.__salary = newsalary

    def setDepartment(self, newdepartment):
        self.__department = newdepartment


emp1 = Employee('รุ่งนภา', 50000, 'นักเรียน')
emp1.setName('นิลศรี')
emp1.setSalary(70000)
emp1.setDepartment('ศึกษา')
emp1._showData()