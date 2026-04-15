class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    @property
    def numerator(self):
        return self.__numerator
    
    @numerator.setter
    def numerator(self, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise ValueError("Numerator must be a number.")
        self.__numerator = value

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise ValueError("Denominator must be a number.")
        if value == 0:
            raise ValueError("Denominator cannot be zero.")
        self.__denominator = value

    def add(self, f):
        if not isinstance(f, Fraction):
            raise ValueError("Argument must be a Fraction.")
        
        a = self.numerator * f.denominator + f.numerator * self.denominator
        b = self.denominator * f.denominator

        return Fraction(a, b)
    
    def sub(self, f):
        if not isinstance(f, Fraction):
            raise ValueError("Argument must be a Fraction.")
        
        a = self.numerator * f.denominator - f.numerator * self.denominator
        b = self.denominator * f.denominator

        return Fraction(a, b)
    
    def mul(self, f):
        if not isinstance(f, Fraction):
            raise ValueError("Argument must be a Fraction.")
        
        a = self.numerator * f.numerator
        b = self.denominator * f.denominator

        return Fraction(a, b)
    
    def div(self, f):
        if not isinstance(f, Fraction):
            raise ValueError("Argument must be a Fraction.")
        
        if f.numerator == 0:
            raise ValueError("Cannot divide by zero fraction.")
        
        a = self.numerator * f.denominator
        b = self.denominator * f.numerator

        return Fraction(a, b)
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
### TEST ###
f1 = Fraction(1, 2)
f2 = Fraction(3, 4)
f3 = f1.add(f2)
print(f"{f1} + {f2} = {f3}")
f4 = f1.sub(f2)
print(f"{f1} - {f2} = {f4}")
f5 = f1.mul(f2)
print(f"{f1} * {f2} = {f5}")
f6 = f1.div(f2)
print(f"{f1} / {f2} = {f6}")