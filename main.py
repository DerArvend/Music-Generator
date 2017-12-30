# from io import *
from typing import Callable
import midiutil
import os
from generation import *
from midi_saver import *


def main(output_saver: Callable[[Composition, str], None], output_path=os.getcwd(), blocks_count: int = 4):
    composition = generate_composition(blocks_count)
    output_saver(composition, output_path)


if __name__ == '__main__':
    main(save_to_midi, "D:\\test.mid")
