class Stocks:
    def __init__(self , name , symbol , prices = []):

        self.name = name
        self.symbol = symbol
        self.prices = prices
    def maxprice(self):

        if len(self.prices) == 0:
            print("NO PRICES GIVEN")

        return max(self.prices)


apple = Stocks("Apple" , "APPL" , [1.20,3.45])
marcedes = Stocks("Marcedes" , "MAR" , [1.330,5.45])
jaguar = Stocks("Jaguar" , "JAG" , [4.8,7.465])
samsung = Stocks("Samsung" , "SSN" , [3.20,4.65])
hyundai = Stocks("Hyundai" , "HUN" , [4.20,3.47])

max(apple.maxprice() , marcedes.maxprice())