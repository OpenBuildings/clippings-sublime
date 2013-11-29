import sublime, sublime_plugin, copy
from .clippings import ClippingsClass, ClippingsModule

class TestSwitchCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		cl_class = ClippingsClass(self.view)
		
		window = self.view.window()

		if cl_class.is_test():
			new_class = cl_class.view_class[:-4]
		else:
			new_class = cl_class.view_class.replace('Kohana_', '') + 'Test'

		cl_class.module().open_class(new_class)
