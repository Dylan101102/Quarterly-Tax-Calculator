def taxable_income(income, miles):
    """
    This function determines how much of your quarterly income is taxable.
    """
    deduction = miles * 0.70 # 2025 standard mileage rate.
    tax_income = round(income - deduction) # Tax software does a lot of rounding, so that is being done here.
    return tax_income


def fed_tax_rate (yearly_income, status):
    """
    This function determines your tax rate.
    """
    match status:
        case "1": # Single status filer.
            if yearly_income <= 11925:
                tax_rate = 0.10
            elif yearly_income >= 11926 and yearly_income <= 48475:
                tax_rate = 0.12
            elif yearly_income >= 48476 and yearly_income <= 103350:
                tax_rate = 0.22
            elif yearly_income >= 103351 and yearly_income <= 197300:
                tax_rate = 0.24
            elif yearly_income >= 197301 and yearly_income <= 250525:
                tax_rate = 0.32
            elif yearly_income >= 250526 and yearly_income <= 626350:
                tax_rate = 0.35
            else:
                tax_rate = 0.37
        case "2": # Married Filing Jointly
            if yearly_income <= 23850:
                tax_rate = 0.10
            elif yearly_income >= 23851 and yearly_income <= 96950:
                tax_rate = 0.12
            elif yearly_income >= 96951 and yearly_income <= 206700:
                tax_rate = 0.22
            elif yearly_income >= 206701 and yearly_income <= 394600:
                tax_rate = 0.24
            elif yearly_income >= 394601 and yearly_income <= 501050:
                tax_rate = 0.32
            elif yearly_income >= 501051 and yearly_income <= 751600:
                tax_rate = 0.35
            else:
                tax_rate = 0.37
        case "3": # Married Filing Separately
            if yearly_income <= 11925:
                tax_rate = 0.10
            elif yearly_income >= 11926 and yearly_income <= 48475:
                tax_rate = 0.12
            elif yearly_income >= 48476 and yearly_income <= 103350:
                tax_rate = 0.22
            elif yearly_income >= 103351 and yearly_income <= 197300:
                tax_rate = 0.24
            elif yearly_income >= 197301 and yearly_income <= 250525:
                tax_rate = 0.32
            elif yearly_income >= 250526 and yearly_income <= 375800:
                tax_rate = 0.35
            else:
                tax_rate = 0.37
        case "4": # Head of Household
            if yearly_income <= 17000:
                tax_rate = 0.10
            elif yearly_income >= 17001 and yearly_income <= 64850:
                tax_rate = 0.12
            elif yearly_income >= 64851 and yearly_income <= 103350:
                tax_rate = 0.22
            elif yearly_income >= 103351 and yearly_income <= 197300:
                tax_rate = 0.24
            elif yearly_income >= 197301 and yearly_income <= 250500:
                tax_rate = 0.32
            elif yearly_income >= 250501 and yearly_income <= 626350:
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