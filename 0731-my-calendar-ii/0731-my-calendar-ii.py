class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.overlaps = []

    def book(self, startTime: int, endTime: int) -> bool:

        for s,e in self.overlaps:
            if startTime < e and endTime > s:
                return False

        for s,e in self.bookings:
            if startTime < e and endTime > s:
                self.overlaps.append([max(s,startTime),min(e,endTime)])
        
        self.bookings.append([startTime,endTime])
        return True

        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)