import sublime, sublime_plugin, copy, os
from .clippings import ClippingsModule

class MinionTestPrepareCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		cl_module = ClippingsModule(self.view)

		self.view.window().run_command('exec', {'cmd': ['vagrant ssh -c "cd {0}; minion db:migrate; minion db:test:load; minion cache:clear"'.format(cl_module.vagrant_dir)], 'shell': True, 'syntax': 'Packages/clippings-sublime/PHPUnitResult.tmLanguage', 'color_scheme': 'Packages/clippings-sublime/PHPUnitResult.tmTheme'} )