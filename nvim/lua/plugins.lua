vim.cmd [[packadd packer.nvim]]

require('packer').startup(
	function (use)
	use 'wbthomason/packer.nvim'
	-- use 'preservim/nerdtree'
	-- use 'easymotion/vim-easymotion'
	use 'terryma/vim-expand-region'
	use 'junegunn/vim-easy-align'
	-- use 'mg979/vim-visual-multi'
	use 'neoclide/coc.nvim'
	use 'neovim/nvim-lspconfig'
	use 'nvim-treesitter/nvim-treesitter'
	use 'vim-airline/vim-airline'
	use 'kyazdani42/nvim-web-devicons'
	-- use 'kevinoid/vim-jsonc'
	use 'jiangmiao/auto-pairs'
	use 'VundleVim/Vundle.vim'
	use 'farmergreg/vim-lastplace'
	use 'Yggdroot/indentLine'
	use 'w0ng/vim-hybrid'
	-- use 'mhinz/vim-startify'
	use 'aklt/plantuml-syntax'
	use 'tyru/open-browser.vim'
	use 'scrooloose/vim-slumlord'  --plantuml ascii preview
	use 'weirongxu/plantuml-previewer.vim'
	use 'tpope/vim-fugitive'
	use 'nvim-lua/popup.nvim'
	use 'nvim-lua/plenary.nvim'
	use 'nvim-telescope/telescope.nvim'
	use {'nvim-telescope/telescope-fzf-native.nvim', run = 'make' }
	use 'fannheyward/telescope-coc.nvim'
	use 'python-rope/ropevim'
	use 'honza/vim-snippets'
	use 'szw/vim-maximizer'
	use 'tpope/vim-commentary'
	use 'mattn/emmet-vim'
	use 'puremourning/vimspector'
	use 'voldikss/vim-floaterm'
	use 'morhetz/gruvbox'
	use 'reconquest/vim-pythonx'
	use 'vhda/verilog_systemverilog.vim'
	use 'nvim-treesitter/playground'
	use 'kevinhwang91/rnvimr'
	use 'uzxmx/vim-widgets'
	use 'metakirby5/codi.vim'
	use 'cdelledonne/vim-cmake'
	use 'skywind3000/asynctasks.vim'
	use 'skywind3000/asyncrun.vim'
	use
	{
		"ThePrimeagen/refactoring.nvim",
		requires =
		{
			{"nvim-lua/plenary.nvim"},
			{"nvim-treesitter/nvim-treesitter"}
		}
	}
end)



