My tmux configure file
======================

A fine-tuned tmux configure file.

### Usage

    $ cd <some-where>
    $ git clone https://github.com/jinchizhong/my-tmux
    $ ln -s <some-where>/my-tmux/tmux.conf ~/.tmux.conf

### Features

1. Column based pane layout

2. Two different prefixes for different commands

3. Key-bindings in copy-mode exactly same to vim

4. System clipboard support

5. Fine-tuned mouse support

### Session shortcuts

| Key           | Function             |
| ------------- | -------------------- |
| C-b d         | Detach clinet        |
| C-b D         | Detach one client    |
| C-b s         | Choose session       |

### Window shortcuts

| Key | Function |
| - | - |
| C-b c | New window |
| C-b 1-9 | Select window 1-9 |
| C-b tab | Switch between recent two windows |
| C-b , | Rename window |
| C-b . | Move window |

### Pane shortcuts

| Key | Function |
| - | - |
| C-b <left/right/up/down> | Focus left/right/up/down pane |
| C-b - | Create new pane below current pane |
| C-b \| | Create new column after current column |
| C-b % | Split current pane vertically |
| C-b z | Zoom current pane |
| C-b k | Kill current pane |
| C-b m | Mark current pane |
| C-b space | Swap current pane and marked pane |
| C-a <up/down/left/right> | Resize current pane |
| C-a C-<up/down/left/right> | Resize current pane slowly |
| C-a + | Enlarge current pane |
| C-a - | Reduce current pane |

### Copy mode (View history mode)

| Key | Function |
| - | - |
| C-b v | Turn on copy-mode |
| C-b PageUp | Turn on copy-mode |
| C-b / | Turn on copy-mode, and begin search |
| C-b ? | Turn on copy-mode, and begin reverse search |

Following shortcuts only works, when copy-mode is turned on. They are very close to vim default shortcuts.
Most of keys support repeat, for example:

10w => move cursor by 10 words
5PageUp => Scroll 5 pages up

| Key | Function |
| - | - |
| <up/down/left/right> | move cursor |
| <h/j/k/l> | move cursor (vim style) |
| w | move cursor by word |
| W | move cursor by word (space-separated) |
| e | move cursor by word-end |
| E | move cursor by word-end (space-separated) |
| b | backward move cursor by word |
| B | backward move cursor by word (space-separated) |
| - | - |
| 0 | move to start of the line |
| ^ | move to first character of line |
| $ | move to end of the line |
| Home | move to start of the line |
| End | move to end of the line |
| PageUp | page up |
| PageDown | Page down |
| gg | Move to the first line |
| G | Move to the last line |
| <num>G | Move to line <num> |
| - | - |
| / | begin search |
| ? | begin reverse search |
| n | search next |
| N | search previous |
| - | - |
| v | begin selection |
| V | begin selection with line selection mode |
| C-v | begin selection with block selection mode |
| y | copy to clipboard |
| Y | copy to selection(linux primary clipboard) |
| Esc | clear selection |
| q | quit copy-mode |

### Clipboard

| Key | Function |
| - | - |
| C-b p | Paste clipboard to pane |
| C-b P | Paste selection to pane |

### Mouse support

| Action | Function |
| - | - |
| left click pane | active pane |
| right click pane | mark pane, then you can left click another pane to swap them |
| drag in pane | select content, then you can right click to copy them |
| middle click in pane | linux style paste action |
| wheel up/down in pane | if program run in pane support mouse wheel, translate mouse event and send to it, otherwise start copy-mode |
| click on window label | switch to window |
