from sys import argv

try:
	script_name, hours, pay_rate, over_pay = argv
	try:
		print(int(hours)*int(pay_rate)+int(over_pay))
	except ValueError:
		print("Enter only numbers")
	
except ValueError:
	print("Incorrect quantity of params (enter three numbers)")