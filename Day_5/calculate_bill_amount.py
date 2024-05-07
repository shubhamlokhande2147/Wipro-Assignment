def calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity):
    total_bill = 0

    for gem, quantity in zip(reqd_gems, reqd_quantity):
        if gem in gems_list:
            index = gems_list.index(gem)
            total_bill += price_list[index] * quantity
        else:
            return -1
    
    if total_bill > 30000:
        total_bill -= total_bill * 0.05

    return total_bill

# List of gems available in the store
gems_list = ["Emerald", "Ivory", "Jasper", "Ruby", "Garnet"]

# Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list = [1760, 2119, 1599, 3920, 3999]

# List of gems required by the customer
reqd_gems = ["Ivory", "Emerald", "Garnet"]

# Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity = [3, 10, 12]

bill_amount = calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)

print("Total bill amount:", bill_amount)
