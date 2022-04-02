import numpy as np

from museai.audio.audio_utils import add_audio

from museai.symbolic.symbols import Note, Track


class Instrument:
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate
        self.max_amp = 2000

    def render_note(self, note: Note):
        freq = 55 * pow(2, (note.note / 12))
        t = np.linspace(0, note.length, int(note.length*self.sample_rate))

        data = self.max_amp * note.level * np.sin(2. * np.pi * freq * t)
        return data

    def render_track(self, track: Track):
        data = np.linspace(0, track.length, int(track.length*self.sample_rate))

        for time, note in track.get_timed_notes():
            add_audio(time, data, self.render_note(note), self.sample_rate)

        return data
