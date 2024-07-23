class LinearFader:
    def __init__(self, start, end, duration):
        self.duration = duration
        self.start = start
        self.end = end
        self.value = start
        self.time = 0.
        self.finished = False

    def update(self, delta_time):
        if self.time <= self.duration:
            self.time += delta_time
            self.value = self.end * self.time / self.duration
        else:
            self.finished = True
