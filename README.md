# philiprehberger-ansi-style

[![Tests](https://github.com/philiprehberger/py-ansi-style/actions/workflows/publish.yml/badge.svg)](https://github.com/philiprehberger/py-ansi-style/actions/workflows/publish.yml)
[![PyPI version](https://img.shields.io/pypi/v/philiprehberger-ansi-style.svg)](https://pypi.org/project/philiprehberger-ansi-style/)
[![License](https://img.shields.io/github/license/philiprehberger/py-ansi-style)](LICENSE)

Terminal text styling with zero dependencies and TTY detection.

## Install

```bash
pip install philiprehberger-ansi-style
```

## Usage

```python
from philiprehberger_ansi_style import red, green, blue, bold, underline

print(red("Error: something went wrong"))
print(green("Success!"))
print(bold(blue("Important message")))
```

### Color functions

```python
from philiprehberger_ansi_style import (
    red, green, blue, yellow, cyan, magenta, white, gray,
)

print(red("Red text"))
print(green("Green text"))
print(blue("Blue text"))
print(yellow("Yellow text"))
print(cyan("Cyan text"))
print(magenta("Magenta text"))
print(white("White text"))
print(gray("Gray text"))
```

### Style functions

```python
from philiprehberger_ansi_style import bold, dim, underline, italic

print(bold("Bold text"))
print(dim("Dim text"))
print(underline("Underlined text"))
print(italic("Italic text"))
```

### Custom styling

```python
from philiprehberger_ansi_style import style

print(style("Alert", fg="red", bold=True))
print(style("Note", fg="cyan", underline=True))
print(style("Highlight", fg="white", bg="blue", bold=True))
```

### Strip ANSI codes

```python
from philiprehberger_ansi_style import red, strip_ansi

styled = red("hello")
plain = strip_ansi(styled)  # "hello"
```

## API

| Function | Description |
|---|---|
| `red(text)` | Apply red foreground color |
| `green(text)` | Apply green foreground color |
| `blue(text)` | Apply blue foreground color |
| `yellow(text)` | Apply yellow foreground color |
| `cyan(text)` | Apply cyan foreground color |
| `magenta(text)` | Apply magenta foreground color |
| `white(text)` | Apply white foreground color |
| `gray(text)` | Apply gray foreground color |
| `bold(text)` | Apply bold weight |
| `dim(text)` | Apply dim intensity |
| `underline(text)` | Apply underline decoration |
| `italic(text)` | Apply italic style |
| `style(text, *, fg, bg, bold, dim, underline)` | Apply custom combination of colors and styles |
| `strip_ansi(text)` | Remove all ANSI escape codes from text |

## Development

```bash
pip install -e .
python -m pytest tests/ -v
```

## License

MIT
