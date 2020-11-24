class Node:

    def __init__(self, data):
        self.data = data
        self.val = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            pass

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

root = Node(17)
n = int(input("range: "))
print("Enter elements to add:")
for i in range(n):
    root.insert(int(input()))

root.printTree()
