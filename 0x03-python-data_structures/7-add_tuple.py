#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum0 = sum(tuple_a[:1] + tuple_b[:1])
    sum1 = sum(tuple_a[1:2] + tuple_b[1:2])
    return (sum0, sum1)
