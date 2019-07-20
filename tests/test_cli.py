import pytest
from hr import cli

@pytest.fixture
def parser():
    return cli.create_parser()

def test_parser_no_args(parser):
    with pytest.raises(SystemExit):
        parser.parse_args([])

def test_parser_no_flag(parser):
    args = parser.parse_args(['path_to_file'])
    assert args and not args.export

def test_parser_with_flag(parser):
    args = parser.parse_args(['--export', 'path_to_file'])
    assert args and args.export

