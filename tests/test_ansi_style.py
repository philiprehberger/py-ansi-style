"""Tests for philiprehberger_ansi_style."""

from __future__ import annotations

import os
from unittest import mock

from philiprehberger_ansi_style import bold, red, strip_ansi, style


def _enable_tty() -> mock._patch[mock.MagicMock]:
    """Return a patch that makes sys.stdout.isatty() return True."""
    return mock.patch("philiprehberger_ansi_style.sys.stdout")


class TestRedWrapsText:
    def test_red_adds_ansi_codes_when_tty(self) -> None:
        with _enable_tty() as mock_stdout:
            mock_stdout.isatty.return_value = True
            result = red("hello")
        assert result == "\033[31mhello\033[0m"

    def test_red_returns_plain_text_when_not_tty(self) -> None:
        with _enable_tty() as mock_stdout:
            mock_stdout.isatty.return_value = False
            result = red("hello")
        assert result == "hello"


class TestBoldWrapsText:
    def test_bold_adds_ansi_codes_when_tty(self) -> None:
        with _enable_tty() as mock_stdout:
            mock_stdout.isatty.return_value = True
            result = bold("hello")
        assert result == "\033[1mhello\033[0m"


class TestStripAnsi:
    def test_removes_color_codes(self) -> None:
        styled = "\033[31mhello\033[0m"
        assert strip_ansi(styled) == "hello"

    def test_removes_multiple_codes(self) -> None:
        styled = "\033[1;31mhello\033[0m \033[34mworld\033[0m"
        assert strip_ansi(styled) == "hello world"

    def test_plain_text_unchanged(self) -> None:
        assert strip_ansi("hello") == "hello"


class TestStyleFunction:
    def test_style_with_fg_and_bold(self) -> None:
        with _enable_tty() as mock_stdout:
            mock_stdout.isatty.return_value = True
            result = style("hello", fg="red", bold=True)
        assert "\033[" in result
        assert "hello" in result
        assert "1" in result.split("m")[0]
        assert "31" in result.split("m")[0]


class TestNoColor:
    def test_returns_plain_when_no_color_set(self) -> None:
        with _enable_tty() as mock_stdout:
            mock_stdout.isatty.return_value = True
            with mock.patch.dict(os.environ, {"NO_COLOR": "1"}):
                result = red("hello")
        assert result == "hello"
