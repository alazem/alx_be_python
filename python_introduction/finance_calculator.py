income = int(input("Enter your monthly income: "));
expenses = int(input("Enter your total monthly expenses: "));
savings = float(income)- float(expenses);
print("Your monthly savings are " + str(savings)); 
projected_savings = savings * 12 + (savings*12*0.05);
print("Projected savings after one year, with interest, is: " +str(projected_savings));
