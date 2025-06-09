# Neovim Keybinds & Commands Cheat Sheet

## Basic Vim Motions & Commands

### Movement
- `h j k l` - Left, Down, Up, Right
- `w` - Next word start
- `b` - Previous word start
- `e` - End of word
- `0` - Beginning of line
- `$` - End of line
- `gg` - Top of file
- `G` - Bottom of file
- `{` `}` - Previous/Next paragraph
- `%` - Jump to matching bracket

### Editing
- `i` - Insert before cursor
- `a` - Insert after cursor
- `I` - Insert at beginning of line
- `A` - Insert at end of line
- `o` - New line below
- `O` - New line above
- `x` - Delete character
- `dd` - Delete line
- `yy` - Copy line
- `p` - Paste after cursor
- `P` - Paste before cursor
- `u` - Undo
- `Ctrl+r` - Redo

### Visual Mode
- `v` - Character visual mode
- `V` - Line visual mode
- `Ctrl+v` - Block visual mode

## Advanced Text Objects & Operations

### Text Objects (use with d, y, c, v, etc.)
- `iw` / `aw` - Inside/Around word
- `is` / `as` - Inside/Around sentence
- `ip` / `ap` - Inside/Around paragraph
- `i(` / `a(` - Inside/Around parentheses
- `i[` / `a[` - Inside/Around brackets
- `i{` / `a{` - Inside/Around braces
- `i"` / `a"` - Inside/Around double quotes
- `i'` / `a'` - Inside/Around single quotes
- `i`` / `a`` - Inside/Around backticks
- `it` / `at` - Inside/Around HTML/XML tags

### Common Text Object Operations
- `daw` - Delete around word (including spaces)
- `diw` - Delete inside word (word only)
- `dap` - Delete around paragraph
- `dip` - Delete inside paragraph
- `di"` - Delete inside quotes
- `da"` - Delete around quotes (including quotes)
- `di(` - Delete inside parentheses
- `da(` - Delete around parentheses (including parens)
- `ci"` - Change inside quotes
- `ca"` - Change around quotes
- `yip` - Copy paragraph
- `vip` - Select paragraph

### Function Operations (language-dependent)
- `daf` - Delete around function (with treesitter)
- `dif` - Delete inside function (with treesitter)
- `vaf` - Select around function
- `vif` - Select inside function

## Custom Keybinds (Your Setup)

### File Operations
- `<leader>e` - Toggle file explorer (NvimTree)
- `<leader>ff` - Find files (Telescope)
- `<leader>fg` - Live grep/search in files (Telescope)

### Movement & Navigation
- `Ctrl+d` - Half page down (cursor stays centered)
- `Ctrl+u` - Half page up (cursor stays centered)
- `n` - Next search result (centered)
- `N` - Previous search result (centered)
- `J` (visual mode) - Move selected lines down
- `K` (visual mode) - Move selected lines up
- `<leader>0` - End of line (alternative to $)

### Line Operations
- `J` (normal mode) - Join lines (cursor stays in place)

### Clipboard & Paste
- `<leader>y` - Copy to system clipboard
- `<leader>Y` - Copy line to system clipboard
- `<leader>p` (visual mode) - Paste without losing clipboard
- `<leader>d` - Delete without affecting clipboard

### LSP (Language Server) - Auto-loaded when available
- `gd` - Go to definition
- `K` - Show hover information
- `<leader>vws` - Workspace symbol search
- `<leader>vd` - Show diagnostic float
- `<leader>vca` - Code actions
- `<leader>vrr` - Show references
- `<leader>vrn` - Rename symbol
- `Ctrl+h` (insert mode) - Signature help
- `[d` - Next diagnostic
- `]d` - Previous diagnostic

### Search & Replace
- `<leader>s` - Search and replace word under cursor
- `/` - Search forward
- `?` - Search backward

### Quickfix Navigation
- `Ctrl+k` - Next quickfix item
- `Ctrl+j` - Previous quickfix item
- `<leader>k` - Next location list item
- `<leader>j` - Previous location list item

### Code Formatting
- `<leader>f` - Format current buffer

### Markdown
- `<leader>mp` - Markdown preview
- `<leader>ms` - Markdown preview stop
- `<leader>mt` - Markdown preview toggle

### Utility
- `<leader><leader>` - Reload config
- `Ctrl+c` (insert mode) - Alternative escape
- `Q` - Disabled (no-op)

## 🔥 REPL & Data Science (Iron.nvim)

### REPL Management
- `<leader>rs` - Start REPL (choose Python, Lua, etc.)
- `<leader>rr` - Restart REPL
- `<leader>rF` - Focus REPL window
- `<leader>rh` - Hide REPL window

### Sending Code to REPL
- `<leader>rf` - Send entire file to REPL
- `<leader>rl` - Send current line to REPL
- `<leader>rp` - Send paragraph to REPL (perfect for code blocks)
- `<leader>rc` - Send motion/visual selection to REPL
  - Example: `<leader>rc` + `ip` = send paragraph
  - Example: `<leader>rc` + `i"` = send inside quotes
  - Example: Visual select + `<leader>rc` = send selection
- `<leader>ru` - Send from top of file to cursor

### REPL Control
- `<leader>r<cr>` - Send Enter to REPL
- `<leader>r<space>` - Interrupt REPL (Ctrl+C)
- `<leader>rx` - Clear REPL screen
- `<leader>rq` - Exit REPL

### Data Science Shortcuts
- `<leader>ri` - Auto-import data science libraries (pandas, numpy, matplotlib, sklearn)
- `<leader>rm` - Setup matplotlib with nice defaults

### REPL Workflow Example
1. `<leader>rs` → select `python` (start Python REPL)
2. `<leader>ri` (import pandas, numpy, matplotlib, etc.)
3. `<leader>rm` (setup matplotlib for nice plots)
4. `<leader>rp` (send code paragraph to REPL)
5. See results instantly in REPL window!

## Completion (Auto-loaded)
- `Tab` - Next completion item
- `Shift+Tab` - Previous completion item
- `Enter` - Confirm completion

## Visual Mode Specific
- `>` - Indent selection
- `<` - Unindent selection
- `=` - Auto-format selection

## Window Management
- `Ctrl+w h/j/k/l` - Navigate between windows
- `Ctrl+w s` - Split horizontally
- `Ctrl+w v` - Split vertically
- `Ctrl+w q` - Close window

## Useful Commands (type in command mode with `:`)
- `:w` - Save file
- `:q` - Quit
- `:wq` - Save and quit
- `:q!` - Quit without saving
- `:e filename` - Edit file
- `:vs filename` - Open file in vertical split
- `:sp filename` - Open file in horizontal split
- `:Lazy` - Open Lazy.nvim plugin manager
- `:Mason` - Open Mason LSP installer
- `:TSUpdate` - Update Treesitter parsers
- `:checkhealth` - Check Neovim health
- `:IronRepl` - Start REPL manually
- `:IronRestart` - Restart REPL manually

## File Explorer (NvimTree) - When open
- `Enter` - Open file/folder
- `o` - Open file/folder
- `a` - Create new file/folder
- `d` - Delete
- `r` - Rename
- `x` - Cut
- `c` - Copy
- `p` - Paste
- `R` - Refresh
- `H` - Toggle hidden files
- `q` - Close tree

## Telescope (Fuzzy Finder) - When open
- `Ctrl+n/Ctrl+p` - Navigate results
- `Ctrl+j/Ctrl+k` - Navigate results
- `Enter` - Select item
- `Ctrl+x` - Open in horizontal split
- `Ctrl+v` - Open in vertical split
- `Ctrl+t` - Open in new tab
- `Esc` - Close telescope

## Text Objects Cheat Sheet

### Delete Operations
- `daw` - Delete word + surrounding spaces
- `diw` - Delete word only
- `dap` - Delete paragraph + blank lines
- `dip` - Delete paragraph content only
- `das` - Delete sentence + surrounding spaces
- `dis` - Delete sentence only
- `di"` - Delete text inside quotes
- `da"` - Delete text + quotes
- `di(` - Delete inside parentheses
- `da(` - Delete parentheses + content
- `di{` - Delete inside braces
- `da{` - Delete braces + content

### Change Operations (same patterns)
- `caw` - Change word + spaces
- `ciw` - Change word only
- `cip` - Change paragraph
- `ci"` - Change inside quotes
- `ca"` - Change quotes + content

### Copy Operations (same patterns)
- `yaw` - Copy word + spaces
- `yip` - Copy paragraph
- `yi"` - Copy inside quotes

## Pro Tips
- **Leader key is `Space`** - so `<leader>ff` means press Space then f then f
- **Text objects are powerful** - Learn `dip`, `daw`, `ci"`, etc. for efficient editing
- **REPL workflow** - Use `<leader>rp` to send code blocks and see results instantly
- **Visual line selection + J/K** - Select lines and move them up/down
- **Centered scrolling** - Ctrl+d/u keeps you oriented while scrolling
- **System clipboard** - Use `<leader>y` to copy things you want to paste outside Neovim
- **Word replacement** - `<leader>s` lets you quickly replace all instances of a word
- **Auto-formatting** - `<leader>f` formats your code according to language standards
- **Combine motions** - `<leader>rc` + any motion sends that text to REPL
- **Data science flow** - Write code in paragraphs separated by blank lines, use `<leader>rp` to run each section
