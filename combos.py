# TASK
# Create a function combos, that accepts a single positive integer num (30 > num > 0)
# and returns an array of arrays of positive integers that sum to num.
# Notes:
#     Sub-arrays may or may not have their elements sorted.
#     The order of sub-arrays inside the main array does not matter.
#     For an optimal solution, the following operation should complete within 6000ms.
# Ex. : combos(3) => [ [ 3 ], [ 1, 1, 1 ], [ 1, 2 ] ]


def combos(n):
    set = []
    out = [None] * n

    # index - next location in array
    def subset_combo(start, stop, arr, index):

        if stop == 0:
            set.append(arr[:index])

        for i in range(start, stop + 1):
            arr[index] = i
            subset_combo(i, stop - i, arr, index + 1)

    subset_combo(1, n, out, 0)
    return set




print(combos(3))