class Fraction:

    def __init__(self, n, d):
        self.num = n
        self.den = d

    def __str__(self):
        return f'{self.num}/{self.den}'

    def __add__(self, other):
        temp_num = self.num + other.num
        temp_deb = self.den + other.den
        return f'{temp_num}/{temp_deb}'

    def __add__(self, other):
        temp_num = self.num - other.num
        temp_deb = self.den - other.den
        return f'{temp_num}/{temp_deb}'
    
    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_deb = self.den * other.den
        return f'{temp_num}/{temp_deb}'
    

    def __truediv__(self, other):
        temp_num = self.num / other.num
        temp_deb = self.den / other.den
        return f'{temp_num}/{temp_deb}'
