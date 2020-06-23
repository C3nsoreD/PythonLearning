'''
Find the sum of all the multipes of 3 and 5 below 1000
'''
import numpy as np


def multiples(num):

    numlis = np.arange(1,num)
    # multiples of 3
    x_3, x_5 = 3, 5
    m_3, m_5 = [], []

    for i in numlis:
        if i % x_3 == 0:
            m_3.append(i)

        if i % x_5 == 0:
            m_5.append(i)

    total = m_5 + m_3
    sTotal = set(total)

    # print(sTotal)
    print(sum(sTotal))


def main():
        multiples(1000)



main()
