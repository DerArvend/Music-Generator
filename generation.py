from random import choice
from typing import Callable, Dict

from music_structures import *

scale_weights: Dict[Scale, List[int]] = {
    Scale.Minor: [0, 2, 3, 5, 7, 8, 10],
    Scale.Major: [0, 2, 4, 5, 7, 9, 11],
    Scale.MinorPentatonic: [0, 3, 5, 7, 10],
    Scale.MajorPentatonic: [0, 2, 4, 7, 9]
}


def get_sequence_generator(scale: Scale) -> Callable[[int], List[Degree]]:
    degrees = list(Degree)
    diminished_degree = Degree.II if scale == Scale.Minor else Degree.VII
    degrees.remove(diminished_degree)

    def generator(sequence_length: int) -> List[Degree]:
        result: List[Degree] = [Degree.T]
        for i in range(sequence_length - 2):
            degree = choice([d for d in degrees if not result.__contains__(d)])
            result.append(degree)
        result.append(choice([Degree.S, Degree.D]))
        return result

    return generator


def get_note_by_degree(tonic: Note, degree: Degree, scale: Scale) -> Note:
    note_value = (tonic.value + scale_weights[scale][degree.value]) % 12
    return Note(note_value)


def get_chord_by_degree(degree: Degree, scale: Scale, scale_tonic: Note, chord_size: int = 3) -> Chord:
    result = []
    for i in range(chord_size):
        next_note = get_note_by_degree(scale_tonic, Degree((degree.value + i * 2) % 7), scale)
        result.append(next_note)
    return Chord(result)


def get_chords(degrees: List[Degree], scale: Scale, tonic: Note) -> List[Chord]:
    result = []
    for degree in degrees:
        result.append(get_chord_by_degree(degree, scale, tonic))

    return result


def generate_lead(degrees: List[Degree], scale: Scale, tonic: Note) -> List[Note]:
    result: List[Note] = []
    step = choice([1, -1])

    for n, degree in enumerate(degrees):
        next_note_degree = degree
        for i in range(4):
            if n % 2 == 0 and i >=2:
                result.append(None)
                continue
            result.append(get_note_by_degree(tonic, next_note_degree, scale))
            next_note_degree = Degree((next_note_degree.value + step) % 7)


    return result


def generate_composition(blocks_count: int) -> Composition:
    scale = choice([Scale.Minor, Scale.Major])
    tonic = choice(list(Note))
    composition = Composition(scale, tonic)
    seq_gen = get_sequence_generator(scale)
    for i in range(blocks_count):
        degrees = seq_gen(blocks_count)
        composition.degrees.append(degrees)
        composition.rythm.append(get_chords(degrees, scale, tonic))
        composition.lead.extend(generate_lead(degrees, scale, tonic))

    return composition
