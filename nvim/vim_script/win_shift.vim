function If_left_most(layout_list)
	let l:id = win_getid()
	if a:layout_list[0] == "leaf"
		if a:layout_list[1] == l:id
			return 1 
		else
			return 0
		endif
	elseif a:layout_list[0] == "col"
		for l:win in a:layout_list[1]
			if If_left_most(l:win)
				return 1
			endif
			return 0
		endfor
	elseif a:layout_list[0] == "row"
		if If_left_most(a:layout_list[1][0])
			return 1
		else
			return 0
		endif
	endif
endfunction

function If_right_most(layout_list)
	let l:id = win_getid()
	if a:layout_list[0] == "leaf"
		if a:layout_list[1] == l:id
			return 1 
		else
			return 0
		endif
	elseif a:layout_list[0] == "col"
		for l:win in a:layout_list[1]
			if If_left_most(l:win)
				return 1
			endif
			return 0
		endfor
	elseif a:layout_list[0] == "row"
		if If_left_most(a:layout_list[1][-1])
			return 1
		else
			return 0
		endif
	endif
endfunction

function Win_shift_left()
	if If_left_most(winlayout())
		tabp
	else
		exe "normal \<c-w>h"
	endif
		
endfunction

function Win_shift_right()
	if If_right_most(winlayout())
		tabn
	else
		exe "normal \<c-w>l"
	endif
endfunction
