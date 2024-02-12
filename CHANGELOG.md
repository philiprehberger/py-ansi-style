# Changelog

## 0.2.0 (2026-04-04)

- Add `rgb()` function for 24-bit RGB foreground colors
- Add `bg_rgb()` function for 24-bit RGB background colors
- Add `hex_color()` function for hex color code support

## 0.1.2 (2026-03-31)

- Standardize README to 3-badge format with emoji Support section
- Update CI checkout action to v5 for Node.js 24 compatibility
- Add GitHub issue templates, dependabot config, and PR template

## 0.1.1 (2026-03-22)

- Rename Install section to Installation in README
- Add Changelog URL to project URLs
- Add `#readme` anchor to Homepage URL
- Add pytest and mypy configuration

## 0.1.0 (2026-03-21)

- Initial release
- Color functions: red, green, blue, yellow, cyan, magenta, white, gray
- Style functions: bold, dim, underline, italic
- Custom styling with `style()` supporting fg, bg, and style combinations
- `strip_ansi()` utility to remove ANSI codes
- Auto-detect TTY with NO_COLOR environment variable support
