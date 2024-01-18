import sys

##sys.argv[1]

##consider scaliebilty and extensivibility - make sure your code is flexible (scale and add more features)
##print(sys.argv[1]*1*1.13)


def parseArguments(): ##dictionary 
     arguments = {
          "price": int(sys.arv[1]),
          "quantity": 1,
          "province":"ON"
     }
     return arguments ##allows to scale up arguments - can add more arguments that you want to read from comman line 

def taxRate(province):
     tax ={
          "ON": 0.13
     }
     return tax[province]

def mcmerchCalculator():
     arguments = parseArguments()
     tax = taxRate(arguments['province'])

     print(arguments['price']*arguments['quantity']*(1+tax))


mcmerchCalculator()
