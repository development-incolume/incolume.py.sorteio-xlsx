"""Skell test."""

import pytest

from incolume.py.model_2023_07_05.skell import Skell, skell

__author__ = '@britodfbr'


class TestSkellCase:
    # @pytest.mark.skip
    @pytest.mark.parametrize(
        'entrance expected'.split(),
        (
            (('1', 2, 'a', 1, '3', 3), {'args': ('1', 2, 'a', 1, '3', 3)}),
            (('1', 'a', '3'), {'args': ('1', 'a', '3')}),
            ((2, 1, 3), {'args': (2, 1, 3)}),
        ),
    )
    def test_args(self, entrance, expected):
        """Validação de entrada em args."""
        assert skell(*entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        (
            (
                {'a': '1', 'b': 2, 'c': 3},
                {'a': '1', 'args': (), 'b': 2, 'c': 3},
            ),
        ),
    )
    def test_kwargs(self, entrance, expected):
        """Validação de entrada em kwargs."""
        s = Skell(**entrance)
        assert s.__dict__ == expected

    @pytest.mark.parametrize(
        'args kwargs expected'.split(),
        (
            pytest.param(
                (1, 2, 3),
                {},
                {'args': (1, 2, 3)},
            ),
            pytest.param(
                (),
                {'a': '1', 'b': 2, 'c': 3},
                {'a': '1', 'args': (), 'b': 2, 'c': 3},
            ),
            pytest.param(
                (1, 2, 3),
                {'a': '1', 'b': 2, 'c': 3},
                {'a': '1', 'args': (1, 2, 3), 'b': 2, 'c': 3},
            ),
        ),
    )
    def test_all_params(self, args, kwargs, expected):
        """Validação de entrada em kwargs."""
        s = Skell(*args, **kwargs)
        assert s.__dict__ == expected
