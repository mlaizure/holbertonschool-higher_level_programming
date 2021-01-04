#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    quo_list = []
    for idx in range(list_length):
        try:
            quotient = my_list_1[idx] / my_list_2[idx]
        except (ValueError, TypeError):
            print("wrong type")
            quotient = 0
        except ZeroDivisionError:
            print("division by 0")
            quotient = 0
        except IndexError:
            print("out of range")
            quotient = 0
        finally:
            quo_list.append(quotient)
    return quo_list
