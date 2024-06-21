"""dojo module."""

from __future__ import annotations

import datetime as dt
import random
from pathlib import Path

import pandas as pd
import pytz
from faker import Faker
from typing import Final


TZ: Final = pytz.timezone('America/Sao_Paulo')


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


def sorteio(k: int = 1, filename: Path | None = None) -> Path:
    """Lotery by xlsx file."""
    filename = filename or Path(__file__).parent / 'empregados.xlsx'
    ext = {'.xlsx': pd.read_excel}
    fout: Path = filename.with_name(
        f'{filename.stem}{dt.datetime.now(tz=TZ).isoformat()}.xlsx',
    )
    df0 = ext.get(filename.suffix)(filename)

    items = list(df0.index)
    k = min(k, len(items))
    result = random.sample(items, k=k)

    df0.loc[result].to_excel(fout)
    return fout
