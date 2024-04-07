class Holding:
    ticker:str
    name: str
    weight: float
    exchange = ""
    
    def __init__(self):
        return
    
    def is_equal(self, holding):
        return self.ticker == holding.ticker and self.exchange == holding.exchange
    
    def is_equal_by_ticker(self, exchange, ticker):
        return self.ticker == ticker and self.exchange == exchange