class Scene:
    def __init__(self):
        self.frames = []

    def add_frame(self, frame):
        self.frames.append(frame)

    def add_frames(self, frames):
        self.frames.extend(frames)

    def start_ts(self):
        return self.frames[0].timestamp

    def end_ts(self):
        return self.frames[-1].timestamp
