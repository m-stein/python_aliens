class Animation:
    def __init__(self, frame_size, num_frames, frame_duration, loop=True):
        self.frame = 0
        self.frame_size = frame_size
        self.frame_duration = frame_duration
        self.num_frames = num_frames
        self.frame_time = 0.
        self.loop = loop
        self.finished = False

    def frame_rectangle(self):
        return self.frame * self.frame_size[0], 0, self.frame_size[0], self.frame_size[1]

    def update(self, delta_time):
        if self.finished:
            return

        self.frame_time += delta_time
        frame = self.frame + int(self.frame_time / self.frame_duration)
        if not self.loop and frame >= self.num_frames:
            self.frame = self.num_frames - 1
            self.finished = True
        else:
            self.frame = frame % self.num_frames
        self.frame_time %= self.frame_duration
