# amne challenge
#
# Ratul Esrar, 8/2/17


def segment_prices(input_list, k):
    '''
    '''
    range_list = []
    for i in range(len(input_list)):
        l = input_list[i:k+i]
        range_list.append(input_list)
    return range_list
    
def analyze_subrange(prices, k):
    '''
    '''
    inc = 0
    dec = 0
    consec_inc = 0
    consec_dec = 0
    for i, current_val in enumerate(prices):
        if i is 0:
            continue
        prev_val = prices[i-1]
        if current_val < prev_val:
            if consec_dec == 0:
                consec_dec = 1
            else:
                consec_dec += 1

            consec_inc = 0
            dec += consec_dec
        elif current_val > prev_val:
            if consec_inc == 0:
                consec_inc = 1
            else:
                consec_inc += 1

            consec_dec = 0
            inc += consec_inc
        else:
            if consec_inc == 0:
                consec_inc = 1
                consec_dec += 1
            if consec_dec == 0:
                consec_dec = 1
                consec_inc += 1
            inc += consec_inc
            dec += consec_dec

    return inc, dec
