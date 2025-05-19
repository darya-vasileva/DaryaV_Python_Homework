import pytest
from string_processor import StringProcessor


@pytest.mark.parametrize('input_text, result', [
    ('hello', 'Hello.'),
    ('Hello', 'Hello.'),
    ('hi', 'Hi.')])
def test_process_positive(input_text, result):
    processor = StringProcessor()
    assert processor.process(input_text) == result


@pytest.mark.parametrize('input_text, result', [
    ('', '.'),
    (' ', ' .')])
def test_process_negative(input_text, result):
    processor = StringProcessor()
    assert processor.process(input_text) == result
