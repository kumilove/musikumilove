from midi2audio import FluidSynth

midi_file = 'miditest/Mizore and Ririka Oboe Duet.mid'

mp3_file = 'miditest/Mizore and Ririka Oboe Duet.mp3'

fs = FluidSynth('soundfont/FluidR3_GM.sf2')

# Convert MIDI to MP3
fs.midi_to_audio(midi_file, mp3_file)