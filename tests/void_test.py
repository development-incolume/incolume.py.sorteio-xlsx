"""Module test."""

import logging

import pytest


def test_void(capsys):
    """Test void."""
    print('oi')  # noqa: T201
    out, err = capsys.readouterr()
    assert out.strip() == 'oi'
    assert err == ''


@pytest.mark.parametrize(
    'entrance',
    [
        'oi',
        'hi',
        'python',
    ],
)
def test_none(capsys, entrance):
    """Test none."""
    print(entrance)  # noqa: T201
    out, err = capsys.readouterr()
    logging.debug('%s, %s', out, err)
    assert out.strip() == entrance
