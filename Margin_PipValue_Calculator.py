#! python3

'''This program is my attempt at making a calculator to make the process of calculating margin requirements and the
value of a trades movements with ease, allowing the user to focus more on his strategy than bing worried about going
through many steps to know how much you stand to gain or lose'''
# Just updated the repository name. This is to test if it work

CurrentPrice = 0.0
Contract_Size = 0
Leverage = 1
Lot_Size = 0
CurrentPrice += float(input('Enter Current position/price: '))
Contract_Size += float(input("Currency pairs[1] Other Products[2]. Enter corresponding number: "))
TradeType = ''
TheDifference = 0

if (Contract_Size == 1):
    Contract_Size1 = int(input('Standard[1] or Micro[2]: '))
    if (Contract_Size1 == 1):
        Contract_Size = float(100000)
        Leverage = float(input('Enter leverage: '))
    elif (Contract_Size1 == 2):
        Contract_Size = float(1000)
        Leverage = float(input('Enter leverage: '))
else:
    if (float(Contract_Size == 2)):
        Contract_Size = int(input('Enter desired contract size:'))
        stock_or_Not = input("Is this item a stock option: Enter [y] or [n]")
        if (stock_or_Not == 'y'):
            TradeType = 'Stock'
            pass
        elif (stock_or_Not == 'n'):
            Leverage = float(input('Enter leverage: '))

Lot_Size = float(input('Enter lot size: '))
TradeSize = Lot_Size * Contract_Size

if (TradeType == 'Stock'):
    TradeSize /= Contract_Size
    TheRealTradeSize = TradeSize
    Actual_Value = TheRealTradeSize * CurrentPrice
    print('Margin requirement for the desired trade: ' + str(Actual_Value))
    proceed_to_make_money = input("Claculate price action? Type 'y' or 'n' as your answer: ")
elif (TradeType != 'Stock'):
    TheRealTradeSize = TradeSize / Leverage
    Actual_Value = TheRealTradeSize * CurrentPrice
    print('Margin requirement for the desired trade: ' + str(Actual_Value))
    proceed_to_make_money = input("Claculate price action? Type 'y' or 'n' as your answer: ")
if (proceed_to_make_money == 'y'):
    Closing_Price = float(input("Enter closing price:  "))
    TheDifference = Closing_Price - CurrentPrice
    if (TheDifference < 0):
        TheDifference *= -1
TheDifference *= Contract_Size
if (TradeType == 'Stock'):
        print("Total price difference:" + str(TheDifference))
        print("Please be advised, you should convert this price to your currency to know the value to you.")
elif (TradeType != 'Stock'):
        print("Total price difference:" + str(TheDifference * Lot_Size))
        print("Please be advised, you should convert this price to your currency to know the value to you.")