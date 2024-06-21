def savings(gross_pay, tax_rate, expenses):
    After_Taxes = int(gross_pay) * float(1-tax_rate)
    After_Expenses = After_Taxes - int(expenses)
    return int(After_Expenses)
    
savings(100.5,0.35,10.3)