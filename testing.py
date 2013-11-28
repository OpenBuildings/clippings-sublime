import sublime, sublime_plugin, copy

class ToggleTestCommand(sublime_plugin.TextCommand):

	def on_picked(self, picked):
		sublime.status_message(picked)

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

		window = self.view.window()

		if first_symbol[1][-4:] == 'Test':
			locations = window.lookup_symbol_in_index(first_symbol[1][:-4])
		else:
			locations = window.lookup_symbol_in_index(first_symbol[1] + 'Test')

		if len(locations) == 1:
			window.open_file(locations[0][0])
		else:
			names = [l[1] for l in locations]
			window.show_quick_panel(names, lambda picked: window.open_file(locations[picked][0]))


