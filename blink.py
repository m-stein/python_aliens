class Blink:
    def __init__(self, period, start_value):
        self.value = start_value
        self.period = period
        self.timeout = self.period

    def update(self, delta_time):
        if self.timeout > delta_time:
            self.timeout -= delta_time
        else:
            self.timeout = self.period
            self.value = not self.value
