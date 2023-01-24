def and_not(inputs, weights, threshold=2):
    total = 0
    for i, j in zip(inputs, weights):
        total += i*j
    print(f"total: {total}")
    if total >= threshold:
        return 1
    return 0 

print(and_not([1,2,3,4,5], [0,1,-1,1,1]))     
