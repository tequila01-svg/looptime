def myfunction(n):
    # First loop
    for i in range(0, n+1):
        print("first loop")
    
    # Second loop (logarithmic complexity)
    j = 1
    while j <= n+1:
        print("second loop", j)
        j = j * 2
    
    # Third loop (constant complexity)
    for i in range(0, 100):
        print("third loop")