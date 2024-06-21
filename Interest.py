def interest(principal, rate, periods):
    Quantity = float(rate) * int(periods)
    Simple_Interest = int(principal) * Quantity
    Final_Money = principal + Simple_Interest
    return int(Final_Money)

interest(1000,0.1,1)