"""Skell structure."""

import logging
import typing


def skell(
    *args: typing.Any,
    **kwargs: typing.Any,
) -> typing.Dict[str, typing.Any]:
    """Esqueleto de função.

    Args:
        args: Argumentos.
        kwargs: Argumentos chaveados.

    Returns:
        Um dicionário com os argumentos de entrada.

    Examples:
        >>> skell(1, 2, 3)
        {'args': (1, 2, 3)}

        >>> skell(a=1, b=2, c=3)
        {'args': (), 'a': 1, 'b': 2, 'c': 3}
    """
    result = {'args': args, **kwargs}
    logging.debug(result)
    logging.info('Args: {%s}, kwargs: {%s}', bool(args), bool(kwargs))
    return result


class Skell:
    """Class for skell."""

    def __init__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """Esqueleto de função.

        Args:
            args: Argumentos.
            kwargs: Argumentos chaveados.

        Returns:
            Um dicionário com os argumentos de entrada.

        Examples:
            >>> skell = Skell(1, 2, 3)
            >>> skell.__dict__
            {'args': (1, 2, 3)}

            >>> skell = Skell(a=1, b=2, c=3)
            >>> skell.__dict__
            {'args': (), 'a': 1, 'b': 2, 'c': 3}

            >>> skell = Skell(1, 2, 3, a=1, b=2, c=3)
            >>> skell.__dict__
            {'args': (1, 2, 3), 'a': 1, 'b': 2, 'c': 3}
        """
        self.__dict__.update({'args': args})
        self.__dict__.update(kwargs)


def run():
    """Run this."""
    skell(1, 2, 3, a=7)


if __name__ == '__main__':
    run()
