# MyCalc.py
# UCID: sk3298
# Date: 02/24/2023

class MyCalc:
    ans = 0

    def _is_float(self, val):
        try:
            val = float(val)
            return True
        except:
            return False

    def _is_int(self, val):
        try:
            val = int(val)
            return True
        except:
            return False

    def _as_number(self, val):
        if self._is_int(val):
            return int(val)
        elif self._is_float(val):
            return float(val)
        else:
            raise Exception("Not a number")
    
    # UCID: sk3298
    # Date: 02/24/2023
    # Description: This method takes two numbers as input and returns their sum. 
    # It can also take the string "ans" as the first input to use the result of 
    # the previous operation as the first operand.
    def add(self, num1, num2):
        if num1 == "ans":
            return self.add(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1+num2
        return self.ans
    
    # UCID: sk3298
    # Date: 02/24/2023
    # Description: This method takes two numbers as input and returns their difference. 
    # It can also take the string "ans" as the first input to use the 
    # result of the previous operation as the first operand.
    def sub(self, num1, num2):
        if num1 == "ans":
            return self.sub(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1-num2
        return self.ans

    # UCID: sk3298
    # Date: 02/24/2023
    # Description: This method takes two numbers as input and returns their product.
    # It can also take the string "ans" as the first input to use the result of the previous 
    # operation as the first operand.
    def mult(self, num1, num2):
        if num1 == "ans":
            return self.mult(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1*num2
        return self.ans

    # UCID: sk3298
    # Date: 02/24/2023
    # Description:This method takes two numbers as input and returns their quotient. It can also take 
    # the string "ans" as the first input to use the result of the previous operation as the first operand. 
    # If the second operand is 0, an error message is printed and the function returns None.
    def div(self, num1, num2):
        if num1 == "ans":
            return self.div(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            if num2 == 0:
                print("Can't divide by zero, sorry")
            else:
                self.ans = num1/num2
        return self.ans


if __name__ == '__main__':
    is_running = True
    iSTR = input("Are you ready?")
    calc = MyCalc()
    print(calc)
    if iSTR == "yes":
        while is_running:
            iSTR = input("Enter an expression or 'quit' to exit: ")
            if iSTR == "quit" or iSTR == "q":
                is_running = False
            else:
                print("Your eq was " + str(iSTR))
                if "+" in iSTR:
                    nums = iSTR.split("+")
                    r = calc.add(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))
                # must be done before - check to hanlde negative values
                elif "/" in iSTR:
                    nums = iSTR.split("/")
                    r = calc.div(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))

                elif "*" in iSTR or "x" in iSTR:
                    nums = iSTR.split("*") if "*" in iSTR else iSTR.split("x")
                    r = calc.mult(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))
                # must be done last so negative numbers work
                elif "-" in iSTR:
                    nums = iSTR.split("-")
                    r = calc.sub(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))




    else:
        print("Good bye")
        is_running = False
