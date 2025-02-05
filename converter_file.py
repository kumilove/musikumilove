from music21 import converter

score = converter.parse("./testcases/Mizore and Ririka Oboe Duet.mxl")

score.write("midi", fp="./testcases/mxl_to_midi/Mizore and Ririka Oboe Duet.midi")

print("MIDI file created.")
