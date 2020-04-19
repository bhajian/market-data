import market.FinancialMarketData as fd
import market.QuestradeData as QD
import numpy as np


qd = QD.QuestradeData()
data = qd.login('XXXX')
data = qd.getCandles('AAPL', '2020-01-01T00:00:00-05:00', '2020-10-20T23:59:59-05:00', 'OneDay')
print(data)
