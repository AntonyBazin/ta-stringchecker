import AppClass
import time


def analyze(filename):
    checker = AppClass.AppClass()
    with open(filename, 'r') as dt:
        for line in dt:
            checker.CheckString(line)

    cnt = checker.get_lines_read()
    dct = dict(reversed(sorted(checker.get_dict().items(), key=lambda x: x[1])))

    with open('answer_smc.txt', 'w') as ans:
        ans.write('Lines read successfully: ' + str(cnt) + '\n')
        ans.writelines(['Variable ' + x + '---' + str(dct[x]) + '\n' for x in dct.keys()])


if __name__ == '__main__':
    print('Input file name to analyze:')
    start = time.time()
    analyze(input())
    end = time.time()
    with open('timing-smc.txt', 'w') as file:
        file.write(str(end - start))
