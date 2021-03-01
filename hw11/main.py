"""
pirple/python/hw11/main.py
Homework Assignment #11

Play around with error handling
"""

import statistics as stat

def stats_table(test_data, mean, mode, med, std, var):
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


def calculate_stats(test_data):
    status = 'PASS'

    try:
        mean = stat.mean(test_data)
    except TypeError:
        status = 'FAIL'
        print('You have strings in your input, or have not passed in a list of numbers')
        print('Your input: ', test_data)
    finally:
        if status == 'PASS':
            mode = stat.mode(test_data)
            med = stat.median(test_data)
            std = stat.stdev(test_data)
            var = stat.variance(test_data)
        else:
            mean = 0
            mode = 0
            med = 0
            std = 0
            var = 0

    return status, mean, mode, med, std, var


def main(test_data):
    status, mean, mode, med, std, var = calculate_stats(test_data)

    if status == 'PASS':
        stats_table(test_data, mean, mode, med, std, var)
    else:
        print('Aborting stats table creation . . .')
    print()

main([3, -10, 8, 73, -2, -39, 48, 1, 99, -84, -10])
main(['3', -10, 8, 73, -2, '-39', 48, 1, 99, -84, -10])
main(['three', -10, 8, 73, -2, 'OK', 48, 1, 99, -84, -10])
main(45)
