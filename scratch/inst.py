from scipy import io as sio
from symbolic.symbolic import Note, Track

from synth.instrument import Instrument

inst = Instrument()

track = Track([0.5, 1, 1.5, 2, 2.5, 3, 3.5],
              [Note(n, length=0.4) for n in [50, 52, 54, 50, 50, 52, 54]])

data = inst.render_track(track)
sio.wavfile.write('output.wav', inst.sample_rate, data.astype(np.int16))
