class LinearFader:
    def __init__(self, start, end, duration):
        self.duration = duration
        self.start = start
        self.end = end
        self.value = start
        self.time = 0.
        self.finished = False

    def update(self, delta_time):
        if self.finished:
            return
        if self.duration - self.time > delta_time:
            self.time += delta_time
            self.value = self.start + (self.end - self.start) * self.time / self.duration
        else:
            self.finished = True
            self.value = self.end
