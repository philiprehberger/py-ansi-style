# philiprehberger-ansi-style

[![Tests](https://github.com/philiprehberger/py-ansi-style/actions/workflows/publish.yml/badge.svg)](https://github.com/philiprehberger/py-ansi-style/actions/workflows/publish.yml)
[![PyPI version](https://img.shields.io/pypi/v/philiprehberger-ansi-style.svg)](https://pypi.org/project/philiprehberger-ansi-style/)
[![Last updated](https://img.shields.io/github/last-commit/philiprehberger/py-ansi-style)](https://github.com/philiprehberger/py-ansi-style/commits/main)

![philiprehberger-ansi-style](https://raw.githubusercontent.com/philiprehberger/py-ansi-style/main/package-card.webp)

Terminal text styling with zero dependencies and TTY detection.

## Installation

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

### Detect color support

```python
from philiprehberger_ansi_style import supports_color, red

text = red("error") if supports_color() else "error"
```

### Clickable terminal links

```python
from philiprehberger_ansi_style import terminal_link

print(terminal_link("Open docs", "https://example.com"))
```

### Force or disable color

```python
from philiprehberger_ansi_style import color_mode, red, set_color_mode

# Force color even when stdout isn't a TTY (e.g. capturing output in tests)
with color_mode("always"):
    print(red("Always red"))

# Disable color for an entire process
set_color_mode("never")
```

The `auto` mode also honors the `FORCE_COLOR` env var to enable styling in
CI logs where stdout is not a TTY. `NO_COLOR` continues to take precedence
when both are set.

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
| `supports_color()` | Return `True` if styling will be emitted (honors mode + TTY + `NO_COLOR` / `FORCE_COLOR`) |
| `terminal_link(text, url)` | Wrap text as an OSC 8 hyperlink for capable terminals |
| `set_color_mode(mode)` | Force `"always"`, `"never"`, or `"auto"` color emission globally |
| `color_mode(mode)` | Context manager that temporarily overrides the color mode |

## Development

```bash
pip install -e .
python -m pytest tests/ -v
```

## Support

If you find this project useful:

⭐ [Star the repo](https://github.com/philiprehberger/py-ansi-style)

🐛 [Report issues](https://github.com/philiprehberger/py-ansi-style/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

💡 [Suggest features](https://github.com/philiprehberger/py-ansi-style/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement)

❤️ [Sponsor development](https://github.com/sponsors/philiprehberger)

🌐 [All Open Source Projects](https://philiprehberger.com/open-source-packages)

💻 [GitHub Profile](https://github.com/philiprehberger)

🔗 [LinkedIn Profile](https://www.linkedin.com/in/philiprehberger)

## License

[MIT](LICENSE)
