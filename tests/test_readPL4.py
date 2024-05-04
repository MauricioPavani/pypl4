import re

from pytest import raises

from errors.ReadError import FileNotPL4Error
from pypl4.readPL4 import readfile

def test_open_a_pl4_file_with_readfile():
    path = '/home/mauricio/Documentos/pypl4/tests/exemple.pl4'
    result = readfile(path)

    assert result.readable()


def test_not_found_file_with_readfile():
    path = '/home/mauricio/Documentos/pypl4/tests/exemple100.pl4'

    mensagem_erro = 'File not found!'

    with raises(FileNotFoundError, match=re.escape(mensagem_erro)):
        result = readfile(path)


def test_not_pl4_file_readfile():
    path = '/home/mauricio/Documentos/pypl4/tests/exemplo2.txt'
    mensagem_erro = 'It is not a pl4 file!'

    with raises(FileNotPL4Error, match=re.escape(mensagem_erro)):
        result = readfile(path)
