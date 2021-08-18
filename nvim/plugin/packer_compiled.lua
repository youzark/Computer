-- Automatically generated packer.nvim plugin loader code

if vim.api.nvim_call_function('has', {'nvim-0.5'}) ~= 1 then
  vim.api.nvim_command('echohl WarningMsg | echom "Invalid Neovim version for packer.nvim! | echohl None"')
  return
end

vim.api.nvim_command('packadd packer.nvim')

local no_errors, error_msg = pcall(function()

  local time
  local profile_info
  local should_profile = false
  if should_profile then
    local hrtime = vim.loop.hrtime
    profile_info = {}
    time = function(chunk, start)
      if start then
        profile_info[chunk] = hrtime()
      else
        profile_info[chunk] = (hrtime() - profile_info[chunk]) / 1e6
      end
    end
  else
    time = function(chunk, start) end
  end
  
local function save_profiles(threshold)
  local sorted_times = {}
  for chunk_name, time_taken in pairs(profile_info) do
    sorted_times[#sorted_times + 1] = {chunk_name, time_taken}
  end
  table.sort(sorted_times, function(a, b) return a[2] > b[2] end)
  local results = {}
  for i, elem in ipairs(sorted_times) do
    if not threshold or threshold and elem[2] > threshold then
      results[i] = elem[1] .. ' took ' .. elem[2] .. 'ms'
    end
  end

  _G._packer = _G._packer or {}
  _G._packer.profile_output = results
end

time([[Luarocks path setup]], true)
local package_path_str = "/home/hyx/.cache/nvim/packer_hererocks/2.1.0-beta3/share/lua/5.1/?.lua;/home/hyx/.cache/nvim/packer_hererocks/2.1.0-beta3/share/lua/5.1/?/init.lua;/home/hyx/.cache/nvim/packer_hererocks/2.1.0-beta3/lib/luarocks/rocks-5.1/?.lua;/home/hyx/.cache/nvim/packer_hererocks/2.1.0-beta3/lib/luarocks/rocks-5.1/?/init.lua"
local install_cpath_pattern = "/home/hyx/.cache/nvim/packer_hererocks/2.1.0-beta3/lib/lua/5.1/?.so"
if not string.find(package.path, package_path_str, 1, true) then
  package.path = package.path .. ';' .. package_path_str
end

if not string.find(package.cpath, install_cpath_pattern, 1, true) then
  package.cpath = package.cpath .. ';' .. install_cpath_pattern
end

time([[Luarocks path setup]], false)
time([[try_loadstring definition]], true)
local function try_loadstring(s, component, name)
  local success, result = pcall(loadstring(s))
  if not success then
    vim.schedule(function()
      vim.api.nvim_notify('packer.nvim: Error running ' .. component .. ' for ' .. name .. ': ' .. result, vim.log.levels.ERROR, {})
    end)
  end
  return result
end

time([[try_loadstring definition]], false)
time([[Defining packer_plugins]], true)
_G.packer_plugins = {
  ["Vundle.vim"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/Vundle.vim"
  },
  ["asyncrun.vim"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/asyncrun.vim"
  },
  ["asynctasks.vim"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/asynctasks.vim"
  },
  ["auto-pairs"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/auto-pairs"
  },
  ["coc.nvim"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/coc.nvim"
  },
  ["codi.vim"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/codi.vim"
  },
  ["emmet-vim"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/emmet-vim"
  },
  gruvbox = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/gruvbox"
  },
  indentLine = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/indentLine"
  },
  ["nvim-lspconfig"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/nvim-lspconfig"
  },
  ["nvim-treesitter"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/nvim-treesitter"
  },
  ["nvim-web-devicons"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/nvim-web-devicons"
  },
  ["open-browser.vim"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/open-browser.vim"
  },
  ["packer.nvim"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/packer.nvim"
  },
  ["plantuml-previewer.vim"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/plantuml-previewer.vim"
  },
  ["plantuml-syntax"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/plantuml-syntax"
  },
  playground = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/playground"
  },
  ["plenary.nvim"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/plenary.nvim"
  },
  ["popup.nvim"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/popup.nvim"
  },
  ["refactoring.nvim"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/refactoring.nvim"
  },
  rnvimr = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/rnvimr"
  },
  ropevim = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/ropevim"
  },
  ["telescope-coc.nvim"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/telescope-coc.nvim"
  },
  ["telescope-fzf-native.nvim"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/telescope-fzf-native.nvim"
  },
  ["telescope.nvim"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/telescope.nvim"
  },
  ["verilog_systemverilog.vim"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/verilog_systemverilog.vim"
  },
  ["vim-airline"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/vim-airline"
  },
  ["vim-cmake"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/vim-cmake"
  },
  ["vim-commentary"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/vim-commentary"
  },
  ["vim-easy-align"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/vim-easy-align"
  },
  ["vim-expand-region"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/vim-expand-region"
  },
  ["vim-floaterm"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/vim-floaterm"
  },
  ["vim-fugitive"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/vim-fugitive"
  },
  ["vim-hybrid"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/vim-hybrid"
  },
  ["vim-lastplace"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/vim-lastplace"
  },
  ["vim-maximizer"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/vim-maximizer"
  },
  ["vim-pythonx"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/vim-pythonx"
  },
  ["vim-slumlord"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/vim-slumlord"
  },
  ["vim-snippets"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/vim-snippets"
  },
  ["vim-widgets"] = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/vim-widgets"
  },
  vimspector = {
    loaded = true,
    path = "/home/hyx/.local/share/nvim/site/pack/packer/start/vimspector"
  }
}

time([[Defining packer_plugins]], false)
if should_profile then save_profiles() end

end)

if not no_errors then
  vim.api.nvim_command('echohl ErrorMsg | echom "Error in packer_compiled: '..error_msg..'" | echom "Please check your config for correctness" | echohl None')
end
