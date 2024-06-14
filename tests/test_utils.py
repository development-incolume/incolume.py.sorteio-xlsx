"""Test utils module."""
import pytest

from incolume.py.model_2023_07_05 import utils

__author__ = '@britodfbr'  # pragma: no cover


class TestCaseUtils:
    """Test case."""

    def test_type(self):
        assert isinstance(utils.color, utils.TypeColor)

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        (
            (utils.color.none, '\x1b[0m'),
            (utils.color.red, '\x1b[1;31m'),
            (utils.color.green, '\x1b[1;32m'),
            (utils.color.blue, '\x1b[1;34m'),
            (utils.color.yellow, '\x1b[1;33m'),
        ),
    )
    def test_type_color(self, entrance, expected):
        """Test it."""
        assert entrance == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        (
            (('xpto', utils.color.blue), '\x1b[1;34mxpto\x1b[0m'),
            (('xpto', utils.color.green), '\x1b[1;32mxpto\x1b[0m'),
            (('xpto', utils.color.red), '\x1b[1;31mxpto\x1b[0m'),
            (('xpto', utils.color.yellow), '\x1b[1;33mxpto\x1b[0m'),
        ),
    )
    def test_msg_colored(self, entrance, expected):
        assert utils.msg_colored(*entrance) == expected
