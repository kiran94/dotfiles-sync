" ------------------------ PLUGINS ------------------------------------
call plug#begin('~/.vim/plugged')
Plug 'mhinz/vim-startify'
Plug 'mhinz/vim-signify'
Plug 'vim-airline/vim-airline'
Plug 'airblade/vim-gitgutter'
" Plug 'vim-syntastic/syntastic'
Plug 'bronson/vim-trailing-whitespace'
Plug 'tpope/vim-commentary'
Plug 'dstein64/vim-win'
Plug 'farmergreg/vim-lastplace'
Plug 'ctrlpvim/ctrlp.vim'
Plug 'mg979/vim-visual-multi'
Plug 'davidhalter/jedi-vim'
Plug 'jmcantrell/vim-virtualenv'
" Plug 'OmniSharp/omnisharp-vim'
Plug 'preservim/nerdtree'
Plug 'rafi/awesome-vim-colorschemes'
Plug 'bagrat/vim-buffet'
Plug 'Yggdroot/indentLine'
Plug 'jiangmiao/auto-pairs'
Plug 'frazrepo/vim-rainbow'
Plug 'mileszs/ack.vim'
Plug 'tc50cal/vim-terminal'
Plug 'inside/vim-search-pulse'
Plug 'gko/vim-coloresque'
Plug 'sheerun/vim-polyglot'
Plug 'editorconfig/editorconfig-vim'
Plug 'tpope/vim-surround'
Plug 'liuchengxu/vim-which-key'
Plug 'puremourning/vimspector'

if v:version > 703
    " https://github.com/neoclide/coc.nvim/issues/691
    let g:coc_global_extensions = ['coc-highlight', 'coc-python', 'coc-omnisharp','coc-clangd','coc-json', 'coc-markdownlint', 'coc-sh', 'coc-sql']
    Plug 'neoclide/coc.nvim', {'do': { -> coc#util#install()  } }
end

" let g:airline#extensions#syntastic#enabled = 1
let g:airline_detect_spell = 0
call plug#end()

" ------------------------ General Settings ---------------------------

nnoremap <SPACE> <Nop>
let mapleader = " "

set encoding=UTF-8
set ffs=unix,dos,mac
set updatetime=100
set number relativenumber
set autoread
set ruler
set wildmode=longest,list,full
set wildmenu
set cmdheight=1
set hid
set showcmd

set spell
set spelllang=en_gb
set confirm
set backspace=indent,eol,start
set nocompatible
set mouse=a
if has("patch-8.1.1564")
    set signcolumn=number
else
    set signcolumn=yes
endif

" Split
set splitbelow
set splitright

" Search
set ignorecase
set smartcase
set hlsearch
set incsearch
set lazyredraw
set showmatch

" Bell
set noerrorbells
set novisualbell
set t_vb=
set tm=500

" File
filetype plugin on
filetype indent on
set tabstop=4
set shiftwidth=4
set expandtab
set smarttab
set cursorline

" Backup
set nobackup
set nowb
set noswapfile

set termguicolors

autocmd FileType * setlocal formatoptions-=c formatoptions-=r formatoptions-=o
nnoremap <silent> <leader> :WhichKey '<Space>'<CR>

" Highlight
if v:version < 703
    highlight clear SignColumn
end

color oceanic_material

" ------------------------ KEYWORD MAPPINGS ------------------------------------

" Navigating Panes
nnoremap <C-h> <C-W>h
nnoremap <C-j> <C-W>j
nnoremap <C-k> <C-W>k
nnoremap <C-l> <C-W>l

nnoremap <C-Left> <C-W>h
nnoremap <C-Down> <C-W>j
nnoremap <C-Up> <C-W>k
noremap <C-Right> <C-W>l

imap ii <esc>
inoremap <leader><tab> <esc>
inoremap <leader>s :wq
" Navigating Tabs
nmap <leader>t :tabnew<CR>
nmap <leader>q :q<CR>
nmap <leader>1 <Plug>BuffetSwitch(1)
nmap <leader>2 <Plug>BuffetSwitch(2)
nmap <leader>3 <Plug>BuffetSwitch(3)
nmap <leader>4 <Plug>BuffetSwitch(4)
nmap <leader>5 <Plug>BuffetSwitch(5)
nmap <leader>6 <Plug>BuffetSwitch(6)
nmap <leader>7 <Plug>BuffetSwitch(7)
nmap <leader>8 <Plug>BuffetSwitch(8)
nmap <leader>9 <Plug>BuffetSwitch(9)
nmap <leader>0 <Plug>BuffetSwitch(10)

" Terminal
if v:version < 703
    nmap <C-j> :TerminalTab bash<CR>
    nmap <C-J> :TerminalVSplit bash<CR>
else
    nmap<C-j> :terminal<CR>
    imap<C-j> :q<CR>
    hi Terminal ctermbg=black ctermfg=white guibg=black guifg=white
endif

" Other Things
map <C-o> :NERDTreeToggle<CR>
map <C-c> :Commentary<CR>
nmap <C-I> gg=G<CR>
" nmap <C-w> :w<CR>

" Disabled Keys
nnoremap Q <nop>
" nnoremap <TAB> <nop>
nnoremap ` <nop>

let g:buffet_powerline_separators = 1
let g:buffet_show_index = 1
let g:buffet_tab_icon = '🎉'
let g:buffet_new_buffer_name = '🔴'
" let g:buffet_modified_icon = '🟡'
let g:rainbow_active = 1

function! g:BuffetSetCustomColors()
    " cterm colors https://jonasjacek.github.io/colors/
    hi! BuffetCurrentBuffer cterm=NONE ctermbg=27 ctermfg=15 guibg=#466adf guifg=#FFFFFF
    hi! BuffetTrunc cterm=bold ctermbg=66 ctermfg=8 guibg=#458588 guifg=#000000
    hi! BuffetBuffer cterm=NONE ctermbg=239 ctermfg=8 guibg=#504945 guifg=#000000
    hi! BuffetTab cterm=NONE ctermbg=66 ctermfg=8 guibg=#458588 guifg=#000000
    hi! BuffetActiveBuffer cterm=NONE ctermbg=10 ctermfg=239 guibg=#999999 guifg=#504945
endfunction

" ------------------------ AUTOCOMPLETE ------------------------------------


if v:version > 703
    let g:airline#extensions#coc#enabled = 1

    " tab for trigger completion with characters ahead and navigate.
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

    " Use <c-space> to trigger completion.
    if has('nvim')
        inoremap <silent><expr> <c-space> coc#refresh()
    else
        inoremap <silent><expr> <c-@> coc#refresh()
    endif

    " Make <CR> auto-select the first completion item and notify coc.nvim to
    " format on enter, <cr> could be remapped by other vim plugin
    inoremap <silent><expr> <cr> pumvisible() ? coc#_select_confirm()
                \: "\<C-g>u\<CR>\<c-r>=coc#on_enter()\<CR>"

    " Use `[g` and `]g` to navigate diagnostics
    " Use `:CocDiagnostics` to get all diagnostics of current buffer in location list.
    nmap <silent> [g <Plug>(coc-diagnostic-prev)
    nmap <silent> ]g <Plug>(coc-diagnostic-next)

    " GoTo code navigation.
    nmap <silent> gd <Plug>(coc-definition)
    nmap <silent> gy <Plug>(coc-type-definition)
    nmap <silent> gi <Plug>(coc-implementation)
    nmap <silent> gr <Plug>(coc-references)

    " Use K to show documentation in preview window.
    nnoremap <silent> K :call <SID>show_documentation()<CR>

    function! s:show_documentation()
        if (index(['vim','help'], &filetype) >= 0)
            execute 'h '.expand('<cword>')
        elseif (coc#rpc#ready())
            call CocActionAsync('doHover')
        else
            execute '!' . &keywordprg . " " . expand('<cword>')
        endif
    endfunction

    " Highlight the symbol and its references when holding the cursor.
    autocmd CursorHold * silent call CocActionAsync('highlight')

    " Symbol renaming.
    nmap <leader>rn <Plug>(coc-rename)

    " Formatting selected code.
    xmap <leader>f  <Plug>(coc-format-selected)
    nmap <leader>f  <Plug>(coc-format-selected)

    augroup mygroup
        autocmd!
        " Setup formatexpr specified filetype(s).
        autocmd FileType typescript,json setl formatexpr=CocAction('formatSelected')
        " Update signature help on jump placeholder.
        autocmd User CocJumpPlaceholder call CocActionAsync('showSignatureHelp')
    augroup end

    " Applying codeAction to the selected region.
    " Example: `<leader>aap` for current paragraph
    xmap <leader>a  <Plug>(coc-codeaction-selected)
    nmap <leader>a  <Plug>(coc-codeaction-selected)

    " Remap keys for applying codeAction to the current buffer.
    nmap <leader>ac  <Plug>(coc-codeaction)
    " Apply AutoFix to problem on the current line.
    nmap <leader>qf  <Plug>(coc-fix-current)

    " Map function and class text objects
    " NOTE: Requires 'textDocument.documentSymbol' support from the language server.
    xmap if <Plug>(coc-funcobj-i)
    omap if <Plug>(coc-funcobj-i)
    xmap af <Plug>(coc-funcobj-a)
    omap af <Plug>(coc-funcobj-a)
    xmap ic <Plug>(coc-classobj-i)
    omap ic <Plug>(coc-classobj-i)
    xmap ac <Plug>(coc-classobj-a)
    omap ac <Plug>(coc-classobj-a)

    " Remap <C-f> and <C-b> for scroll float windows/popups.
    " Note coc#float#scroll works on neovim >= 0.4.3 or vim >= 8.2.0750
    nnoremap <nowait><expr> <C-f> coc#float#has_scroll() ? coc#float#scroll(1) : "\<C-f>"
    nnoremap <nowait><expr> <C-b> coc#float#has_scroll() ? coc#float#scroll(0) : "\<C-b>"
    inoremap <nowait><expr> <C-f> coc#float#has_scroll() ? "\<c-r>=coc#float#scroll(1)\<cr>" : "\<Right>"
    inoremap <nowait><expr> <C-b> coc#float#has_scroll() ? "\<c-r>=coc#float#scroll(0)\<cr>" : "\<Left>"

    " NeoVim-only mapping for visual mode scroll
    " Useful on signatureHelp after jump placeholder of snippet expansion
    if has('nvim')
        vnoremap <nowait><expr> <C-f> coc#float#has_scroll() ? coc#float#nvim_scroll(1, 1) : "\<C-f>"
        vnoremap <nowait><expr> <C-b> coc#float#has_scroll() ? coc#float#nvim_scroll(0, 1) : "\<C-b>"
    endif

    " Use CTRL-S for selections ranges.
    " Requires 'textDocument/selectionRange' support of language server.
    nmap <silent> <C-s> <Plug>(coc-range-select)
    xmap <silent> <C-s> <Plug>(coc-range-select)

    " Add `:Format` command to format current buffer.
    command! -nargs=0 Format :call CocAction('format')

    " Add `:Fold` command to fold current buffer.
    command! -nargs=? Fold :call     CocAction('fold', <f-args>)

    " Add `:OR` command for organize imports of the current buffer.
    command! -nargs=0 OR   :call     CocAction('runCommand', 'editor.action.organizeImport')

    " Add (Neo)Vim's native statusline support.
    " NOTE: Please see `:h coc-status` for integrations with external plugins that
    " provide custom statusline: lightline.vim, vim-airline.
    set statusline^=%{coc#status()}%{get(b:,'coc_current_function','')}

    " Mappings for CoCList
    " Show all diagnostics.
    nnoremap <silent><nowait> <space>a  :<C-u>CocList diagnostics<cr>
    " Manage extensions.
    nnoremap <silent><nowait> <space>e  :<C-u>CocList extensions<cr>
    " Show commands.
    nnoremap <silent><nowait> <space>c  :<C-u>CocList commands<cr>
    " Find symbol of current document.
    nnoremap <silent><nowait> <space>o  :<C-u>CocList outline<cr>
    " Search workspace symbols.
    nnoremap <silent><nowait> <space>s  :<C-u>CocList -I symbols<cr>
    " Do default action for next item.
    nnoremap <silent><nowait> <space>j  :<C-u>CocNext<CR>
    " Do default action for previous item.
    nnoremap <silent><nowait> <space>k  :<C-u>CocPrev<CR>
    " Resume latest coc list.
    nnoremap <silent><nowait> <space>p  :<C-u>CocListResume<CR>

endif

syntax enable
