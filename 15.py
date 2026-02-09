for a in range (2000):
    if all( (x*y < a) or (y > x) or (x >= 8)
           for x in range (1, 2001) \
           for y in range (1, 2001) ):
        print(a)
        break