"""Test sorteio module."""

import sys
from incolume.py.sorteio_xlsx import sorteio as pkg
from tempfile import NamedTemporaryFile
from pathlib import Path
import pytest


class TestCase:
    """Testcase."""

    def test_0(self):
        """Teste 0."""
        obj = pkg.DataFake(count=1, seed=1061, lang='pt_BR')
        expected = (
            'Carolina Duarte Cardoso',
            '651.037.248-71',
            'carolina-duarte-cardoso@example.net',
        )
        assert obj.data_fake() == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ({'seed': 1061}, (10, 3)),
            ({'seed': 1073, 'lang': 'pt_BR'}, (10, 3)),
            ({'seed': 1073, 'lang': 'en_US'}, (10, 3)),
            ({'count': 1, 'seed': 1061, 'lang': 'pt_BR'}, (1, 3)),
        ],
    )
    def test_1(self, entrance, expected):
        """Test 1."""
        obj = pkg.DataFake(**entrance)
        assert obj._generate_dataframe().shape == expected  # noqa: SLF001

    def test_2(self):
        """Test 2."""
        obj = pkg.DataFake(
            seed=1061,
            fileoutput=Path(NamedTemporaryFile().name),
        )
        assert obj.write_xlsx()

    @pytest.mark.parametrize(
        'obj_param entrance expected'.split(),
        [
            pytest.param(
                {'count': 50, 'seed': 1061, 'lang': 'pt_BR', 'fileoutput': ''},
                {
                    'k': 3,
                    'filename': '',
                },
                3,
                marks=pytest.mark.skipif(
                    sys.platform.startswith('win'),
                    reason='Does not run on windows.',
                ),
            ),
            pytest.param(
                {
                    'count': 100,
                    'seed': 1061,
                    'lang': 'pt_BR',
                    'fileoutput': '',
                },
                {
                    'k': 10,
                    'filename': '',
                },
                10,
                marks=pytest.mark.skipif(
                    sys.platform.startswith('win'),
                    reason='Does not run on windows.',
                ),
            ),
        ],
    )
    def test_3(self, obj_param, entrance, expected):
        """Unittest."""
        fout = Path(NamedTemporaryFile(suffix='.xlsx').name)
        obj_param.update({'fileoutput': fout})
        entrance.update({'filename': fout})

        obj = pkg.DataFake(**obj_param)
        obj.write_xlsx()
        result = pkg.sorteio(**entrance)
        assert pkg.pd.read_excel(result).shape[0] == expected
