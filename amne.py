# Amne Challenge
#
# Ratul Esrar, 8/3/17


import sys


def segment_prices(input_list, k):
    '''
    Takes a list of n positive integers and a k such that 1 <= k <= n
    Segments input list into subranges of length n - k+1
    Returns list of subranges stored in lists

    Inputs:
        input_list (list)
        k (int)

    Output:
        windows (list)
    '''
    windows = []
    for i in range(len(input_list)):
        l = input_list[i:k+i]
        if len(l) == k:
            windows.append(l)
    return windows


def analyze_subrange(window):
    '''
    Takes a list of prices and calculates the number of subranges that are increasing, descreasing, or static
    Returns the difference between the number of increasing and decreasing subranges

    Input:
        prices (list)

    Output
        inc - dec (calculated int)
    '''
    inc = 0
    dec = 0
    eq = 0
    consec_inc = 0
    consec_dec = 0
    consec_eq = 0
    for i, current_val in enumerate(window):
        if i is 0:
            continue
        prev_val = window[i-1]
        if current_val > prev_val:
            consec_inc += 1
            consec_dec = 0
            inc += consec_inc
        elif current_val < prev_val:
            consec_dec += 1
            consec_inc = 0
            dec += consec_dec
        elif current_val == prev_val:
            consec_eq += 1
            consec_inc = 0
            consec_dec = 0
            eq += consec_eq
    return inc - dec


if __name__ == '__main__':
    in_file = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
    out_file = open(sys.argv[-1], 'w') if len(sys.argv) > 2 else sys.stdin
    dummy_list = []
    for line in in_file:
        dummy_list.append(map(int, line.split()))
    in_file.close()
    n, k = dummy_list[0][0], dummy_list[0][1]
    price_list = dummy_list[1]
    windows = segment_prices(price_list, k)
    for window in windows:
        result = analyze_subrange(window)
        out_file.write(str(result)+'\n')
        print result
    out_file.close()
