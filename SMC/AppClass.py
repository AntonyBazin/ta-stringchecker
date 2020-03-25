import AppClass_sm


class AppClass:

    def __init__(self):
        self._fsm = AppClass_sm.AppClass_sm(self)
        self._is_acceptable = True
        self._name = ''
        self._dict = {}
        self._local_dict = {}
        self._count = 0
        self._fsm.enterStartState()

        # Uncomment to see debug output.
        # self._fsm.setDebugFlag(True)

    def CheckString(self, string):
        self._is_acceptable = True
        self._name = ''
        self._local_dict = {}
        if string == '':
            self._is_acceptable = False
        for c in string:
            if not self._is_acceptable:
                break
            if c == '<':
                self._fsm.LArr()
            elif c is '-':
                self._fsm.Dash()
            elif c is '!':
                self._fsm.Exclam()
                self._name += c
            elif c in r'^|&':
                self._fsm.Sign()
            elif c is '#':
                self._fsm.Htag()
            elif c.isdecimal():
                self._fsm.Number()
                self._name += c
            elif c.isalpha():
                self._fsm.Letter()
                self._name += c
            elif c is '\n':
                self._fsm.EOS()
            else:
                self._fsm.Unknown()
        if not self._is_acceptable:
            return False
        self._count += 1

        return self._is_acceptable

    def Acceptable(self):
        self._is_acceptable = True

    def Unacceptable(self):
        self._is_acceptable = False

    def length_available(self):
        return len(self._name) < 17

    def add_var(self):
        if self._name not in self._local_dict.keys():
            self._local_dict[self._name] = 1
        else:
            self._local_dict[self._name] += 1
        self._name = ''

    def push_vars(self):
        for i in self._local_dict.keys():
            if i not in self._dict.keys():
                self._dict[i] = self._local_dict[i]
            else:
                self._dict[i] += self._local_dict[i]

    def get_lines_read(self):
        return self._count

    def get_dict(self):
        return self._dict
