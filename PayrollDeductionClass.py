class Payroll_Deduction:

    def __init__(self, description, date, charge_amount, employee_ID):
        self.description = description
        self.date = date
        self.charge_amount = charge_amount 
        self.employee_ID = employee_ID

    def setdescription(self, description):
        self.description = description

    def getdescription(self):
        return self.description

    def setdate(self, date):
        self.date = date

    def getdate(self):
        return self.date

    def setchargeamount(self, charge_amount):
        self.charge_amount = charge_amount

    def getchargeamount(self):
        return self.charge_amount

    def setemployeeid(self, employee_ID):
        self.employee_ID = employee_ID

    def getemployeeid(self):
        return self.employee_ID

    

    