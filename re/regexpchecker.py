import re
import sys
import time


def analyze(filename):
    names_dict = {}

    regexp = re.compile(r'<-[!a-zA-Z][a-zA-Z\d]{0,15}([&|^]([!a-zA-Z][a-zA-Z\d]{0,15}))*#\n')
    word = re.compile(r'[!a-zA-Z][a-zA-Z\d]{0,15}')
    counter = 0

    with open(filename, 'r') as dt:
        for line in dt:
            if regexp.fullmatch(line):
                counter += 1
                for name in list(reversed(word.findall(line))):
                    if name not in names_dict.keys():
                        names_dict[name] = 1
                    else:
                        names_dict[name] += 1
    names_dict = dict(reversed(sorted(names_dict.items(), key=lambda x: x[1])))
    with open('answer_re.txt', 'w') as ans:
        ans.write('Lines read successfully: ' + str(counter) + '\n')
        ans.writelines(['Variable ' + x + '---' + str(names_dict[x]) + '\n' for x in names_dict.keys()])


if __name__ == '__main__':
    print('Input file name to analyze:')
    start = time.time()
    analyze(input())
    end = time.time()
    with open('timing-re.txt', 'w') as file:
        file.write(str(end - start))
