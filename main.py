# Simple program to calculate quarterly taxes for making deliveries as an independent contractor.
# By no means is this 100% perfect, but does do a decent job at least of estimating quarterly taxes.
# For example, income is not taxed at a single tax rate. For simplicity, it will be here. Lowering tax liability come April is the main goal here.
# This program also assumes the taxable income between the current and previous year do not differ too much, but again, this was done for simplicity.
# For testing purposes, will be using 2024 rates to test if it matches what I paid quarterly last year. Will eventually switch over to 2025 numbers.
# This program also assumes you live in a state with no state income tax, like Florida.


def taxable_income(income, miles):
    """
    This function determines how much of your quarterly income is taxable.
    """
    deduction = miles * 0.67 # 2024 standard mileage rate.
    tax_income = round(income - deduction) # Tax software does a lot of rounding, so that is being done here.
    return tax_income
    

def fed_tax_rate (yearly_income, status):
    """
    This function determines your tax rate.
    """
    match status:
        case "1": # Single status filer.
            if yearly_income <= 11600:
                tax_rate = 0.10
            elif yearly_income >= 11601 and yearly_income <= 47150:
                tax_rate = 0.12
            elif yearly_income >= 47151 and yearly_income <= 100525:
                tax_rate = 0.22
            elif yearly_income >= 100526 and yearly_income <= 191950:
                tax_rate = 0.24
            elif yearly_income >= 191951 and yearly_income <= 243725:
                tax_rate = 0.32
            elif yearly_income >= 243726 and yearly_income <= 609350:
                tax_rate = 0.35
            else:
                tax_rate = 0.37
        case "2": # Married Filing Jointly
            if yearly_income <= 23200:
                tax_rate = 0.10
            elif yearly_income >= 23201 and yearly_income <= 94300:
                tax_rate = 0.12
            elif yearly_income >= 94301 and yearly_income <= 201050:
                tax_rate = 0.22
            elif yearly_income >= 201051 and yearly_income <= 383900:
                tax_rate = 0.24
            elif yearly_income >= 383901 and yearly_income <= 487450:
                tax_rate = 0.32
            elif yearly_income >= 487451 and yearly_income <= 731200:
                tax_rate = 0.35
            else:
                tax_rate = 0.37
        case "3": # Married Filing Separately
            if yearly_income <= 11600:
                tax_rate = 0.10
            elif yearly_income >= 11601 and yearly_income <= 47150:
                tax_rate = 0.12
            elif yearly_income >= 47151 and yearly_income <= 100525:
                tax_rate = 0.22
            elif yearly_income >= 100526 and yearly_income <= 191950:
                tax_rate = 0.24
            elif yearly_income >= 191951 and yearly_income <= 243725:
                tax_rate = 0.32
            elif yearly_income >= 243726 and yearly_income <= 365600:
                tax_rate = 0.35
            else:
                tax_rate = 0.37
        case "4": # Head of Household
            if yearly_income <= 16550:
                tax_rate = 0.10
            elif yearly_income >= 16551 and yearly_income <= 63100:
                tax_rate = 0.12
            elif yearly_income >= 63101 and yearly_income <= 100500:
                tax_rate = 0.22
            elif yearly_income >= 100501 and yearly_income <= 191950:
                tax_rate = 0.24
            elif yearly_income >= 191951 and yearly_income <= 243700:
                tax_rate = 0.32
            elif yearly_income >= 243701 and yearly_income <= 609350:
                tax_rate = 0.35
            else:
                tax_rate = 0.37
    return tax_rate


def pay_irs(rate, quarterly_income):
    """
    This function determines how much you will pay to the IRS quarterly with the given information.
    """
    fed_income_tax = rate * quarterly_income
    self_employment_tax = (quarterly_income * 0.9235) * 0.153
    total_taxes = fed_income_tax + self_employment_tax
    return round(total_taxes)


quarterly_income = float(input("From your side jobs, how much did you make for the previous quarter? $"))
miles_driven = float(input("How many miles did you drive for the previous quarter? "))
quar_tax_income = taxable_income(quarterly_income, miles_driven)
# print(f"Your taxable income for the previous quarter is ${quar_tax_income}")

anticip_yearly_income = float(input("What was your taxable income last year? This will determine your tax rate: $"))
marital_status = input("To also determine your tax rate, you will need to input your filing status. Press 1 if you are 'Single'," 
                        " 2 if you are 'Married Filing Jointly', \n3 if you are 'Married, Filing Separately', or 4 if you are 'Head of Household': ")
tax_rate = fed_tax_rate(anticip_yearly_income, marital_status)
irs_payment = pay_irs(tax_rate, quar_tax_income)
print(f"Please owe the IRS ${irs_payment}.")