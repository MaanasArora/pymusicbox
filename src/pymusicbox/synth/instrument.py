from collections import namedtuple

import numpy as np

from pymusicbox.audio.audio_utils import add_audio
from pymusicbox.symbolic.symbols import Note, Track


HarmonicsConfiguration = namedtuple("HarmonicsConfiguration", ["attack", "decay", "release", "sustain"])


class Instrument:
    def __init__(self, sample_rate: int = 44100, harmonics: HarmonicsConfiguration = None):
        self.sample_rate = sample_rate
        self.max_amp = 9000

        self.harmonics = harmonics

    def get_harmonics(self, length: float):
        attack, decay, release, sustain_factor = self.harmonics
        sustain = length - (attack + decay + release)

        attack_amp = np.linspace(0, 1, int(attack * self.sample_rate))
        decay_amp = np.linspace(1, sustain_factor, int(decay * self.sample_rate))
        sustain_amp = np.linspace(sustain_factor, sustain_factor, int(sustain * self.sample_rate))
        release_amp = np.linspace(self.sustain_factor, 0, int(release * self.sample_rate))

        return np.concatenate([attack_amp, decay_amp, sustain_amp, release_amp])

    def render_note(self, note: Note):
        freq = 55 * pow(2, (note.note / 12))
        t = np.linspace(0, note.length, int(note.length*self.sample_rate))

        data = self.max_amp * note.level * np.sin(2. * np.pi * freq * t)
        if self.harmonics is not None:
            data *= self.get_harmonics(note.length)

        return data

    def render_track(self, track: Track):
        data = np.zeros((int(track.length*self.sample_rate),))

        for time, note in track.get_timed_notes():
            add_audio(time, data, self.render_note(note), self.sample_rate)

        return data
