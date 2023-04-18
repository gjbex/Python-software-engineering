#!/usr/bin/env python
import argparse

class Duck:

    def quack(self):
        print('quack')


class AlarmClock:

    def make_sound(self):
        print('ring-ring')


def sound_repeater(sound_maker, nr_repeats):
    for _ in range(nr_repeats):
        sound_maker.make_sound()


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='sound maker')
    arg_parser.add_argument('--type', choices=['duck', 'alarm'],
                            help='sound source')
    arg_parser.add_argument('--n', type=int, default=1,
                            help='number of sounds to make')
    options = arg_parser.parse_args()
    sound_maker = Duck() if options.type == 'duck' else AlarmClock()
    sound_repeater(sound_maker, options.n)
