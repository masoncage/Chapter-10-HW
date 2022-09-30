import EmployeeClass as ec 

import PayrollDeductionClass as pd

def main():
    employee = ec.Employee('Jimmy Smith', 58475, 'Information Systems', 'Developer', 6800.00)
    
    
    t1 = pd.Payroll_Deduction('food court', '8/14/2022', 22.5, 39119)
    t2 = pd.Payroll_Deduction('gift contribution', '8/12/2022', 25.00, 58475)
    t3 = pd.Payroll_Deduction('food court', '8/17/2022', 15.25, 21547)
    t4 = pd.Payroll_Deduction('vending machine', '8/22/2022', 3.00, 58475)
    t5 = pd.Payroll_Deduction('vending machine', '8/5/2022', 2.75, 58475)

    print('*** Employee Pay ***')
    print('Name: ', employee.name)
    print('ID Number: ', employee.id_number)
    print('Department: ', employee.department)
    print('Job Title: ', employee.job_title)

    for transaction in pd.Payroll_Deduction:
        if pd.employee_ID == 48475:
         ec.monthly_salary - pd.charge_amount

    print('Monthly Salary: ', employee.get_monthly_salary)

main()