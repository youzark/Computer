local silent = {silent = true}

-- store all (used by other hotkey)
vim.api.nvim_set_keymap('n','<leader>w',':wall<CR>',silent)
-- config vim in new tab
-- vim.api.nvim_set_keymap('n','<leader>cg',':tabnew ~/.config/nvim/lua/',{})
vim.api.nvim_set_keymap('n','<leader>cg','<cmd>tabnew|lua require("telescope.builtin").find_files({hidden=true,search_dirs={"~/.config/nvim"}})<cr>',silent)

-- 0 and $
vim.api.nvim_set_keymap('n','<','0',silent)
vim.api.nvim_set_keymap('n','>','$',silent)
-- window movement and tab movement
vim.api.nvim_set_keymap('n','K','<C-w>k',silent)
vim.api.nvim_set_keymap('n','J','<C-w>j',silent)
vim.api.nvim_set_keymap('n','L','<cmd>call Win_shift_right()<cr>',silent)
vim.api.nvim_set_keymap('n','H','<cmd>call Win_shift_left()<cr>',silent)
-- following two D,F mapping are deprecated
-- vim.api.nvim_set_keymap('n','D','<C-w>hm ',silent)
-- vim.api.nvim_set_keymap('n','F','<C-w>lm ',silent)

-- vim.api.nvim_set_keymap('n','L','<cmd>tabn<cr>',silent)
-- vim.api.nvim_set_keymap('n','H','<cmd>tabp<cr>',silent)
-- quick test
vim.api.nvim_set_keymap('n','<leader>t','<leader>w<cmd>!sh ./test.sh<cr>',{})
-- hyper link
vim.api.nvim_set_keymap('n','gk','<c-]>',silent)
vim.api.nvim_set_keymap('n','gj','<c-o>',silent)
-- write and source
vim.api.nvim_set_keymap('n','<leader>sc','<leader>w<cmd>so %<cr>',silent)
-- judge window position
-- vim.api.nvim_set_keymap('n','<leader>ww','<cmd>echom If_left_most(winlayout())<cr>',{})




-- fugitive
vim.api.nvim_set_keymap('n','<leader>gs',',w<cmd>Git<cr>',silent)
vim.api.nvim_set_keymap('n','<leader>gc','<cmd>Git commit<cr>',silent)
vim.api.nvim_set_keymap('n','<leader>gp','<cmd>Git push<CR>',silent)
-- vim.api.nvim_set_keymap('n','<leader>gc',',w<cmd>Git add .<bar>:Git commit<cr>',silent)
-- vim.api.nvim_set_keymap('n','<leader>gp','<cmd>Git push<CR>',silent)





-- ranger
vim.api.nvim_set_keymap('n','tt',':RnvimrToggle<cr>',silent)


-- easy motion
vim.api.nvim_set_keymap('n','<leader>n','<Plug>(easymotion-w)',silent)

-- easy expand
vim.api.nvim_set_keymap('n','E','<Plug>(expand_region_expand)',silent)
vim.api.nvim_set_keymap('x','S','<Plug>(expand_region_shrink)',silent)

-- easy align
vim.api.nvim_set_keymap('x','ga','<Plug>(EasyAlign)',silent)
vim.api.nvim_set_keymap('n','ga','<Plug>(EasyAlign)',silent)




-- maximizer
vim.api.nvim_set_keymap('n','m','<cmd>MaximizerToggle<cr>',silent)





-- floaterm
vim.api.nvim_set_keymap('n','tn','<cmd>FloatermToggle<cr>',silent)
vim.api.nvim_set_keymap('t','<Esc>','<c-\\><c-n>',silent)

