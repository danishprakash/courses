balance = int(raw_input("Enter the balance: "))
annualInterestRate = float(raw_input("Enter annual interest rate: "))
monthlyPaymentRate = float(raw_input("Enter monthly payment rate: "))

for i in range(0,12):
	monthlyInterestRate = annualInterestRate/12
	minMonthlyPayment = monthlyPaymentRate*balance
	monthlyUnpaidBalance = balance - minMonthlyPayment
	balance = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)

print(str(round(balance,2)))
