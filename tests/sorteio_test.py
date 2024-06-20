"""Test sorteio module."""

from incolume.py.sorteio_xlsx import sorteio as pkg
from tempfile import NamedTemporaryFile
from pathlib import Path


class TestCase:
    """Testcase."""

    def test_0(self):
        """Teste 0."""
        obj = pkg.DataFake(count=1, seed=1061, lang='pt_BR')
        expected = ('Carolina Duarte Cardoso', '651.037.248-71', 'carolina-duarte-cardoso@example.net')
        assert obj.data_fake() == expected

    def test_1(self):
        """Test 1."""
        obj = pkg.DataFake(count=1, seed=1061, lang='pt_BR')
        expected = (1,3)
        assert obj._generate_dataframe().shape == expected
    
    def test_2(self):
        """Test 2."""
        obj = pkg.DataFake(seed=1061, fileoutput=Path(NamedTemporaryFile().name))
        expected = ''
        assert obj.write_xlsx()

