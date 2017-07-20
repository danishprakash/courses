balance = float(raw_input("Enter the balance"))
annualInterestRate = float(raw_input("Enter the annual interest rate: "))
newbalance = balance
monthlyInterestRate = annualInterestRate/12
monthlyPayment = 0


while newbalance > 0:
	newbalance = balance
	monthlyPayment += 10
	month = 1

	while month <= 12 and newbalance > 0:
		newbalance -= monthlyPayment
		interest = newbalance * monthlyInterestRate
		newbalance += interest
		month += 1
	newbalance = round(newbalance, 2)

print(monthlyPayment)
