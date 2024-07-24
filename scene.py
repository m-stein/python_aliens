class Scene:
    def __init__(self, next_scene=None):
        self.finished = False
        self.next_scene = next_scene
