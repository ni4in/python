class Queue():
    def __init__(self) -> None:
        self.items = []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def size(self):
        return len(self.items)

def main():
    queue = Queue()
    queue.enqueue("Hello")
    queue.enqueue("dog")
    queue.enqueue(3)
    queue.dequeue()
    print(queue.items)
    print(queue.size())

if __name__ == "__main__":
    main()


