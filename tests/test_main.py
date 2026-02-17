from unittest.mock import patch
from app import main


def test_main_calls_repl():
    with patch("app.main.repl") as repl_mock:
        main.main()
        repl_mock.assert_called_once()
