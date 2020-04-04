"""
Parse the signals from Olafemi Adeyemo's Telegram channel.
"""

sample_signal = """Opengates Forex Trade Signal Alert Services:

Symbol: EURNZD

Action: SELL

Entry: 1.83605

TakeProfit: 1.83386

StopLoss: 1.85217

Good Favor.
"""

import re
from pyparsing import Word, alphas, alphanums, CaselessKeyword, CaselessLiteral, Combine, Optional, Literal, nums
from pyparsing import Regex


header = Regex("Opengates.+Services:", flags=re.IGNORECASE)

trading_pair = Word(alphanums, exact=6)
symbol = CaselessKeyword("Symbol:") + trading_pair

buy_or_sell = CaselessLiteral("buy") | CaselessLiteral("sell")
action = CaselessKeyword("Action:") + buy_or_sell

point = Literal(".")
e = CaselessLiteral("E")
plusorminus = Literal("+") | Literal("-")
number = Word(nums)
integer = Combine(Optional(plusorminus) + number)
float_number = Combine(
    integer + Optional(point + Optional(number)) + Optional(e + integer)
)
entry = CaselessKeyword("Entry:") + float_number
take_profit = CaselessKeyword("TakeProfit:") + float_number
stop_loss = CaselessKeyword("StopLoss:") + float_number

footer = Regex(".+", flags=re.IGNORECASE)

trade_signal = header + symbol + action + entry + take_profit + stop_loss + footer

def list_to_dict(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct

def parse(signal):
    result = trade_signal.parseString(signal)
    print(f"Result of parsing={result}")
    result = result[1:-1]
    print(f"Trimmed Result of parsing={result}")
    dict = list_to_dict(result)
    print(f"Dict={dict}")
    dict2 = {}
    for k, v in dict.items():
        k = k[:-1]
        print(k)
        k = k.lower()
        if k in "entry takeprofit stoploss":
            print("\tconverting...")
            v = float(v)
        dict2[k] = v

    dict = dict2

    print(f"Dict={dict}")
    return dict


if __name__ == '__main__':
    parse(sample_signal)
