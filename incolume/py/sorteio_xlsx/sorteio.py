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
        *,
        count: int = 0,
        fileoutput: Path | None = None,
        domain: str = '',
        seed: int | None = None,
        lang: str = '',
    ):
        """Init this class."""
        self.fileoutput = (
            fileoutput or Path(__file__).parent / 'empregados.xlsx'
        )
        self.count = count or 10
        self.seed = seed
        self.lang = lang or 'pt_BR'
        self.fake = Faker(lang)
        self.domain = domain

    def data_fake(self) -> tuple[str, ...]:
        """Gen data fake for XLSX files."""
        if self.seed:
            self.fake.seed_instance(self.seed)
        domain = self.domain or self.fake.safe_domain_name()
        name = f'{self.fake.first_name()} {self.fake.last_name()} {self.fake.last_name()}'
        cpf = self.fake.cpf()
        email = f'{self.fake.slug(name)}@{domain}'
        return name, cpf, email

    def _generate_dataframe(self) -> pd.DataFrame:
        """Generate dataframe."""
        title = 'nome cpf email'.split()
        users = (self.data_fake() for _ in range(self.count))
        pd0 = pd.DataFrame(users, columns=title)
        print(pd0)
        return pd0

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
    result = random.sample(items, k=k)

    df0.loc[result].to_excel(fout)
    return fout
