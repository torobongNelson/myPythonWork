Employee_name = (input("Enter employee's name :"))

Number_of_hours_worked_in_a_week = int(input("Number of hours : "))

Hourly_pay_rate = float(input("Enter your hourly pay rate: "))

Month = input("Enter the month: ")

Federal_tax_withholding_rate = float(input("Enter federal tax rate :"))

State_tax_withholding_rate = float(input("Enter state :"))


Gross_Pay = Number_of_hours_worked_in_a_week * Hourly_pay_rate
federal_deduction = 20/100 * Gross_Pay
state_deduction = 9/100 * Gross_Pay

Total_deduction = federal_deduction + state_deduction

Net_pay = Gross_Pay - Total_deduction

print(Employee_name, "Payroll statement for the month", Month)
print(" ")
print("Employee Name:",Employee_name)
print("Hours worked:",Hourly_pay_rate)
print("Pay rate:", "$", Hourly_pay_rate)
print("Gross pay:", "$", Gross_Pay)
print("Deductions:")
print("federal withholding:","(20.0%)", federal_deduction)
print("State Deduction:", state_deduction)
print("Total Deduction:", "$", Total_deduction)

print("Net pay:", "$", Net_pay)
