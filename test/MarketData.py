import market.FinancialMarketData as fd
import market.QuestradeData as qd
import numpy as np


# data = qd.login("z5nFFCcrSwQzIM4OaAUg3mYBFVigoppP0")
data = qd.searchSymbol('https://api01.iq.questrade.com/', 'TSLA', 'ttlQ48C3eyEB4jPanfLDev0AkTf17iLO0')
print(data)
