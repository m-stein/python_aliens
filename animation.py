class Animation:
    """Manages an animation using a sprite sheet."""

    def __init__(self, frame_size, num_frames, frame_duration):
        """Initialize animation to first frame."""
        self.frame = 0
        self.frame_size = frame_size
        self.frame_duration = frame_duration
        self.num_frames = num_frames
        self.frame_time = 0.

    def frame_rectangle(self):
        """Obtain the source rectangle of the current frame."""
        return self.frame * self.frame_size.x, 0, self.frame_size.x, self.frame_size.y

    def update(self, delta_time):
        """Update internal state to elapsed time since the last call."""
        self.frame_time += delta_time
        self.frame = (self.frame + int(self.frame_time / self.frame_duration)) % self.num_frames
        self.frame_time %= self.frame_duration