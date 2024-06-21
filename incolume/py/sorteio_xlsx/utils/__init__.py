"""Module utils."""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = '@britodfbr'  # pragma: no cover

from collections import namedtuple
from typing import NamedTuple
import pandas as pd
from faker import Faker
from pathlib import Path

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


class DataFake:
    """Data Fake for this module."""

    def __init__(
        self,
        **kwargs,
    ):
        """Init this class.

        count: int = 0,
        fileoutput: Path = None,
        domain: str = '',
        seed: int = None,
        lang: str = 'pt_BR',
        """
        self.fileoutput = (
            kwargs.get('fileoutput')
            or Path(__file__).parent / 'empregados.xlsx'
        )
        self.count = kwargs.get('count') or 10
        self.seed = kwargs.get('seed')
        self.lang = kwargs.get('lang', 'pt_BR')
        self.domain = kwargs.get('domain', '')
        self.fake = Faker(self.lang)

    def data_fake(self) -> tuple[str, ...]:
        """Gen data fake for XLSX files."""
        if self.seed:
            self.fake.seed_instance(self.seed)
        domain = self.domain or self.fake.safe_domain_name()
        name = (
            f'{self.fake.first_name()}'
            f' {self.fake.last_name()}'
            f' {self.fake.last_name()}'
        )
        try:
            cpf = self.fake.cpf()
        except AttributeError:
            cpf = self.fake.pystr_format(string_format='###.###.###-##')

        email = f'{self.fake.slug(name)}@{domain}'
        return name, cpf, email

    def _generate_dataframe(self) -> pd.DataFrame:
        """Generate dataframe."""
        title = 'nome cpf email'.split()
        users = (self.data_fake() for _ in range(self.count))
        return pd.DataFrame(users, columns=title)

    def write_xlsx(self) -> bool:
        """Write xlsx file."""
        data = self._generate_dataframe()
        data.to_excel(self.fileoutput, index=False)
        return self.fileoutput.is_file()
