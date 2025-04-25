tax_brackets = {
    "Single or married filing separately": [
        (0, 10412, 0.01),
        (10413, 24684, 0.02),
        (24685, 38959, 0.04),
        (38960, 54081, 0.06),
        (54082, 68350, 0.08),
        (68351, 349137, 0.093),
        (349138, 418961, 0.103),
        (418962, 698271, 0.113),
        (698272, float('inf'), 0.123)
    ],
    "Married filing jointly or surviving spouse": [
        (0, 20824, 0.01),
        (20825, 49368, 0.02),
        (49369, 77918, 0.04),
        (77919, 108162, 0.06),
        (108163, 136700, 0.08),
        (136701, 698274, 0.093),
        (698275, 837922, 0.103),
        (837923, 1396542, 0.113),
        (1369543, float('inf'), 0.123)
    ],
    "Head of household": [
        (0, 20839, 0.01),
        (20840, 49371, 0.02),
        (49372, 63644, 0.04),
        (63645, 78765, 0.06),
        (78766, 93037, 0.08),
        (93038, 474824, 0.093),
        (474825, 569790, 0.103),
        (569791, 949649, 0.113),
        (949650, float('inf'), 0.123)
    ]
}

def calculate_tax(income, status):
    if status not in tax_brackets:
        raise ValueError("Invalid status. Choose from 'Single or married filing separately', 'Married filing jointly or surviving spouse', 'Head of household'.")

    brackets = tax_brackets[status]
    tax = 0

    for lower, upper, rate in brackets:
        if income > lower:
            taxable_income = min(upper, income) - lower
            tax += taxable_income * rate
        if income <= upper:
            break

    return round(tax, 2)

if __name__ == "__main__":
    personal_income = 201760
    status = "Single or married filing separately"
    print(calculate_tax(201760, status=status))