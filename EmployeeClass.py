class Employee:
    
    def __init__(self, name, id_number, department, job_title, monthly_salary):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title
        self.monthly_salary = monthly_salary

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setIdNumber(self, id_number):
        self.id_number = id_number

    def getIdNumber(self):
        return self.id_number

    def setDepartment(self, department):
        self.department = department

    def getDepartment(self):
        return self.department

    def setJobTitle(self, job_title):
        self.job_title = job_title

    def getJobTitle(self):
        return self.job_title

    def setMonthlySalary(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def getMonthlySalary(self):
        return self.monthly_salary
