import time
from parser import Parser


def analyze(filename):
    names = {}
    counter = 0
    parser = Parser()

    with open(filename, 'r') as dt:
        cnt = 0
        with open('timing-ply.txt', 'w') as out:
            out.write('# amount TIME\n')
        start = time.time()
        for line in dt:
            cnt += 1
            res = parser.check_string(line)
            if res:
                counter += 1
                for i in res.items():
                    names[i[0]] = i[1] if i[0] not in names.keys() else names[i[0]] + i[1]
            if not cnt % 100000:
                end = time.time()
                with open('timing-ply.txt', 'a') as out:
                    out.write(str(cnt / 100000) + ' ' + str(end - start) + '\n')
    names = dict(reversed(sorted(names.items(), key=lambda x: x[1])))
    with open('answer_ply.txt', 'w') as ans:
        ans.write('Lines read successfully: ' + str(counter) + '\n')
        ans.writelines(['Variable ' + x + '---' + str(names[x]) + '\n' for x in names.keys()])


if __name__ == '__main__':
    print('Input file name to analyze:')
    analyze(input())
    # with open('timing-ply.txt', 'w') as file:
    #     file.write(str(end - start))
