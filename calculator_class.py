class calculator:
    def __init__(self):
        pass
    def __del__(self):
        pass
    def handling_user_ipnut(self):
        ebarat =input("loftan ebarat khodra vared konid:") # "(1+3*(2-4)-3)*(1+3*(2-4)-3)" 
        ebarat=ebarat.replace(' ','')
        while not  self.is_formart_correct(ebarat):
            print("\033[1;31;40mebarat vared sode etebah ast \033[0;37;40m")#31 is red , 37 is white #default value = \033[0;37;40m
            ebarat = input("loftan ebarat khodra vared konid:")

        lis = []
        startOfNumber = 0
        endOfNumber = 0
        for i in range(len(ebarat)):
            if ebarat[i] == '+' or ebarat[i] == '-' or ebarat[i] == '*' or ebarat[i] == '/' or ebarat[i]=='(' or ebarat[i]==')' :
                endOfNumber = i - 1
                lis.append(ebarat[startOfNumber:endOfNumber+1])
                startOfNumber = i + 1
                lis.append(ebarat[i])

        endOfNumber = len(ebarat)
        lis.append(ebarat[startOfNumber:endOfNumber+1])

        while '' in lis:
            lis.remove('')
        #print(lis)
        return lis
            
    def is_formart_correct(self,ebarat):
        for x in ebarat:
            if not ( x=='+' or x=='-' or x=='*' or x=='/' or x=='1' or  x=='2' or  x=='3' or  x=='4' or  x=='5' or  x=='6' or  x=='7' or  x=='8' or  x=='9' or x=='0' or   x=='(' or  x==')'):
                return False
        return True

    def addition(self,ebarat):
        try:
            ebarat.index("+")
        except:
            return False
        numberBefore = ebarat.pop(ebarat.index("+") - 1)
        numberAfter = ebarat.pop(ebarat.index("+") + 1)
        ebarat[ebarat.index("+")] = int(numberBefore) + int(numberAfter)
        return True

    def submission(self,ebarat):
        try:
                ebarat.index("-")
        except:
            return False
        numberBefore = ebarat.pop(ebarat.index("-") - 1)
        numberAfter = ebarat.pop(ebarat.index("-") + 1)
        ebarat[ebarat.index("-")] = int(numberBefore) - int(numberAfter)
        return True


    def multiplication(self,ebarat):
        try:
            ebarat.index("*")
        except:
            return False
        numberBefore = ebarat.pop(ebarat.index("*") - 1)
        numberAfter = ebarat.pop(ebarat.index("*") + 1)
        ebarat[ebarat.index("*")] = int(numberBefore) * int(numberAfter)
        return True

    def division(seld,ebarat):
        try:
            ebarat.index("/")
        except:
            return False
        numberBefore = ebarat.pop(ebarat.index("/") - 1) #number before oprator
        numberAfter = ebarat.pop(ebarat.index("/") + 1) #number after oprator
        ebarat[ebarat.index("/")] = int(numberBefore) / float(numberAfter)
        return True

    def operators(self,ebarat):
        flag_multiplication = True
        flag_division = True
        flag_addition = True
        flag_submission = True
        while flag_multiplication or flag_division or flag_addition or flag_submission :
            if flag_multiplication :
                flag_multiplication =  self.multiplication(ebarat)
            elif flag_division:
                flag_division =  self.division(ebarat)
            elif flag_addition:
                flag_addition =  self.addition(ebarat)
            elif flag_submission:
                flag_submission =  self.submission(ebarat)
        return ebarat[0]

    def handleing_parentheses( self,ebarat):
        while "(" in ebarat:
            startP = 0 #start of parentheses
            endP = 0 #end of parentheses
            for x in range(len(ebarat)):
                if ebarat[x] == "(":
                    startP = x
            for x in range(startP, len(ebarat)):
                if ebarat[x] == ")":
                    endP = x
                    break
            thingsThatOpratorsShouldHandel = ebarat[startP+1:endP]
            thingsThatOpratorsShouldHandel = self.operators(thingsThatOpratorsShouldHandel)

            while ebarat[startP] !=')':#to remove the parentheses that selected
                ebarat.pop(startP)
            ebarat.pop(startP)
            
            
            
            ebarat.insert(startP , thingsThatOpratorsShouldHandel)
        return  self.operators(ebarat)
    
    def write(self,ebarat):
        string = ""
        for x in ebarat:
            string += str(x)
            string += ' '
        
        string += '= '
        return string

    def mainloop(self):
        while True:
            file = open("history.txt","at")
            ebart = self.handling_user_ipnut()
            file.write(self.write(ebart))
            ebart = self.handleing_parentheses(ebart)
            file.write(str(ebart) + "\n")
            print("\033[1;32;40m", ebart,'\033[0;37;40m')
            file.close()

 
