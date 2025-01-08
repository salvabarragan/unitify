from src.units import Units

class Length(Units):
    def __init__(self, number, unit):
        reviewed_number = self.to_unit(unit, number, "metres", "m")
        if reviewed_number == "Error":
            self.number = 0
            self.unit = "unit"
        elif reviewed_number:
            self.number = reviewed_number
            self.unit = unit
        else:
            self.number = number
            self.unit = unit
        
        
    def to_miles(self):
        self.to_unit(self.unit, self.number, "metres", "m")
        self.number /= 1609.34708789 
        self.unit = "miles"
        
    def to_yards(self):
        self.to_unit(self.unit, self.number, "metres", "m")
        self.number *= 1.09361
        self.unit = "yards"
        
    def __str__(self):
        if self.unit == "miles" or self.unit == "yards":
            return f"{self.number} {self.unit}"
        elif self.unit == "deca" or self.unit == "hecto":
                return f"{self.number} {self.unit + "metres"}"
        elif self.unit == "k" or self.unit == "d" or self.unit == "c" or self.unit == "m":
            return f"{self.number} {self.unit + "m"}"
        else:
            return "ERROR: Invalid unit."