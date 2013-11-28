import sublime, sublime_plugin, copy, os

class TestRunCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		if len(self.view.symbols()) == 0:
			sublime.error_message('This File is not a PHP class')
			return

		first_symbol = self.view.symbols()[0]
		region = first_symbol[0]

		class_region = sublime.Region(region.begin() - 6, region.begin() - 1)

		if self.view.substr(class_region) != 'class':
			sublime.error_message('This File is not a PHP class')
			return

		if first_symbol[1][-4:] != 'Test':
			sublime.error_message('This File is not a PHP Test')
			return

		window = self.view.window()
		directory = os.path.dirname(self.view.file_name())

		while not (directory in window.folders()) and not os.path.isfile(directory + '/phpunit.xml'):
			directory = os.path.dirname(directory)

		if not os.path.isfile(directory + '/phpunit.xml'):
			sublime.error_message('No phpunit.xml file found in parent directories')
			return

		test_file = os.path.relpath(self.view.file_name(), directory)
		directory = '/vagrant/' + os.path.relpath(directory, os.path.dirname(window.folders()[0]))
		
		window.run_command('exec', {'cmd': ['vagrant ssh -c "cd {0}; phpunit {1}"'.format(directory, test_file)], 'shell': True, 'syntax': 'Packages/clippings-sublime/SimplePHPUnit.hidden-tmLanguage'} )


