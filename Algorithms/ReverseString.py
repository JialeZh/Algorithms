string = "ReverseThis"
print (string)

##Convert string to list and then reverse list
##Convert List back to string and return finished string
def reverseString(string):
    finishedString = " "
    li = list(string)
    li.reverse()
    return (finishedString.join(li))



print(reverseString(string))
