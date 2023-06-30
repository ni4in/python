class Stack():
    def __init__(self) -> None:
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)


def main():
    s = Stack()
    print(s.is_empty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.push(8.4))
    print(s.pop())


if __name__ == "__main__":
    main()