"""dojo module."""

from __future__ import annotations

import datetime as dt
import random
from pathlib import Path

import pandas as pd
import pytz
from faker import Faker


def data_fake(*, seed: int | None = None, lang: str = '') -> tuple[str, ...]:
    """Gen data fake for XLSX files."""
    lang = lang or 'pt_BR'
    fake = Faker(lang)
    if seed:
        fake.seed_instance(seed)

    return (
        (name := f'{fake.first_name()} {fake.last_name()} {fake.last_name()}'),
        fake.cpf(),
        f'{fake.slug(name)}@example.com',
    )


def generate_dataframe(count: int = 0) -> pd.DataFrame:
    """Generate dataframe."""
    count = count or 10
    title = 'nome cpf email'.split()
    users = (data_fake() for _ in range(count))
    df0 = pd.DataFrame(users, columns=title)
    return df0


def write_xlsx(data: pd.DataFrame, filename: Path | None = None) -> bool:
    """Write xlsx file."""
    filename = filename or Path(__file__).parent / 'empregados.xlsx'
    data.to_excel(filename, index=False)
    return filename.is_file()


def sorteio(k: int = 1, filename: Path | None = None) -> Path:
    """Lotery by xlsx file."""
    filename = filename or Path(__file__).parent / 'empregados.xlsx'
    ext = {'.xlsx': pd.read_excel}
    fout: Path = filename.with_name(
        f'{filename.stem}{dt.datetime.now(tz=pytz.timezone("America/Sao_Paulo")).isoformat()}.xlsx',
    )
    df0 = ext.get(filename.suffix)(filename)

    items = list(df0.index)
    result = random.sample(items, k=k)

    df0.loc[result].to_excel(fout)
    return fout
