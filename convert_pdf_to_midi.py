import pdfplumber
from midiutil import MIDIFile
import pytesseract
from PIL import Image
import os

def extract_notes_from_pdf(pdf_path):
    notes = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    lines = text.split('\n')
                    for line in lines:
                        line_notes = [note.strip() for note in line.split() if note.strip()]
                        notes.extend(line_notes)
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return notes

def extract_notes_from_image(image_path):
    notes = []
    try:
        text = pytesseract.image_to_string(Image.open(image_path))
        lines = text.split('\n')
        for line in lines:
            line_notes = [note.strip() for note in line.split() if note.strip()]
            notes.extend(line_notes)
    except Exception as e:
        print(f"Error reading image: {e}")
    return notes

def create_midi_file(notes, output_path):
    midi = MIDIFile(1)
    track = 0
    time = 0
    channel = 0
    volume = 100
    midi.addTrackName(track, time, "Track 1")
    midi.addTempo(track, time, 120)

    for note in notes:
        pitch = note_to_midi_pitch(note)
        if pitch is not None:
            midi.addNote(track, channel, pitch, time, 1, volume)
            time += 1

    with open(output_path, "wb") as output_file:
        midi.writeFile(output_file)

def note_to_midi_pitch(note):
    note_mapping = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11}
    try:
        if len(note) < 2:
            return None
        base_note = note[:-1]
        octave = int(note[-1])
        pitch = 12 * (octave + 1) + note_mapping[base_note]
        return pitch
    except (KeyError, ValueError):
        return None

def convert_to_midi(input_path, midi_filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(script_dir, "mxl_to_midi")
    os.makedirs(output_folder, exist_ok=True)  
    midi_path = os.path.join(output_folder, midi_filename)
    ext = os.path.splitext(input_path)[1].lower()
    if ext == '.pdf':
        notes = extract_notes_from_pdf(input_path)
    elif ext in ['.png', '.jpg', '.jpeg']:
        notes = extract_notes_from_image(input_path)
    else:
        print(f"Unsupported file type: {ext}")
        return
    if notes:
        create_midi_file(notes, midi_path)
        print(f"Successfully created MIDI file: {midi_path}")
    else:
        print("No valid notes found in the input file.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python convert_pdf_to_midi.py <input_file_path> <output_midi_path>")
    else:
        input_file_path = sys.argv[1]
        output_midi_path = sys.argv[2]
        convert_to_midi(input_file_path, output_midi_path)
