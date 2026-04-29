"""Tests for philiprehberger_ansi_style."""

from __future__ import annotations

import os
from unittest import mock

from philiprehberger_ansi_style import (
    bg_rgb,
    bold,
    hex_color,
    red,
    rgb,
    strip_ansi,
    style,
    supports_color,
    terminal_link,
)


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


class TestRgb:
    def test_rgb_adds_24bit_foreground_when_tty(self) -> None:
        with _enable_tty() as mock_stdout:
            mock_stdout.isatty.return_value = True
            result = rgb("hello", 255, 87, 51)
        assert result == "\033[38;2;255;87;51mhello\033[0m"

    def test_rgb_returns_plain_text_when_not_tty(self) -> None:
        with _enable_tty() as mock_stdout:
            mock_stdout.isatty.return_value = False
            result = rgb("hello", 255, 87, 51)
        assert result == "hello"


class TestBgRgb:
    def test_bg_rgb_adds_24bit_background_when_tty(self) -> None:
        with _enable_tty() as mock_stdout:
            mock_stdout.isatty.return_value = True
            result = bg_rgb("hello", 0, 128, 255)
        assert result == "\033[48;2;0;128;255mhello\033[0m"

    def test_bg_rgb_returns_plain_text_when_not_tty(self) -> None:
        with _enable_tty() as mock_stdout:
            mock_stdout.isatty.return_value = False
            result = bg_rgb("hello", 0, 128, 255)
        assert result == "hello"


class TestHexColor:
    def test_hex_color_with_hash_prefix(self) -> None:
        with _enable_tty() as mock_stdout:
            mock_stdout.isatty.return_value = True
            result = hex_color("hello", "#FF5733")
        assert result == "\033[38;2;255;87;51mhello\033[0m"

    def test_hex_color_without_hash_prefix(self) -> None:
        with _enable_tty() as mock_stdout:
            mock_stdout.isatty.return_value = True
            result = hex_color("hello", "00FF00")
        assert result == "\033[38;2;0;255;0mhello\033[0m"

    def test_hex_color_returns_plain_text_when_not_tty(self) -> None:
        with _enable_tty() as mock_stdout:
            mock_stdout.isatty.return_value = False
            result = hex_color("hello", "#FF5733")
        assert result == "hello"


class TestNoColor:
    def test_returns_plain_when_no_color_set(self) -> None:
        with _enable_tty() as mock_stdout:
            mock_stdout.isatty.return_value = True
            with mock.patch.dict(os.environ, {"NO_COLOR": "1"}):
                result = red("hello")
        assert result == "hello"


class TestSupportsColor:
    def test_true_when_tty_and_no_color_unset(self) -> None:
        with _enable_tty() as mock_stdout:
            mock_stdout.isatty.return_value = True
            with mock.patch.dict(os.environ, {}, clear=True):
                assert supports_color() is True

    def test_false_when_not_tty(self) -> None:
        with _enable_tty() as mock_stdout:
            mock_stdout.isatty.return_value = False
            assert supports_color() is False

    def test_false_when_no_color_set(self) -> None:
        with _enable_tty() as mock_stdout:
            mock_stdout.isatty.return_value = True
            with mock.patch.dict(os.environ, {"NO_COLOR": "1"}):
                assert supports_color() is False


class TestTerminalLink:
    def test_emits_osc8_when_tty(self) -> None:
        with _enable_tty() as mock_stdout:
            mock_stdout.isatty.return_value = True
            result = terminal_link("docs", "https://example.com")
        assert result == "\033]8;;https://example.com\033\\docs\033]8;;\033\\"

    def test_returns_plain_when_not_tty(self) -> None:
        with _enable_tty() as mock_stdout:
            mock_stdout.isatty.return_value = False
            result = terminal_link("docs", "https://example.com")
        assert result == "docs"
