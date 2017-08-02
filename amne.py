# amne challenge
#
# Ratul Esrar, 8/2/17


'''
for i in range(len(l)):
    r = l[i:k+i]
    d = {}
    if len(r) is k:
        for j in range(k):
            print r[j]
'''
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
