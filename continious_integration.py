import sublime, sublime_plugin, webbrowser

class ClippingsTravisCommand(sublime_plugin.WindowCommand):

	def run(self):
		webbrowser.open_new_tab('https://magnum.travis-ci.com/OpenBuildings/Clippings');
