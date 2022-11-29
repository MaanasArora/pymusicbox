from dataclasses import astuple, dataclass

import numpy as np

from pymusicbox.audio.audio import Audio
from pymusicbox.symbolic.symbols import Note, NoteEvent, Track


@dataclass
class Instrument:
    sample_rate: int = 44100
    max_amp: float = 1e-5

    def render_note(self, note: Note):
        note_length = note.length*self.sample_rate

        freq = 55 * pow(2, (note.note / 12))
        t = np.linspace(0, note.length, int(note_length))

        data = self.max_amp * note.level * np.sin(2. * np.pi * freq * t)
        return Audio(data, self.sample_rate)

    def render_track(self, track: Track):
        audio = Audio.empty(track.length, self.sample_rate)

        for event in track:
            if isinstance(event, NoteEvent):
                audio.add(event.time, self.render_note(event.note))

        return audio


@dataclass
class HarmonicsConfiguration:
    attack: float
    decay: float
    release: float
    sustain_factor: float

    def __iter__(self):
        return iter(astuple(self))

    def apply_rate(self, sample_rate):
        return map(lambda time: int(sample_rate * time), self)


@dataclass
class HarmonicInstrument(Instrument):
    harmonics: HarmonicsConfiguration = None

    def get_harmonic_amps(self, length: float):
        attack, decay, release, sustain_factor = self.harmonics.apply_rate(self.sample_rate)
        sustain = length - (attack + decay + release)

        if sustain < 0:
            raise ValueError("Length too small for harmonics")

        attack_amp = np.linspace(0, 1, attack)
        decay_amp = np.linspace(1, sustain_factor, decay)
        sustain_amp = np.linspace(sustain_factor, sustain_factor, sustain)
        release_amp = np.linspace(sustain_factor, 0, release)

        return np.concatenate([attack_amp, decay_amp, sustain_amp, release_amp])

    def render_note(self, note: Note):
        audio = super().render_note(note)

        audio.waveform *= self.get_harmonic_amps(note.length * self.sample_rate)
        return audio