function! denite_command_args#getcmdcompletion(cmd_prefix)
	let [cwh, ls, ve, v] = [&cwh, &ls, &ve, @v]
	set cwh=1 ls=0 ve=onemore
	try
		silent! execute 'nnoremap <buffer> <Plug>(denite-command-args_aux) :' . a:cmd_prefix . '<c-a><cmd>let @v=getcmdline()<cr><c-u><esc>'
		silent! execute "normal \<Plug>(denite-command-args_aux)"
		" Doesn't work:
		" nunmap <Plug>(denite-command-args_aux)
		let res = split(@v[len(a:cmd_prefix):])
	catch
		res = []
	endtry
	let [&cwh, &ls, &ve, @v] = [cwh, ls, ve, v]
	return res
endfunction
