import unittest
from src.length import Length

class TestLength(unittest.TestCase):
    def setUp(self):
        self.length = Length(4, "m")
        
    def test_to_deci(self):
        self.length.to_deci()
        self.assertEqual(str(self.length), "40 dm")
        
    def test_to_centi(self):
        self.length.to_centi()
        self.assertEqual(str(self.length), "400 cm")
    
    def test_to_mili(self):
        self.length.to_mili()
        self.assertEqual(str(self.length), "4000 mm")
    
    def test_to_deca(self):
        self.length.to_deca()
        self.assertEqual(str(self.length), "0.4 decametres")
        
    def test_to_hecto(self):
        self.length.to_hecto()
        self.assertEqual(str(self.length), "0.04 hectometres")
        
    def test_to_kilo(self):
        self.length.to_kilo()
        self.assertEqual(str(self.length), "0.004 km")
        
    def test_to_miles(self):
        self.length.to_miles()
        self.assertEqual(str(self.length), "0.0024854799999945087 miles")    
        
    def test_to_yards(self):
        self.length.to_yards()
        self.assertEqual(str(self.length), "4.37444 yards")
    
    def test_unkown_unit(self):
        self.length = Length(5, "p")
        self.assertEqual(str(self.length), "ERROR: Invalid unit.")

    
if __name__ == '__main__':
    unittest.main()