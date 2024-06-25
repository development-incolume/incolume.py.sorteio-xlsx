"""dojo module."""

from __future__ import annotations

import datetime as dt
import random
from pathlib import Path

import pandas as pd
import pytz
from typing import Final


TZ: Final = pytz.timezone('America/Sao_Paulo')


def sorteio(k: int = 1, filename: Path | None = None) -> Path:
    """Lotery by xlsx file."""
    filename = filename or Path(__file__).parent / 'empregados.xlsx'
    ext = {'.xlsx': pd.read_excel}
    timestamp = f'{dt.datetime.now(tz=TZ):-%Y-%m-%d-%H-%M-%S}'
    fout: Path = filename.with_name(
        f'{filename.stem}{timestamp}.xlsx',
    )
    df0 = ext.get(filename.suffix)(filename)

    items = list(df0.index)
    k = min(k, len(items))
    result = random.sample(items, k=k)

    df0.loc[result].to_excel(fout)
    return fout
