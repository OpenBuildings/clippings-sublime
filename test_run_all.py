import sublime, sublime_plugin, copy, os
from .clippings import ClippingsModule

class TestRunAllCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		cl_module = ClippingsModule(self.view)

		self.view.window().run_command('exec', {'cmd': ['vagrant ssh -c "cd {0}; phpunit"'.format(cl_module.vagrant_dir)], 'shell': True} )