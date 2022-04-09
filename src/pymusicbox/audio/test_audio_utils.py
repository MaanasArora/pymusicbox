import pytest

import numpy as np
from scipy import signal

from pymusicbox.audio.audio_utils import add_audio


def test_add_audio():
    sr = 44100

    base_lengths = 2, 4, 5, 8, 9
    add_lengths = 1, 4, 3, 3, 1
    add_times = 1, 0, 2, 1, 7

    for base_length, add_length, t in zip(base_lengths, add_lengths, add_times):
        base_audio = signal.sawtooth(np.linspace(0, base_length, base_length*sr))
        append_audio = signal.square(np.linspace(0, add_length, add_length*sr))

        add_audio(t, base_audio, append_audio, sample_rate=sr)