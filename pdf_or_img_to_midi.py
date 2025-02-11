import pdfplumber
from midiutil import MIDIFile
import pytesseract
from PIL import Image
import os
import sys

def extract_notes(text):
    return [note.strip() for line in text.split("\n") for note in line.split() if note.strip()]

def extract_notes_from_pdf(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            return extract_notes("\n".join(page.extract_text() or "" for page in pdf.pages))
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return []

def extract_notes_from_image(image_path):
    try:
        return extract_notes(pytesseract.image_to_string(Image.open(image_path)))
    except Exception as e:
        print(f"Error reading image: {e}")
        return []

def note_to_midi_pitch(note):
    note_map = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11}
    try:
        return 12 * (int(note[-1]) + 1) + note_map[note[:-1]]
    except (KeyError, ValueError, IndexError):
        return None

def create_midi_file(notes, output_path):
    midi = MIDIFile(1)
    midi.addTrackName(0, 0, "Track 1")
    midi.addTempo(0, 0, 120)

    for time, note in enumerate(notes):
        if (pitch := note_to_midi_pitch(note)) is not None:
            midi.addNote(0, 0, pitch, time, 1, 100)

    with open(output_path, "wb") as output_file:
        midi.writeFile(output_file)

def convert_to_midi(input_path, midi_filename):
    file_ext = os.path.splitext(input_path)[1].lower()
    extract_function = extract_notes_from_pdf if file_ext == ".pdf" else extract_notes_from_image if file_ext in [".png", ".jpg", ".jpeg"] else None

    if not extract_function:
        print(f"Unsupported file type: {file_ext}")
        return

    if (notes := extract_function(input_path)):
        create_midi_file(notes, os.path.join(os.path.dirname(__file__), midi_filename))
        print(f"Successfully created MIDI file: {midi_filename}")
    else:
        print("No valid notes found in the input file.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pdf_or_img_to_midi.py <input_file_path> <output_midi_filename>")
    else:
        convert_to_midi(sys.argv[1], sys.argv[2])
