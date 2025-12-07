from collections import deque

class RateLimiter:
    def __init__(self, capacity, window):
        self.capacity = capacity
        self.window = window
        self.q = deque()

    def allow(self, t):
        boundary = t - self.window

        # remove all timestamps <= boundary
        while self.q and self.q[0] <= boundary:
            self.q.popleft()

        # now the window is (t - window, t]
        if len(self.q) < self.capacity:
            self.q.append(t)
            return True

        return False
        
        # Reject everything else
        return False



        return False
