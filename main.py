from resources import variables
for i in range(7):
    ans = int(input("How many bancnotes of " + variables.moneyNames[variables.count] + " do you have?"))
    variables.totalAmount += ans*variables.moneyValues[variables.count]
    variables.count = variables.count + 1
print("Your total amount is ", variables.totalAmount)