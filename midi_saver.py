from typing import List

from music_structures import Composition
from midiutil import MIDIFile
from utils import *

chord_octave = 3
bass_octave = 1
lead_octave = 5

chord_channel = 0
lead_channel = 1
bass_channel = 2

chord_volume = 70
lead_volume = 100

track = 0
channel = 0
time = 0  # In beats
duration = 2  # In beats
tempo = 100  # In BPM
volume = 100  # 0-127, as per the MIDI standard


def save_to_midi(composition: Composition, output_path: str):
    midi = MIDIFile(3)
    midi.addTempo(track, time, tempo)
    for i, block in enumerate(composition.rythm):
        for j, chord in enumerate(block):
            for note in chord.notes:
                note_code = get_midi_note_code(note, chord_octave)
                midi.addNote(track, chord_channel, note_code,
                             time + j * duration + i * len(block) * duration, duration,
                             chord_volume)
    for i, note in enumerate(composition.lead):
        if note is not None:
            note_code = get_midi_note_code(note, lead_octave)
            midi.addNote(track, lead_channel, note_code, time + i * duration / 4, duration / 4, lead_volume)

    with open(output_path, "wb") as output_file:
        midi.writeFile(output_file)
