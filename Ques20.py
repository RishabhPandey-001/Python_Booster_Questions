# 20.	Salary Deduction: Calculate in-hand salary after HRA, DA, PF, and tax deductions.
basic_salary = float(input("Enter your Basic Salary: "))

# Enter percentages for HRA, DA, PF, and Tax
hra_percent = float(input("Enter HRA percentage: "))
da_percent = float(input("Enter DA percentage: "))
pf_percent = float(input("Enter PF percentage: "))
tax_percent = float(input("Enter Tax percentage: "))

hra_amount = (hra_percent / 100) * basic_salary
da_amount = (da_percent / 100) * basic_salary
pf_amount = (pf_percent / 100) * basic_salary
tax_amount = (tax_percent / 100) * basic_salary

gross_salary = basic_salary + hra_amount + da_amount
in_hand_salary = gross_salary - (pf_amount + tax_amount)

print("\n--- Salary Details ---")
print(f"Basic Salary: {basic_salary}")
print(f"HRA Amount: {hra_amount}")
print(f"DA Amount: {da_amount}")
print(f"PF Deduction: {pf_amount}")
print(f"Tax Deduction: {tax_amount}")
print(f"Gross Salary: {gross_salary}")
print(f"In-Hand Salary: {in_hand_salary}")