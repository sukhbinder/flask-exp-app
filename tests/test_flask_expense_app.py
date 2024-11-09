from flask_expense_app.cli import cli

def test_create_parser():
    parser = cli.create_parser()
    result = parser.parse_args(["--port", 1000])
    assert result.port == "1000"
    assert result.debug is False
    assert result.host == "0.0.0.0"

