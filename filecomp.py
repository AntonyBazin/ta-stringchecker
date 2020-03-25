def check_files(file1, file2):
    lst = []
    st = {}
    with open(file1, 'r') as f:
        for line in f:
            lst.append(line)
        st = set(lst)
        lst = []
    with open(file2, 'r') as f:
        for line in f:
            lst.append(line)
    if st.symmetric_difference(set(lst)) == set():
        return True
    else:
        return st.symmetric_difference(set(lst))


if __name__ == '__main__':
    print('Input files\' names:')
    f1 = input()
    f2 = input()
    print(check_files(f1, f2))
