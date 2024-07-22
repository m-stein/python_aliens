class Blink:
    def __init__(self, period, start_value):
        self.start_value = start_value
        self.period = period
        self.timeout = None
        self.value = None
        self.reset()

    def update(self, delta_time):
        if self.timeout > delta_time:
            self.timeout -= delta_time
        else:
            self.timeout = self.period
            self.value = not self.value

    def reset(self):
        self.timeout = self.period
        self.value = self.start_value
