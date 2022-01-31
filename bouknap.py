import ctypes
import pathlib
import sys

SHARED_OBJECT = pathlib.Path('./bouknap.so')
if not SHARED_OBJECT.exists():
    print(f'Please compile the "bouknap.c" file into a shared object file:')
    print('\tcc -fPIC -shared -o bouknap.so bouknap.c\n')
    sys.exit(1)

c_library = ctypes.CDLL(str(SHARED_OBJECT.resolve()))


def solve(values: [int], weights: [int], available_quantities: [int], capacity: int) -> [int, [int]]:
    item_count = len(values)
    ParameterArray = ctypes.c_int * item_count

    values_array = ParameterArray(*values)
    weights_array = ParameterArray(*weights)
    available_quantities_array = ParameterArray(*available_quantities)

    solution = [0] * item_count
    solution_array = ParameterArray(*solution)

    optimal_profit = c_library.bouknap(
        item_count,
        values_array,
        weights_array,
        available_quantities_array,
        solution_array,
        capacity
    )

    return optimal_profit, solution_array[:]


if __name__ == '__main__':
    solve(
        values=[9, 2, 1],
        weights=[8, 3, 2],
        available_quantities=[5, 10, 15],
        capacity=27
    )
