class Mobile:
    
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def __eq__(self, other):
        if isinstance(other, Mobile):
            return self.brand == other.brand and self.model == other.model
        return False
m1 = Mobile("Samsung", "S23", 70000)
m2 = Mobile("Samsung", "S23", 72000)
m3 = Mobile("Apple", "iPhone 14", 80000)
print("m1 == m2:", m1 == m2)   
print("m1 == m3:", m1 == m3)   
print("m2 == m3:", m2 == m3)
