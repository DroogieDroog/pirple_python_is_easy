"""
pirple/python/hw10/main.py
Homework Assignment #10

Play around with an imported library
"""

import statistics as stat

def main():
    test_data = [3, -10, 8, 73, -2, -39, 48, 1, 99, -84, -10]
    mean = stat.mean(test_data)
    mode = stat.mode(test_data)
    med = stat.median(test_data)
    std = stat.stdev(test_data)
    var = stat.variance(test_data)

    print ('The sample data is: ')
    print(test_data)
    print()
    print('STATISTICS')
    print('----------')
    print('Mean:    ', mean)
    print('Mode:    ', mode)
    print('Median:  ', med)
    print('Std Dev: ', std)
    print('Variance:', var)

main()