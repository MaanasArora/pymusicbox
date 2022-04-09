class MusicGen:
    def __init__(self, tempo=80):
        self.tempo = tempo

    def get_beat_length(self):
        return 60 * (1 / self.tempo)