from music_structures import Note


def get_midi_note_code(note: Note, octave: int) -> int:
    return 12 * (octave + 1) + note.value
