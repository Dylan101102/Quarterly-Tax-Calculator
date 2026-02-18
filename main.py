# Simple program to calculate quarterly taxes for making deliveries as an independent contractor.
# By no means is this 100% perfect, but does do a decent job at least of estimating quarterly taxes.
# For example, income is not taxed at a single tax rate. For simplicity, it will be here. Lowering tax liability come April is the main goal here.
# This program also assumes the taxable income between the current and previous year do not differ too much, but again, this was done for simplicity.
# This program also assumes you live in a state with no state income tax, like Florida.

import functions

quarterly_income = float(input("From your side jobs, how much did you make for the previous quarter? $"))
tips = float(input("Of that amount, how much was from tips? $"))
tips = float(input("Of that amount, how much was from tips? $"))
miles_driven = float(input("How many miles did you drive for the previous quarter? "))
quar_tax_income = functions.taxable_income(quarterly_income, tips, miles_driven)
quar_tax_income = functions.taxable_income(quarterly_income, tips, miles_driven)

previous_year_taxable_income = 30544 #2025 taxable income.
marital_status = input("To also determine your tax rate, you will need to input your filing status. Press 1 if you are 'Single'," 
                        " 2 if you are 'Married Filing Jointly', \n3 if you are 'Married, Filing Separately', or 4 if you are 'Head of Household': ")
tax_rate = functions.fed_tax_rate(previous_year_taxable_income, marital_status)
irs_payment = functions.pay_irs(tax_rate, quar_tax_income)
print(f"Please owe the IRS ${irs_payment}.")