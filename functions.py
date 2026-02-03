def taxable_income(income, miles):
    """
    This function determines how much of your quarterly income is taxable.
    """
    deduction = miles * 0.725 # 2026 standard mileage rate.
    tax_income = round(income - deduction) # Tax software does a lot of rounding, so that is being done here.
    return tax_income


def fed_tax_rate (yearly_income, status):
    """
    This function determines your tax rate.
    """
    match status:
        case "1": # Single status filer.
            if yearly_income <= 12400:
                tax_rate = 0.10
            elif yearly_income >= 12401 and yearly_income <= 50400:
                tax_rate = 0.12
            elif yearly_income >= 50401 and yearly_income <= 105700:
                tax_rate = 0.22
            elif yearly_income >= 105701 and yearly_income <= 201775:
                tax_rate = 0.24
            elif yearly_income >= 201776 and yearly_income <= 256225:
                tax_rate = 0.32
            elif yearly_income >= 256226 and yearly_income <= 640600:
                tax_rate = 0.35
            else:
                tax_rate = 0.37
        case "2": # Married Filing Jointly
            if yearly_income <= 24800:
                tax_rate = 0.10
            elif yearly_income >= 24801 and yearly_income <= 100800:
                tax_rate = 0.12
            elif yearly_income >= 100801 and yearly_income <= 211400:
                tax_rate = 0.22
            elif yearly_income >= 211401 and yearly_income <= 403550:
                tax_rate = 0.24
            elif yearly_income >= 403551 and yearly_income <= 512450:
                tax_rate = 0.32
            elif yearly_income >= 512451 and yearly_income <= 768700:
                tax_rate = 0.35
            else:
                tax_rate = 0.37
        case "3": # Married Filing Separately
            if yearly_income <= 12400:
                tax_rate = 0.10
            elif yearly_income >= 12401 and yearly_income <= 50400:
                tax_rate = 0.12
            elif yearly_income >= 50401 and yearly_income <= 105700:
                tax_rate = 0.22
            elif yearly_income >= 105701 and yearly_income <= 201775:
                tax_rate = 0.24
            elif yearly_income >= 201776 and yearly_income <= 256225:
                tax_rate = 0.32
            elif yearly_income >= 256226 and yearly_income <= 384350:
                tax_rate = 0.35
            else:
                tax_rate = 0.37
        case "4": # Head of Household
            if yearly_income <= 17700:
                tax_rate = 0.10
            elif yearly_income >= 17701 and yearly_income <= 67450:
                tax_rate = 0.12
            elif yearly_income >= 67451 and yearly_income <= 105700:
                tax_rate = 0.22
            elif yearly_income >= 105701 and yearly_income <= 201750:
                tax_rate = 0.24
            elif yearly_income >= 201751 and yearly_income <= 256200:
                tax_rate = 0.32
            elif yearly_income >= 256201 and yearly_income <= 640600:
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