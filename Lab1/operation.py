from constants import *


def calculate_operation(first_value: float, second_value: float, operator: str):
    if operator == ADD_OPERATOR:
        return first_value + second_value
    elif operator == SUB_OPERATOR:
        return first_value - second_value
    elif operator == MULT_OPERATOR:
        return first_value * second_value
    elif operator == DIV_OPERATOR:
        return first_value / second_value  # if second_value != 0 else 'Dividing by zero!'
    else:
        raise Exception('unknown operator!')
