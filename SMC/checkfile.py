import AppClass
import time


def analyze(filename):
    checker = AppClass.AppClass()
    with open('timing-smc.txt', 'w') as out:
        out.write('# amount TIME\n')
    with open(filename, 'r') as dt:
        cnt = 0
        start = time.time()
        for line in dt:
            cnt += 1
            checker.CheckString(line)
            if not cnt % 100000:
                end = time.time()
                with open('timing-smc.txt', 'a') as out:
                    out.write(str(cnt / 100000) + ' ' + str(end - start) + '\n')

    cnt = checker.get_lines_read()
    dct = dict(reversed(sorted(checker.get_dict().items(), key=lambda x: x[1])))

    with open('answer_smc.txt', 'w') as ans:
        ans.write('Lines read successfully: ' + str(cnt) + '\n')
        ans.writelines(['Variable ' + x + '---' + str(dct[x]) + '\n' for x in dct.keys()])


if __name__ == '__main__':
    print('Input file name to analyze:')
    analyze(input())

