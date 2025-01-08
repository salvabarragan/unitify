class Units():
    def __init__(self, number, unit=""):
        self.number = number
        self.unit = unit
        
    def to_unit(self, unit: str, number, unit_check, unit_check2):
        if unit == "m" or unit == "L" or unit == "g":
            return number
        elif unit.replace(unit_check, "") == "deca":
            return number * 10
        elif unit.replace(unit_check, "") == "hecto":
            return number * 100
        elif unit.replace(unit_check2, "") == "k":
            return number * 1000
        elif unit.replace(unit_check2, "") == "d":
            return number / 10
        elif unit.replace(unit_check2, "") == "c":
            return number / 100
        elif unit.replace(unit_check2, "") == "":
            return number / 1000
        else:
            return "Error"
        
    def to_deci(self):
        self.number *= 10
        self.unit = "d"
        
    def to_centi(self):
        self.number *= 100
        self.unit = "c"
        
    def to_mili(self):
        self.number *= 1000
        self.unit = "m"
        
    def to_deca(self):
        self.number /= 10
        self.unit = "deca"
        
    def to_hecto(self):
        self.number /= 100
        self.unit = "hecto"
        
    def to_kilo(self):
        self.number /= 1000
        self.unit = "k"
