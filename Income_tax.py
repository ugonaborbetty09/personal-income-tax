print("Personal Income Tax Calculator")

status = int(input("Enter filing status (0=Single, 1=Married Joint, 2=Married Separate, 3=Head of Household): "))
income = float(input("Enter taxable income: "))

tax = 0

if status == 0:
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 8350 * 0.10
        tax += (income - 8350) * 0.15
    elif income <= 82250:
        tax = 8350 * 0.10
        tax += (33950 - 8350) * 0.15
        tax += (income - 33950) * 0.25
    else:
        tax = 8350 * 0.10
        tax += (33950 - 8350) * 0.15
        tax += (82250 - 33950) * 0.25
        tax += (income - 82250) * 0.28

elif status == 1:
    if income <= 16700:
        tax = income * 0.10
    elif income <= 67900:
        tax = 16700 * 0.10
        tax += (income - 16700) * 0.15
    else:
        tax = 16700 * 0.10
        tax += (67900 - 16700) * 0.15
        tax += (income - 67900) * 0.25

elif status == 2:
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 8350 * 0.10
        tax += (income - 8350) * 0.15
    else:
        tax = 8350 * 0.10
        tax += (33950 - 8350) * 0.15
        tax += (income - 33950) * 0.25

elif status == 3:
    if income <= 11950:
        tax = income * 0.10
    elif income <= 45500:
        tax = 11950 * 0.10
        tax += (income - 11950) * 0.15
    else:
        tax = 11950 * 0.10
        tax += (45500 - 11950) * 0.15
        tax += (income - 45500) * 0.25

else:
    print("Invalid filing status")

print("Total tax is:", tax)
