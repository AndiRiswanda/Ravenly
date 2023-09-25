def plusMinus(arr):
    negative = [x for x in arr if x < 0]
    zero = [x for x in arr if x == 0]
    positive = [x for x in arr if x > 0]
    print (f"{(len(positive)/len(arr)):.6f}")
    print (f"{(len(negative)/len(arr)):.6f}")
    print (f"{(len(zero)/len(arr)):.6f}")
    


plusMinus([-4, 3, -9, 0, 4, 1])