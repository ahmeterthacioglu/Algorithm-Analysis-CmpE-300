from numpy.random import randint
import time
import math

arraylist = [1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
for num in arraylist:
    for case in range(0, 3):
        if case == 0:
            n = num
            arr = [0 for o in range(n)]
            y = 0
            begin = time.time()
            for i in range(0, n):
                if arr[i] == 0:
                    for j in range(i, n):
                        y += 1
                        k = n
                        while k > 0:
                            k = k // 3
                            y += 1
                elif arr[i] == 1:
                    for m in range(i, n):
                        y += 1
                        for l in range(m, n):
                            for t in range(n, 0, -1):
                                for z in range(n, 0, -t):
                                    y += 1
                else:
                    y += 1
                    p = 0
                    while p < n:
                        for j in range(0, p ** 2):
                            y += 1
                        p += 1
            end = time.time()
            print("Case: best Size: {0} Elapsed Time: {1}".format(num, end - begin))
        elif case == 1:
            n = num
            if n == 1:
                arr = [1]
            else:
                ie = n - math.floor(math.sqrt(((2*n**2 + 1 - 3*n)/(3*math.log(n))) + 0.25) - 0.5)
                arr = [2 if v > ie else 1 for v in range(n)]
            y = 0
            begin = time.time()
            for i in range(0, n):
                if arr[i] == 0:
                    for j in range(i, n):
                        y += 1
                        k = n
                        while k > 0:
                            k = k // 3
                            y += 1
                elif arr[i] == 1:
                    for m in range(i, n):
                        y += 1
                        for l in range(m, n):
                            for t in range(n, 0, -1):
                                for z in range(n, 0, -t):
                                    y += 1
                else:
                    y += 1
                    p = 0
                    while p < n:
                        for j in range(0, p ** 2):
                            y += 1
                        p += 1
            end = time.time()
            print("Case: worst Size: {0} Elapsed Time: {1}".format(num, end - begin))
        else:
            timer = 0
            for exc in range(10):
                arr = randint(0, 3, num)
                n = len(arr)
                y = 0
                begin = time.time()
                for i in range(0, n):
                    if arr[i] == 0:
                        for j in range(i, n):
                            y += 1
                            k = n
                            while k > 0:
                                k = k // 3
                                y += 1
                    elif arr[i] == 1:
                        for m in range(i, n):
                            y += 1
                            for l in range(m, n):
                                for t in range(n, 0, -1):
                                    for z in range(n, 0, -t):
                                        y += 1
                    else:
                        y += 1
                        p = 0
                        while p < n:
                            for j in range(0, p**2):
                                y += 1
                            p += 1

                end = time.time()
                timer += (end - begin)
                print("Case: average Size: {0} Elapsed Time: {1}".format(num, end - begin))
            print("Average of the elapsed times of 10 executions = {0}".format(timer/10))
