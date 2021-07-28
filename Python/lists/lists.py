myUniqueList = []
myLeftovers = []


def appender(var):
    if var in myUniqueList:
        myLeftovers.append(var)
        return False
    else:
        myUniqueList.append(var)
        return True


var = appender(3)
var = appender(10)
var = appender(5)
var = appender("Hey teacher :)")
var = appender(3)
var = appender(4.1)
var = appender("pirple")
var = appender("pirple")
var = appender(60)
var = appender(4.1)

print(myUniqueList)
print(var)
print(myLeftovers)
