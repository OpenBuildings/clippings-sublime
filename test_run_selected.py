import sublime, sublime_plugin, copy, os
from .clippings import ClippingsClass, ClippingsModule

class TestRunSelectedCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		cl_class = ClippingsClass(self.view)

		if not cl_class.is_test():
			sublime.error_message('This File is not a PHP Test')

		cl_module = cl_class.module()

		directory = cl_module.vagrant_dir
		class_file = cl_module.relative_path(cl_class.view_file)

		methods = self.view.find_by_selector('entity.name.function.php')
		methods_to_test = {}
		found = None

		for method in methods:
			for index, selection in enumerate(self.view.sel()):
				if method.begin() < selection.begin():
					methods_to_test[index] = self.view.substr(method)

		method_filter = '|'.join(methods_to_test.values())

		self.view.window().run_command('exec', {'cmd': ['vagrant ssh -c "cd {0}; phpunit --filter=\'{1}\' {2} "'.format(directory, method_filter, class_file)], 'shell': True, 'syntax': 'Packages/clippings-sublime/PHPUnitResult.tmLanguage', 'color_scheme': 'Packages/clippings-sublime/PHPUnitResult.tmTheme'} )


