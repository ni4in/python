import random

class Task():
    def __init__(self, time) -> None:
        self.timestamp = time
        self.pages = random.randrange(1,21)
    
    def get_timestamp(self):
        return self.timestamp
    def get_pages(self):
        return self.pages
    def get_wait_time(self, current_time):
        return current_time - self.timestamp


def main():
    t = Task(5)
    print(f"The task is created with pages {t.get_pages()} at time 5 and waiting time at 10s is {t.get_wait_time(10)}")

if __name__ == "__main__":
    main()
