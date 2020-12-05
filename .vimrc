
set encoding=utf-8

set ttymouse=xterm2
set mouse=a
set nowrap

call plug#begin('~/.vim/plugged')
	
	Plug 'preservim/nerdtree'
	Plug 'dense-analysis/ale'
	Plug 'maralla/completor.vim'
	Plug 'junegunn/goyo.vim'
	Plug 'preservim/nerdtree'
	Plug 'iamcco/markdown-preview.nvim', { 'do': { -> mkdp#util#install() }, 'for': ['markdown', 'vim-plug']}

call plug#end()

