# pymusicbox

A library with toolkits for music synthesis and analysis. This is a work in progress.

## Current Features

- Symbolic language to represent notes and tracks
- Create instruments with sine oscilators and harmonics

## Installation

```pip install pymusicbox```

## Example Usage

```python
from pymusicbox.synth.instrument.oscillator import HarmonicOscillator, HarmonicsConfiguration
from pymusicbox.symbolic.symbols import Note, NoteEvent, Track

track = Track(events=[
  NoteEvent(time=0, note=Note(pitch='C', octave=3, length=1),
  NoteEvent(time=1, note=Note(pitch='D', octave=3, length=1),
  NoteEvent(time=2, note=Note(pitch='E', octave=3, length=1),
)

harmonics = HarmonicsConfiguration(attack=0.2, decay=0.4, release=0.2, sustain_factor=0.6)
oscillator = HarmonicOscillator(harmonics)
audio = oscillator.render_track(track)
audio.write('output.wav')
```
