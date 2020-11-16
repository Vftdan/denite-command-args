function! s:c_to_denite_expr()
	return "\<C-u>Denite command/args:" . substitute(getcmdline(), "[\"' :]", '\\\0', 'g') . "\<CR>"
endfunction
cnoremap <expr><silent> <Plug>(denite-command-args<space>to-denite) <SID>c_to_denite_expr()
