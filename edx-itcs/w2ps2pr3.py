balance = float(raw_input("Enter the balance"))
annualInterestRate = float(raw_input("Enter the annual interest rate: "))
newbalance = balance
monthlyInterestRate = annualInterestRate/12
monthlyPayment = 0

minimum = balance / 12
maximum = (balance * (1 + monthlyInterestRate)**12) / 12.0
guessMinimum = (minimum+maximum)/2

mini = 0.1


while newbalance >= mini:
	guessMinimum = (minimum + maximum)/2

	for i in range(0,12):
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
