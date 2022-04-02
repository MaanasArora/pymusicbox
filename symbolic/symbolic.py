import numpy as np


class Note:
    def __init__(self, note, length=1, velocity=127):
        self.note = note
        self.length = length
        self.velocity = velocity
        self.level = self.velocity / 127


class Track:
    def __init__(self, times, notes, length=None):
        self.times = times
        self.notes = notes

        if length is None:
            self.length = self.get_length()

    def get_length(self):
        max_indx = np.argmax(self.times)

        max_time = self.times[max_indx]
        max_note_length = self.notes[max_indx].length

        return max_time + max_note_length

    def get_timed_notes(self):
        for i in range(len(self.times)):
            yield self.times[i], self.notes[i]
