class Printer():
    def __init__(self, ppm) -> None:
        self.ppm = ppm
        self.current_task = None
        self.time_remaining = 0
    
    def tick(self):
        if self.current_task != None:
            self.time_remaining -= 1
            if self.time_remaining <=0:
                self.current_task = None 
    
    def is_busy(self):
        if self.current_task != None:
            return True
        else:
            return False


    


