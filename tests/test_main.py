import runpy
from unittest.mock import patch


def test_main_calls_repl():
    with patch("app.main.repl") as repl_mock:
        runpy.run_module("app.main", run_name="__main__")
        repl_mock.assert_called_once()

