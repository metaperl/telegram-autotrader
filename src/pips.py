"""
Support for forex pip calculations.

Resources:
https://forums.babypips.com/t/having-problem-finding-number-of-pips/111993/2
https://stackoverflow.com/questions/48038949/find-pips-value-3-to-5-digits-forex-pricing-calculation
https://www.luckscout.com/how-to-measure-the-number-of-pips-of-a-price-move-on-mt4/


"""


def multiplier(price):
    """
    The "multiplier" is a number that indicates what to multiply price difference by to get pips.

    Examples:
    The pip distance between 1.25661 and 1.10896 on EUR/USD chart is 1476.5 pips:
    1.25661 – 1.10896 = 0.14765
    Then multiply 0.14765 by 10000

    The pip distance between 114.234 and 114.212 = abs(price1 - price2) * 100

    The multiplier for prices with 3 digits after decimal = 100
    The multiplier for prices with 4 or 5 digits after decimal = 10000

    :param price: a floating point number that will have 3, 4, or 5 digits after decimal. E.g. 112.321
    :return:
    """

    before, after = str(price).split('.')
    if len(after) == 3:
        return 100
    if len(after) == 4:
        return 10000
    if len(after) == 5:
        return 10000
    raise Exception(f"unable to calculate multipler for price {price}.")

def pips_between(price1, price2):
    """
    Return the number of pips between price1 and price2.

    :param price1: float
    :param price2: float
    :return: float
    """
    diff = abs(price1 - price2) * multiplier(price1)
    return round(diff, 1)


if __name__ == '__main__':
    prices=[
        (114.234, 114.204),
        (1.12345, 1.12305),
        (1.12345, 1.12340)
    ]

    for p1, p2 in prices:
        print("The pip difference between {} and {} is {}".format(
            p1, p2, pips_between(p1,p2)
        ))