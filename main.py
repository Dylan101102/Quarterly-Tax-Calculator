# Simple program to calculate quarterly taxes.

def tax_rate(status, income):
    match status:
        case "1": # Single status filer
            if income <= 11925: # 10% tax rate
                tax_rate = 0.10 * income
            elif income >= 11926 and income <= 48475: # 12%  tax rate
                tax_rate = 0.12 * income + 1192.50
            elif income >= 48476 and income <= 103350: # 22% tax rate
                tax_rate = 0.22 * income + 5578.50
            elif income >= 103351 and income <= 197300: # 24% tax rate
                tax_rate = 0.24 * income + 17651
            elif income >= 197301 and income <= 250525: # 32% tax rate
                tax_rate = 0.32 * income + 40199
            elif income >= 250526 and income <= 626350: # 35% tax rate
                tax_rate = 0.35 * income + 57231
            else: # 37% tax rate
                tax_rate = 0.37 * income + 188769.75
            return tax_rate 








# First, figure out the tax bracket.
filing_status = input("What is your filing status? Press 1 for 'Single', 2 for 'Married Filing Jointly', 3 for 'Married Filing Separately, or 4 for 'Head of Household': ")
taxable_income = float(input("Please enter your taxable income for the quarter: $"))
percent_tax_rate = tax_rate(filing_status, taxable_income)
print(f"Your tax rate is {percent_tax_rate * 100}%.")