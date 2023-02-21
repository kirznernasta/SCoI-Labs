from even_numbers import generate_list_of_even_numbers
from hello_world import say_hello_world
from operation import calculate_operation

if __name__ == '__main__':
    say_hello_world()
    print('calculate_operation function with arguments 1, 2, "add" returned:', calculate_operation(1, 2, 'add'))
    print('list of even numbers with maximum length 15:', generate_list_of_even_numbers())
