federal_tax_brackets = {
    "Single": [
        (0, 11600, 0.10),
        (11601, 47150, 0.12),
        (47151, 100525, 0.22),
        (100526, 191950, 0.24),
        (191951, 243725, 0.32),
        (243726, 609350, 0.35),
        (609351, float('inf'), 0.37)
    ],
    "Married filing jointly": [
        (0, 23200, 0.10),
        (23201, 94300, 0.12),
        (94301, 201050, 0.22),
        (201051, 383900, 0.24),
        (383901, 487450, 0.32),
        (487451, 731200, 0.35),
        (731201, float('inf'), 0.37)
    ],
    "Married filing separately": [
        (0, 11600, 0.10),
        (11601, 47150, 0.12),
        (47151, 100525, 0.22),
        (100526, 191950, 0.24),
        (191951, 243725, 0.32),
        (243726, 365600, 0.35),
        (365601, float('inf'), 0.37)
    ],
    "Head of household": [
        (0, 16550, 0.10),
        (16551, 63100, 0.12),
        (63101, 100500, 0.22),
        (100501, 191950, 0.24),
        (191951, 243700, 0.32),
        (243701, 609350, 0.35),
        (609351, float('inf'), 0.37)
    ]
}

def calculate_federal_tax(income, status):
    if status not in federal_tax_brackets:
        raise ValueError("Invalid status. Choose from 'Single', 'Married filing jointly', 'Married filing separately', 'Head of household'.")

    brackets = federal_tax_brackets[status]
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
    status = "Single"
    print(calculate_federal_tax(201760, status=status))
