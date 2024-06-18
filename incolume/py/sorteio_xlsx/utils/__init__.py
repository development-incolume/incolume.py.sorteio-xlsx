"""Module utils."""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = '@britodfbr'  # pragma: no cover

from collections import namedtuple
from typing import NamedTuple

TypeColor: NamedTuple = namedtuple('TypeColor', 'none red green blue yellow')  # noqa: PYI024

color = TypeColor(
    none='\033[0m',
    red='\033[1;31m',
    green='\033[1;32m',
    blue='\033[1;34m',
    yellow='\033[1;33m',
)


def msg_colored(msg, cor):
    """Colored text."""
    return f'{cor}{msg}{color.none}'
