
# importing numpy as np
from unittest import result
import numpy as np
import random


while 1:
    print("\nEnter 1 to ADD two Martices\nEnter 2 to SUBTRACT two Matrices\nEnter 3 to MULTIPLY TWO Matrices\nEnter 4 to DIVIDE TWO MATRICES\nEnter 5 to EXIT\n")
    i = int(input("Enter --->"))

    if i == 1:  # !!!!!!!!!!
        R1 = int(input("\t\t\t\t\t\tEnter the number of rows of Matrix 1 :"))
        C1 = int(input("\t\t\t\t\t\tEnter the number of columns of Matrxix 1 :"))
        matrix1 = []
        print("Enter the entries row wise:")
        for i in range(R1):
            a = []
            for j in range(C1):
                a.append(int(input()))
            matrix1.append(a)
        R2 = int(input("\t\t\t\t\t\tEnter the number of rows of Matrix 2 :"))
        C2 = int(input("\t\t\t\t\t\tEnter the number of columns of Matrix 2 :"))
        matrix2 = []
        # print("Enter the entries row wise:")
        for i in range(R1):
            a = []
            for j in range(C1):
                a.append(random.randint(0, 100))
            matrix2.append(a)
        print("\t\t\t\t\t\tArray 1 is :", matrix1,
              "\n\t\t\t\t\t\tArray 2 is : ", matrix2)

        if (R1 != R2 or C1 != C2):
            print("\t\t\t\t\t\tGiven Matrix cannot be added !\n")
            break
        else:
            R = np.add(matrix1, matrix2)
            print("\t\t\t\t\t\tThe Matrix obtained by addition is : ", R)

    if i == 2:  # !!!!!!!!!!
        R1 = int(input("\t\t\t\t\t\tEnter the number of rows of Matrix 1 :"))
        C1 = int(input("\t\t\t\t\t\tEnter the number of columns of Matrxix 1 :"))
        matrix1 = []
        print("Enter the entries row wise:")
        for i in range(R1):
            a = []
            for j in range(C1):
                a.append(int(input()))
            matrix1.append(a)
        R2 = int(input("\t\t\t\t\t\tEnter the number of rows of Matrix 2 :"))
        C2 = int(input("\t\t\t\t\t\tEnter the number of columns of Matrix 2 :"))
        matrix2 = []
        # print("Enter the entries row wise:")
        for i in range(R1):
            a = []
            for j in range(C1):
                a.append(random.randint(0, 100))
            matrix2.append(a)
        print("\t\t\t\t\t\tArray 1 is :", matrix1,
              "\n\t\t\t\t\t\tArray 2 is : ", matrix2)

        if (R1 != R2 or C1 != C2):
            print("\t\t\t\t\t\tGiven Matrix cannot be Subtracted !\n")
            break
        else:
            R = np.subtract(matrix1, matrix2)
            print("\t\t\t\t\t\tThe Matrix obtained by Subtarction is : ", R)

    if i == 3:  # !!!!!!!!!!
        R1 = int(input("\t\t\t\t\t\tEnter the number of rows of Matrix 1 :"))
        C1 = int(input("\t\t\t\t\t\tEnter the number of columns of Matrxix 1 :"))
        matrix1 = []
        print("Enter the entries rowwise:")
        for i in range(R1):
            a = []
            for j in range(C1):
                a.append(int(input()))
            matrix1.append(a)
        R2 = int(input("\t\t\t\t\t\tEnter the number of rows of Matrix 2 :"))
        C2 = int(input("\t\t\t\t\t\tEnter the number of columns of Matrix 2 :"))
        matrix2 = []
        # print("Enter the entries rowwise:")
        for i in range(R1):
            a = []
            for j in range(C1):
                a.append(random.randint(0, 100))
            matrix2.append(a)
        print("\t\t\t\t\t\tArray 1 is :", matrix1,
              "\n\t\t\t\t\t\tArray 2 is : ", matrix2)

        if (C1 != R2):
            print("\t\t\t\t\t\tGiven Matrix cannot be Multiplicated !\n")
            break
        else:
            R = np.multiply(matrix1, matrix2)
            print("\t\t\t\t\t\tThe Matrix obtained by Multiplication is : ", R)

    if i == 4:  # !!!!!!!!!!
        R1 = int(input("\t\t\t\t\t\tEnter the number of rows of Matrix 1 :"))
        C1 = int(input("\t\t\t\t\t\tEnter the number of columns of Matrxix 1 :"))
        matrix1 = []
        print("Enter the entries row wise:")
        for i in range(R1):
            a = []
            for j in range(C1):
                a.append(int(input()))
            matrix1.append(a)
        R2 = int(input("\t\t\t\t\t\tEnter the number of rows of Matrix 2 :"))
        C2 = int(input("\t\t\t\t\t\tEnter the number of columns of Matrix 2 :"))
        matrix2 = []
        # print("Enter the entries row wise:")
        for i in range(R1):
            a = []
            for j in range(C1):
                a.append(random.randint(0, 100))
            matrix2.append(a)
        print("\t\t\t\t\t\tMatrix 1 is :", matrix1,
              "\n\t\t\t\t\t\tMatrix 2 is : ", matrix2)

        if (R1 != R2 or C1 != C2):
            print("\t\t\t\t\t\tGiven Matrix cannot be Divided !\n")
            break
        else:
            R = np.divide(matrix1, matrix2)
            print("\t\t\t\t\t\tThe Matrix obtained by Division is : ", R)

    if i == 5:  # !!!!!!!!!!
        break
