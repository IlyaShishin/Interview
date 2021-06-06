class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


brackets = {
    ')': '(',
    ']': '[',
    '}': '{',
}


def balance_checker(text):
    s = Stack()
    for item in text:
        # если символ открывающий
        if item in brackets.values():
            s.push(item)
        # если символ закрывающий
        elif item in brackets:
            if s.isEmpty():
                return "Несбалансированно"
            elif brackets[item] != s.pop():
                return "Несбалансированно"

    return "Сбалансированно"


print(balance_checker('(((([{}]))))'))
print(balance_checker('[([])((([[[]]])))]{()}'))
print(balance_checker('{{[()]}}'))
print(balance_checker('}{}'))
print(balance_checker('{{[(])]}}'))
print(balance_checker('[[{())}]'))
