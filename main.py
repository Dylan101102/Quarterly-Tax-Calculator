# Simple program to calculate quarterly taxes for making deliveries as an independent contractor.
# By no means is this 100% perfect, but does do a decent job at least of estimating quarterly taxes.
# For example, income is not taxed at a single tax rate. For simplicity, it will be here. Lowering tax liability come April is the main goal here.
# This program also assumes the taxable income between the current and previous year do not differ too much, but again, this was done for simplicity.
# For testing purposes, will be using 2024 rates to test if it matches what I paid quarterly last year. Will eventually switch over to 2025 numbers.


def taxable_income(income, miles):
    """
    This function determines how much of your quarterly income is taxable.
    """
    deduction = miles * 0.67 # 2024 standard mileage rate.
    tax_income = round(income - deduction) # Tax software does a lot of rounding, so that is being done here.
    return tax_income    

quarterly_income = float(input("From your side jobs, how much did you make for the previous quarter? $"))
miles_driven = float(input("How many miles did you drive for the previous quarter? "))
quar_tax_income = taxable_income(quarterly_income, miles_driven)
# print(f"Your taxable income for the previous quarter is ${quar_tax_income}")

anticip_yearly_income = float(input("What was your taxable income last year? This will determine your tax rate: $"))
marital_status = input("To also determine your tax rate, you will need to input your filing status. Press 1 if you are 'Single'," 
                        " 2 if you are 'Married Filing Jointly', 3 if you are 'Married, Filing Separately', or 4 if you are 'Head of Household': ")

