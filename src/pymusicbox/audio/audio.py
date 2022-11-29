from dataclasses import dataclass

import numpy as np


@dataclass
class Audio:
    waveform: np.ndarray[np.float64]
    sample_rate: int

    @classmethod
    def empty(length, sample_rate):
        return Audio(np.zeros((length,)), sample_rate)

    def add(self, time, audio):
        t_start = int(time * self.sample_rate)
        t_end = t_start + len(audio)

        self.waveform[t_start:t_end] += audio.waveform

    def duration(self):
        return len(self.waveform) / self.sample_rate

    def __len__(self):
        return len(self.waveform)
