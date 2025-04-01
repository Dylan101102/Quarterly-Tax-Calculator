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