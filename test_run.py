import sublime, sublime_plugin, copy, os
from .clippings import ClippingsClass, ClippingsModule

class TestRunCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		cl_class = ClippingsClass(self.view)

		if not cl_class.is_test():
			sublime.error_message('This File is not a PHP Test')

		cl_module = cl_class.module()

		d = cl_module.vagrant_dir
		f = cl_module.relative_path(cl_class.view_file)

		self.view.window().run_command('exec', {'cmd': ['vagrant ssh -c "cd {0}; phpunit {1}"'.format(d, f)], 'shell': True, 'syntax': 'Packages/clippings-sublime/PHPUnitResult.tmLanguage', 'color_scheme': 'Packages/clippings-sublime/PHPUnitResult.tmTheme'} )


