def number_sum(n):
    assert n>=0, 'n must be greater than zero'

    if n == 0:
        return 0
    else:
        return n + number_sum(n-1)

"""
if __name__ == '__main__':
    from timeit import Timer
    t = Timer('number_sum(30)', 'from __main__ import number_sum')
    print('Time: ', t.timeit()) ##Time:  5.184385329
"""

cache = {0: 0}
def memo_number_sum(n):
    assert n>=0, 'n must be greater than zero'

    if n in cache:
        return cache[n]
    else:
        res = n + memo_number_sum(n-1)
        cache[n] = res
        return res


if __name__ == '__main__':
    from timeit import Timer
    #t = Timer('memo_number_sum(30)', 'from __main__ import memo_number_sum') ##Time:  0.18827976000000002
    t = Timer('memo_number_sum(300)', 'from __main__ import memo_number_sum') ##Time:  0.181029102
    print('Time: ', t.timeit()) 