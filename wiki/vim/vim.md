#project | project:vim
* [X] learn vimwiki  #69e9360e
* [X] win_shift  #78812a11
* [X] learn some advanced taskwiki utilities  #2071c18f
* [X] add some function that can add tags(project) to task  #1733172b
* [X] auto generate log info when we check a task as done  #293704af
* [X] search for best practice  #6e5bd1cb
* [X] learn teej's mapping  #d708619c
* [X] modify vim config structure according to teej's solution  #fea5dbf2
* [ ] shift to lua  #3a2c040f
* [ ] figure out how to link task with the workspace we pin the task down  #fcfdc651

## Note
1. when add a task ,don't add at a diary view point ,add at corresponding wiki page
2. some note about init order and after file and lazy loading:
	1. user define config -> plugin -> after -> vimEnter
	2. later one will override previous one
	3. but because of lazy loading ,filetype specific setting will override all
	4. check loaded file by :scriptnames
	5. check set order by :verbose [setting cmd]
3. read command line result:
	1. execute("!the cmd you want to execute") will return cmd and return value
	2. system("cmd") only return return value
	3. to remove trailing new line, do the following
	4. :let s = substitute(system('echo dani'), '\n\+$', '', '')
	5. to print unprintable char use strtrans()

4. Config Structure:
 
function! cmake#util#FindProjectRoot() abort
    let l:root = getcwd()
    let l:escaped_cwd = fnameescape(getcwd())
    for l:marker in g:cmake_root_markers
        " Search CWD upward for l:marker, assuming it is a file.
        let l:marker_path = findfile(l:marker, l:escaped_cwd . ';' . $HOME)
        if len(l:marker_path)
            " If found, get absolute path and strip l:marker from it.
            let l:root = fnamemodify(l:marker_path, printf(
                    \ ':.:s?%s??:h', l:marker_path))
            break
        endif
        " Search CWD upward for l:marker, assuming it is a directory.
        let l:marker_path = finddir(l:marker, l:escaped_cwd . ';' . $HOME)
        if len(l:marker_path)
            " If found, get absolute path and strip l:marker from it.
            let l:root = fnamemodify(l:marker_path, printf(
                    \ ':.:s?%s/??:h', l:marker_path))
            break
        endif
    endfor
    return l:root
endfunction
