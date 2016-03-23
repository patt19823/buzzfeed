x = int(raw_input("vnesi x "))
while True:
    if x < 1 or x > 100:
        print " buuu"
        x = int(raw_input("vnesi x "))
    else:
        break


i =1

for x in range (0, x):

    if (i % 5 == 0) and (i % 3 == 0):
        print "buzzfeed"
        i += 1



    elif i % 3 == 0:
            print "feed"
            i += 1


    elif i % 5 == 0:
        print "buzz"
        i += 1


    else:
        print i
        i += 1










