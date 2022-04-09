from pymusicbox.symbolic.core import Note
from pymusicbox.symbolic import constants


class Chord:
    def __init__(self, base_note, interval_name, interval, length=1, velocity=127):
        self.base_note = base_note

        self.interval_name = interval_name
        if interval is None:
            self.interval = constants.chord_intervals[self.interval_name]
        else:
            self.interval = interval

        self.length = length
        self.velocity = velocity

    def get_notes(self):
        for offset in self.interval:
            pitch = (self.base_note.pitch + offset) % 12
            octave = self.base_note.octave + \
                ((self.base_note.pitch + offset) // 12)

            note = Note(pitch, octave, self.length, self.velocity)
            yield note
