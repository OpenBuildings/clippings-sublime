import sublime, sublime_plugin, os

__author__ = "Ivan Kerin"
__copyright__ = "Copyright (c) 2014, Clippings Ltd."
__license__ = "The BSD 3-Clause License"
__version__ = "0.1"

class ClippingsModule:

	directory = ''
	vagrant_dir = ''
	view = ''

	def __init__(self, view):
		self.view = view
		view_file = view.file_name()
		folders = view.window().folders()
		directory = os.path.dirname(view_file)

		while not (directory in folders) and not os.path.isfile(directory + '/phpunit.xml'):
			directory = os.path.dirname(directory)

		if not os.path.isfile(directory + '/phpunit.xml'):
			sublime.error_message('No phpunit.xml file found in parent directories')

		self.directory = directory
		self.vagrant_dir = '/vagrant/' + os.path.relpath(directory, os.path.dirname(folders[0]))

	def relative_path(self, file):
		return os.path.relpath(file, self.directory)

	def open_class(self, class_to_find):
		window = self.view.window()
		locations = window.lookup_symbol_in_index(class_to_find)

		locations = [l for l in locations if l[0].startswith(self.directory)]

		if len(locations) == 0:
			sublime.error_message('No corresponding file found')
		elif (len(locations) == 1):
			window.open_file(locations[0][0])
		else:
			names = [l[1] for l in locations]
			window.show_quick_panel(names, lambda picked: window.open_file(locations[picked][0]))

class ClippingsClass:

	view_file = ''
	view_class = ''
	view = ''

	def __init__(self, view):
		self.view = view
		self.view_file = view.file_name()

		if len(view.symbols()) == 0:
			sublime.error_message('This File is not a PHP class')

		first_symbol = view.symbols()[0]
		region = first_symbol[0]

		class_region = sublime.Region(region.begin() - 6, region.begin() - 1)

		if view.substr(class_region) != 'class':
			sublime.error_message('This File is not a PHP class')

		self.view_class = first_symbol[1]

	def is_test(self):
		return self.view_class[-4:] == 'Test'

	def module(self):
		return ClippingsModule(self.view)

