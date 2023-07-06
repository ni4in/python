from my_queue import Queue

def hot_potato(names,num):
    play_circle = Queue()
    for item in names:
        play_circle.enqueue(item)


    times = 0
    play = 0

   
    times = 0
    while play_circle.size()!= 1:
        for __ in range(num):
            play_circle.enqueue(play_circle.dequeue())
        play_circle.dequeue()
    return play_circle.items



print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent","Brad"], 7))