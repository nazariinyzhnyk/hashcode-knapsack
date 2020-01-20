import os


def list_to_int(lst: list) -> list:
    return [int(elem) for elem in lst]


def read_data(path_to_data: str):
    with open(path_to_data) as f:
        line1 = list_to_int(f.readline().split())
        line2 = list_to_int(f.readline().split())
    return line1[0], line1[1], line2


def create_submission(pck, filename):
    with open(os.path.join('data', filename + 'out'), 'w') as f:
        f.write(str(len(pck)) + '\n')
        for i in pck:
            f.write(str(i) + ' ')
        f.write('\n')
