import numpy


def add_audio(t, data, data_to_add, sample_rate):
    t_start = int(t * sample_rate)
    t_end = t_start + len(data_to_add)

    if t_end + 1 > len(data):
        t_end = len(data) - 1

        data[t_start:t_end] = data_to_add[:t_end-t_start]
    else:
        data[t_start:t_end] += data_to_add
