class Evaluate:
    def __init__(self, cap):
        self.top = -1
        self.cap = cap
        self.array = []

    def isEmpty(self):
        return True if self.top == -1 else False

    def peek(self):
        return self.array[-1]

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "none"

    def push(self, op):
        self.top += 1
        self.array.append(op)

    def evaluatePostfix(self, exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                p = self.pop()
                q = self.pop()
                self.push(str(eval(q + i + p)))

        return int(self.pop())

exp = "231*+9-10+"
obj = Evaluate(len(exp))
print(obj.evaluatePostfix(exp))