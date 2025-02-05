from music21 import converter

score = converter.parse("C:/Users/Ayush/OneDrive/Documents/Audiveris/Double Note Scale/Double Note Scale.mxl")

score.write("midi", fp="C:/Users/Ayush/OneDrive/Documents/Audiveris/Double Note Scale/Double Note Scale.midi")

print("MIDI file created.")
