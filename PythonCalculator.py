operator = input("What operation you want to perform(+, -, *, /, %):")
firstnum = int(input("Enter First Number:"))
secondnum = int(input("Enter Second Number:"))
calcvalue = int(0)
if operator == '+':
    calcvalue = firstnum+secondnum
elif operator == '-':
    calcvalue = firstnum-secondnum
elif operator == '*':
    calcvalue = firstnum*secondnum
elif operator == '/':
    calcvalue = firstnum/secondnum
elif operator == '%':
    calcvalue = firstnum%secondnum
print("Calcualted Value = " + str(calcvalue))