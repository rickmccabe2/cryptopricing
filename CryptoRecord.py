class CryptoRecord(object):
  def __init__(self, symbol, prevClosePrice, openPrice, highPrice, lowPrice):
    self.symbol = symbol
    self.prevClosePrice = prevClosePrice
    self.openPrice = openPrice
    self.highPrice = highPrice
    self.lowPrice = lowPrice