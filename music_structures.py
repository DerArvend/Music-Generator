from enum import Enum
from typing import List


class Note(Enum):
    C, Db, D, Eb, E, F, Gb, G, Ab, A, Bb, B = range(12)


class Scale(Enum):
    Major, Minor, MinorPentatonic, MajorPentatonic = range(4)


class Degree(Enum):
    T, II, III, S, D, VI, VII = range(7)


class Composition:
    def __init__(self, scale: Scale, tonic: Note):
        self.rythm: List[List[Chord]] = []
        self.lead: List[Note] = []
        self.degrees: List[List[Degree]] = []
        self.scale = scale
        self.tonic = tonic


class Chord:
    def __init__(self, notes: List[Note]):
        self.notes = notes
