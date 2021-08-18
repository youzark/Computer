let &packpath = &runtimepath
let mapleader = ","

source ~/.config/nvim/vim_script/win_shift.vim
lua require("init")


let g:floaterm_width=0.95
let g:floaterm_height=0.95

let g:python3_host_prog='~/.venv/bin/python3'

let g:maximizer_set_default_mapping = 0
let g:maximizer_restore_on_winleave = 1

let g:rnvimr_draw_border = 1
let g:rnvimr_enable_picker = 1
highlight link RnvimrNormal CursorLine




"NERDTree
" let NERDTreeShowHidden = 1
" let NERDTreeQuitOnOpen = 3

colorscheme gruvbox

set relativenumber
set ignorecase
set incsearch
set nu
set hidden
set noswapfile
set nobackup
set nofoldenable
set termguicolors
set undofile
set icon
set nocompatible           
set nohlsearch
set foldmethod=indent
set foldnestmax=2
set runtimepath^=~/.vim runtimepath+=~/.vim/after
set signcolumn=yes
set tabstop=4
set shiftwidth=4
set scrolloff=20
set background=dark
set rtp+=~/.fzf
set encoding=utf-8
set cmdheight=2
set updatetime=300
set shortmess+=c
set statusline^=%{coc#status()}
set signcolumn=yes
set clipboard=unnamedplus
set colorcolumn=80
filetype plugin indent on    

iabbrev teh the
iabbrev adn and
iabbrev waht what 

" Use tab for trigger completion with characters ahead and navigate.
" NOTE: Use command ':verbose imap <tab>' to make sure tab is not mapped by
" other plugin before putting this into your config.
inoremap <silent><expr> <TAB>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<TAB>" :
      \ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction


