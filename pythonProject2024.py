x = input("enter a number: ")       
y = input("enter a second number: ")
        
lesserThan = "is lesser than"
greaterThan = "is greater than"
equalTo = "is equal to"

answerOne = "x equals {}. y equals {}. Therefore, x {} y.".format(x,y,lesserThan)
answerTwo = "x equals {}. y equals {}. Therefore, x {} y.".format(x,y,greaterThan)
answerThree = "x equals {}. y equals {}. Therefore, x {} y.".format(x,y,equalTo)

if x < y:
    print(answerOne)
elif x > y:
    print (answerTwo)
elif x == y:
    print (answerThree)