def exchange_money(budget, exchange_rate):
    exchanged = budget / exchange_rate
    #print(f'total: {exchanged}')
    return exchanged

#exchange_money(127.5,1.2)

def get_change(budget, exchanging_value):
    exchanged = budget - exchanging_value
    #print(f'total: {exchanged}')
    return exchanged

#get_change(127.5,120)

def get_value_of_bills(denomination, number_of_bills):
    exchanged = denomination * number_of_bills
    #print(f'total: {exchanged}')
    return exchanged

#get_value_of_bills(5,128)

def get_number_of_bills(budget, denomination):
    exchanged = int(budget / denomination)
    #print(f'total: {exchanged}')
    return exchanged

#get_number_of_bills(127.5, 5)

def get_leftover_of_bills(budget, denomination):
    exchanged = budget % denomination
    #print(f'total: {exchanged}')
    return exchanged

#get_leftover_of_bills(127.5,20)

def exchangeable_value(budget, exchange_rate, spread, denomination):
    porcent_decimal = spread / 100
    porcent = exchange_rate + get_value_of_bills(exchange_rate,porcent_decimal)
    exchanged = exchange_money(budget, porcent)
    max_denomined = get_number_of_bills(exchanged, denomination) * denomination
    #print(f'Total: {max_denomined}')
    print(max_denomined)
    return max_denomined

exchangeable_value(127.25,1.20,10,20)