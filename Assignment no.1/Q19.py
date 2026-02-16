# Tuple unpacking: Loop over list of (x,y) coords, dict to count quadrant (if x>0,y>0 etc.).

# list of x,y coords

points = [(2,3), (4,-1), (1,1),(-2,6), (-3,-2)]

Q_count = {"Q1":0, "Q2":0, "Q3":0, "Q4":0}

for x,y in points:
    if x> 0 and y>0:
        Q_count["Q1"] +=1
    elif x<0 and y>0:
        Q_count["Q2"] +=1
    elif x<0 and y<0:
        Q_count ["Q3"] +=1
    elif x>0 and y<0:
        Q_count ["Q4"] +=1

print("Quadrant count:", Q_count)