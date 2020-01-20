import os
from utils import read_data, create_submission


def knapsack01(max_weight, items):
    opt_solution = [[0 for i in range(max_weight + 1)] for j in range(len(items[0]))]
    # TODO:: create a solution that uses only 2 rows - it should be optimal and fit into memory
    # opt_solution = [[0 for i in range(max_weight + 1)] for j in range(2)]
    for i in range(len(items[0])):
        print(i)
        for j in range(max_weight + 1):
            if items[0][i] > j:
                opt_solution[i][j] = opt_solution[i-1][j]
            else:
                opt_solution[i][j] = max(opt_solution[i-1][j], opt_solution[i-1][j-items[0][i]] + items[1][i])
    packed = []
    j = max_weight
    for i in range(len(items[0])-1, -1, -1):
        if i == 0 and opt_solution[i][j] != 0:
            packed.insert(0, i)
        if opt_solution[i][j] != opt_solution[i-1][j]:
            packed.insert(0, i)
            j -= items[0][i]
    print('Max value is ', opt_solution[len(items[0]) - 1][max_weight])
    return packed


def main():
    files_to_process = os.listdir('data')
    for file_to_process in files_to_process:
        if file_to_process == 'd_quite_big.in':  # FIXME:: delete testing condition
            max_order, types, slices = read_data(os.path.join('data', file_to_process))
            print(max_order, types, slices)
            packed = knapsack01(max_order, [slices, slices])
            print(packed)
            create_submission(packed, file_to_process)


if __name__ == '__main__':
    main()
