"""Terminal text styling with zero dependencies and TTY detection."""

from __future__ import annotations

import os
import re
import sys

__all__ = [
    "red",
    "green",
    "blue",
    "yellow",
    "cyan",
    "magenta",
    "white",
    "gray",
    "bold",
    "dim",
    "underline",
    "italic",
    "style",
    "rgb",
    "bg_rgb",
    "hex_color",
    "strip_ansi",
    "supports_color",
    "terminal_link",
]

_ANSI_RE = re.compile(r"\033\[[0-9;]*m")

_FG_CODES: dict[str, int] = {
    "black": 30,
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
    "white": 37,
    "gray": 90,
}

_BG_CODES: dict[str, int] = {
    "black": 40,
    "red": 41,
    "green": 42,
    "yellow": 43,
    "blue": 44,
    "magenta": 45,
    "cyan": 46,
    "white": 47,
    "gray": 100,
}


def _is_tty() -> bool:
    """Return True if stdout is a TTY and NO_COLOR is not set."""
    if os.environ.get("NO_COLOR") is not None:
        return False
    return hasattr(sys.stdout, "isatty") and sys.stdout.isatty()


def _wrap(text: str, code: int) -> str:
    """Wrap text with an ANSI escape code if output is a TTY."""
    if not _is_tty():
        return text
    return f"\033[{code}m{text}\033[0m"


# Color functions


def red(text: str) -> str:
    """Apply red foreground color."""
    return _wrap(text, 31)


def green(text: str) -> str:
    """Apply green foreground color."""
    return _wrap(text, 32)


def blue(text: str) -> str:
    """Apply blue foreground color."""
    return _wrap(text, 34)


def yellow(text: str) -> str:
    """Apply yellow foreground color."""
    return _wrap(text, 33)


def cyan(text: str) -> str:
    """Apply cyan foreground color."""
    return _wrap(text, 36)


def magenta(text: str) -> str:
    """Apply magenta foreground color."""
    return _wrap(text, 35)


def white(text: str) -> str:
    """Apply white foreground color."""
    return _wrap(text, 37)


def gray(text: str) -> str:
    """Apply gray foreground color."""
    return _wrap(text, 90)


# 24-bit RGB color functions


def rgb(text: str, r: int, g: int, b: int) -> str:
    """Apply 24-bit RGB foreground color."""
    if not _is_tty():
        return text
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"


def bg_rgb(text: str, r: int, g: int, b: int) -> str:
    """Apply 24-bit RGB background color."""
    if not _is_tty():
        return text
    return f"\033[48;2;{r};{g};{b}m{text}\033[0m"


def hex_color(text: str, hex_code: str) -> str:
    """Apply foreground color from hex code (e.g., '#FF5733' or 'FF5733')."""
    h = hex_code.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return rgb(text, r, g, b)


# Style functions


def bold(text: str) -> str:
    """Apply bold style."""
    return _wrap(text, 1)


def dim(text: str) -> str:
    """Apply dim style."""
    return _wrap(text, 2)


def underline(text: str) -> str:
    """Apply underline style."""
    return _wrap(text, 4)


def italic(text: str) -> str:
    """Apply italic style."""
    return _wrap(text, 3)


# Custom styling


def style(
    text: str,
    *,
    fg: str | None = None,
    bg: str | None = None,
    bold: bool = False,
    dim: bool = False,
    underline: bool = False,
) -> str:
    """Apply custom styling to text.

    Args:
        text: The text to style.
        fg: Foreground color name (e.g. "red", "blue", "cyan").
        bg: Background color name (e.g. "red", "blue", "cyan").
        bold: Apply bold weight.
        dim: Apply dim intensity.
        underline: Apply underline decoration.

    Returns:
        Styled text if output is a TTY, plain text otherwise.
    """
    if not _is_tty():
        return text

    codes: list[int] = []
    if bold:
        codes.append(1)
    if dim:
        codes.append(2)
    if underline:
        codes.append(4)
    if fg and fg in _FG_CODES:
        codes.append(_FG_CODES[fg])
    if bg and bg in _BG_CODES:
        codes.append(_BG_CODES[bg])

    if not codes:
        return text

    sequence = ";".join(str(c) for c in codes)
    return f"\033[{sequence}m{text}\033[0m"


# Utility


def strip_ansi(text: str) -> str:
    """Remove all ANSI escape codes from text."""
    return _ANSI_RE.sub("", text)


def supports_color() -> bool:
    """Return True if styling will be emitted (stdout is a TTY and NO_COLOR is unset)."""
    return _is_tty()


def terminal_link(text: str, url: str) -> str:
    """Wrap *text* as an OSC 8 hyperlink pointing to *url*.

    Modern terminals (iTerm2, kitty, WezTerm, recent VTE-based terminals) render
    the result as a clickable link. When stdout is not a TTY (or NO_COLOR is set)
    the unformatted text is returned so logs and pipes stay clean.
    """
    if not _is_tty():
        return text
    return f"\033]8;;{url}\033\\{text}\033]8;;\033\\"
