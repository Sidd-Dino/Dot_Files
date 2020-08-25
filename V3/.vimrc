set encoding=utf-8

set ttymouse=xterm2
set mouse=a
set nowrap
"Vundle settings
"#################################################
set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

	" let Vundle manage Vundle, required
	Plugin 'VundleVim/Vundle.vim'

	"Plugin 'tpope/vim-fugitive'

	Plugin 'vim-airline/vim-airline'
	Plugin 'vim-airline/vim-airline-themes'

	Plugin 'bling/vim-bufferline'

	Plugin 'terryma/vim-multiple-cursors'

	Plugin 'preservim/nerdtree'

	Plugin 'mbbill/undotree'

	"Plugin 'vim-syntastic/syntastic'
	Plugin 'dense-analysis/ale'
	
	Plugin 'jiangmiao/auto-pairs'
	Plugin 'godlygeek/tabular'

	"Plugin 'ycm-core/YouCompleteMe'
	"Plugin 'neoclide/coc.nvim'
	Plugin 'sheerun/vim-polyglot'
	
	Plugin 'maralla/completor.vim'

	Plugin 'mhinz/vim-startify'
	Plugin 'ryanoasis/vim-devicons'

	Plugin 'junegunn/goyo.vim'
	
	Plugin 'dylanaraps/wal.vim'
	Bundle 'https://github.com/gorodinskiy/vim-coloresque.git'

call vundle#end()        
filetype plugin indent on

syntax on

colorscheme wal

"tabular Settings
"#################################################
let g:indentguides_ignorelist = ['text']
let g:indentguides_spacechar = '┆'
let g:indentguides_tabchar = '|'

"Airline Settings
"#################################################
let g:airline#extensions#tabline#enabled = 1
let g:airline_powerline_fonts = 1
let g:airline_theme='bubblegum'

"completor.vim Settings
"#################################################
let g:completor_python_binary = '/bin/python3.8'
let g:completor_clang_binary = '/bin/clang'

