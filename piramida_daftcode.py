# Masz za zadnie znaleźć ścieżkę w trójkącie zbudowanym z liczb od 0 do 9 (od górnego wierzchołka do podstawy
# trójkąta) z najmniejszą sumą liczb oraz sumę liczb w tej ścieżce. Wychodząc z dowolnej liczby w każdym wierszu
# trójkąta zawsze możesz pójść na dół, w lewo lub w prawo (poza ostatnim wierszem, którego cyfra kończy ścieżkę).
# Reprezentacje ścieżki uzyskujemy sklejając wszystkie cyfry ze ścieżki ze sobą.

import os
from copy import deepcopy

def import_pyramid(file):
    f = open(file, 'r')
    lines = f.readlines()
    lines_list = []
    for line in lines:
        tmp = [int(i) for i in line.strip().split()]
        lines_list.append(tmp)
    return lines_list

def sum_min_path(pyramid):
    prev_pyramid = deepcopy(pyramid)
    rvd_pyramid = pyramid[::-1]

    for ind_ln, ln in enumerate(rvd_pyramid[1:]):
        for ind_it, item in enumerate(ln):
            tmp_1 = item + rvd_pyramid[ind_ln][ind_it]
            tmp_2 = item + rvd_pyramid[ind_ln][ind_it+1]
            if tmp_1 <= tmp_2:
                rvd_pyramid[ind_ln + 1][ind_it] = tmp_1
            else:
                rvd_pyramid[ind_ln + 1][ind_it] = tmp_2

    sum_on_shortest_path = rvd_pyramid[-1][0]
    path = find_path(pyramid, prev_pyramid)
    path = [str(i) for i in path]
    path = ''.join(path)
    return sum_on_shortest_path, path

def find_path(prmd_after, prmd_before):

    path = [prmd_before[0][0]]
    indx = 0
    for enum, row in enumerate(prmd_after[:-1]):
        prev_val = prmd_after[enum][indx] - prmd_before[enum][indx]
        indx = prmd_after[enum+1].index(prev_val, indx, indx+2)
        path.append(prmd_before[enum+1][indx])

    return path

pyramid_v_easy = import_pyramid('1-very_easy.txt')
pyramid_easy = import_pyramid('2-easy.txt')
pyramid_medium = import_pyramid('3-medium.txt')

pyra = import_pyramid('2-easy.txt')


test_prmd= [[9], [2, 7], [2,9,1], [2,6,8,6]]
tst = [[3], [6,4], [5,2,7], [9,1,8,6]]
print(sum_min_path(test_prmd))
print(sum_min_path(pyramid_v_easy))
print(sum_min_path(pyramid_easy))
print(sum_min_path(pyramid_medium))
print(sum_min_path(tst))
