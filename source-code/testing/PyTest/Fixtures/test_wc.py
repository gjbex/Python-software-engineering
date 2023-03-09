from pathlib import Path
from subprocess import check_output
import pytest


@pytest.fixture(scope='module')
def text_file():
    file_path = Path('my_text.txt')
    nr_lines, nr_words = 10, 0
    with open(file_path, 'w') as out_file:
        for line_nr in range(nr_lines):
            print(' '.join(['bla']*(line_nr + 1)), file=out_file)
            nr_words += line_nr + 1
    yield file_path, nr_lines, nr_words
    file_path.unlink()


def test_wc_l(text_file):
    path, nr_lines, _ = text_file
    output = check_output(['wc', '-l', path])
    lines, _ = output.decode(encoding='utf-8').split()
    assert int(lines) == nr_lines


def test_wc_w(text_file):
    path, _, nr_words = text_file
    output = check_output(['wc', '-w', path])
    words, _ = output.decode(encoding='utf-8').split()
    assert int(words) == nr_words
