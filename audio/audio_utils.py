import numpy as np


def add_audio(t, data, data_to_add, sample_rate):
    t_start = int(t * sample_rate)
    t_end = t_start + len(data_to_add)

    data_to_add[t_start:t_end] += data
