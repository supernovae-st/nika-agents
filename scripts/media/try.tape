# try.tape — the cheapest first success in the ecosystem, in ~10 seconds:
# `nika try 01-hello` renders a live DAG offline (the mock rehearsal · zero
# keys · nothing written) and the run card points at `nika new` to make it
# yours. Every command is the released binary's own; the sandbox HOME
# (/tmp/you) is staged by scripts/media/render.sh — nothing is faked.
Output try.gif

Set Shell zsh
Set FontFamily "JetBrains Mono"
Set FontSize 21
Set Width 1420
Set Height 780
Set Padding 24
Set Margin 22
Set MarginFill "#4f86ff"
Set BorderRadius 14
Set WindowBar Colorful
Set WindowBarSize 42
Set Theme { "name": "nika", "background": "#08090b", "foreground": "#dbe3ee", "cursor": "#4f86ff", "black": "#10131a", "red": "#ff6b6b", "green": "#34d399", "yellow": "#f0b45b", "blue": "#4f86ff", "magenta": "#b07bff", "cyan": "#22d3ee", "white": "#dbe3ee", "brightBlack": "#5b6472", "brightRed": "#ff8f8f", "brightGreen": "#5ee6b0", "brightYellow": "#ffd08a", "brightBlue": "#8db4ff", "brightMagenta": "#c9a2ff", "brightCyan": "#67e3f5", "brightWhite": "#ffffff" }
Set TypingSpeed 30ms
Set PlaybackSpeed 1.0

Hide
Type "export HOME=/tmp/you && cd /tmp/you/demo && unset -m '*API_KEY*' '*_TOKEN*' '*SECRET*' 2>/dev/null; setopt interactive_comments && clear"
Enter
Show

Type "# see a workflow WORK · offline · zero keys · nothing written"
Enter
Sleep 700ms
Type "nika try 01-hello"
Enter
Sleep 6200ms
Sleep 1400ms
