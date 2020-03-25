import time
from parser import Parser


def analyze(filename):
    names = {}
    counter = 0
    parser = Parser()

    with open(filename, 'r') as dt:
        for line in dt:
            res = parser.check_string(line)
            if res:
                counter += 1
                for i in res.items():
                    names[i[0]] = i[1] if i[0] not in names.keys() else names[i[0]] + i[1]
    names = dict(reversed(sorted(names.items(), key=lambda x: x[1])))
    with open('answer_ply.txt', 'w') as ans:
        ans.write('Lines read successfully: ' + str(counter) + '\n')
        ans.writelines(['Variable ' + x + '---' + str(names[x]) + '\n' for x in names.keys()])


if __name__ == '__main__':
    print('Input file name to analyze:')
    start = time.time()
    analyze(input())
    end = time.time()
    with open('timing-ply.txt', 'w') as file:
        file.write(str(end - start))
