def checker(num):
	if num>0:
		print("Positive Number");
	elif num ==0:
		print("Zero");
	else:
		print("Negative Number");

print("Enter a number");
x = int(input());
checker(x);