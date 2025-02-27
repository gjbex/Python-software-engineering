#!/usr/bin/env python
import argparse
from typing import Protocol


class SoundMaker(Protocol):

    def make_sound(self) -> None:
        pass


class Duck:

    def make_sound(self) -> None:
        print('quack')


class AlarmClock:

    def make_sound(self) -> None:
        print('ring-ring')


def sound_maker_factory(sound_type: str) -> SoundMaker:
    if sound_type == 'duck':
        return Duck()
    elif sound_type == 'alarm':
        return AlarmClock()
    else:
        raise ValueError(f'unknown sound type: {sound_type}')


def sound_repeater(sound_maker: SoundMaker, nr_repeats: int) -> None:
    for _ in range(nr_repeats):
        sound_maker.make_sound()


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='sound maker')
    arg_parser.add_argument('--type', choices=['duck', 'alarm'],
                            help='sound source')
    arg_parser.add_argument('--n', type=int, default=1,
                            help='number of sounds to make')
    options = arg_parser.parse_args()
    sound_maker: SoundMaker = sound_maker_factory(options.type)
    sound_repeater(sound_maker, options.n)
