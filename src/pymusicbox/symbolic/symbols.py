import numpy as np


NOTES = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
NOTES_PITCH = {p: i + 1 for i, p in enumerate(NOTES)}


class Note:
    def __init__(self, pitch, octave, length=1, velocity=127):
        self.pitch = pitch
        self.octave = octave
        self.note = self.get_note()

        self.length = length

        self.velocity = velocity
        self.level = self.velocity / 127

    def get_note(self):
        note = NOTES_PITCH[self.pitch.upper()] + 12 * self.octave
        return note


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
