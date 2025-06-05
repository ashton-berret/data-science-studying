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

## Custom Keybinds (Your New Setup)

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

### Utility
- `<leader><leader>` - Reload config
- `Ctrl+c` (insert mode) - Alternative escape
- `Q` - Disabled (no-op)

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
- `:PackerSync` - Update plugins (if still using Packer)
- `:Lazy` - Open Lazy.nvim plugin manager
- `:Mason` - Open Mason LSP installer (if installed)
- `:TSUpdate` - Update Treesitter parsers
- `:checkhealth` - Check Neovim health

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

## Pro Tips
- **Leader key is `Space`** - so `<leader>ff` means press Space then f then f
- **Visual line selection + J/K** - Select lines and move them up/down
- **Centered scrolling** - Ctrl+d/u keeps you oriented while scrolling
- **System clipboard** - Use `<leader>y` to copy things you want to paste outside Neovim
- **Word replacement** - `<leader>s` lets you quickly replace all instances of a word
- **Auto-formatting** - `<leader>f` formats your code according to language standards
