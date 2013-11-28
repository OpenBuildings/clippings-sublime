import sublime, sublime_plugin, os, json, sys

class ClippingsCheckoutPackageCommand(sublime_plugin.WindowCommand):

	packages = []

	def load_composer_packages(self):
		project = self.window.project_data()
		project_dir = os.path.dirname(self.window.project_file_name())

		composer_file = os.path.join(project_dir, 'clippings', 'composer.lock')
		
		fp = open(composer_file, mode="r", encoding='utf-8')
		data = json.load(fp)
		fp.close()
		self.packages = data['packages']

	def run(self):
		self.load_composer_packages()
		names = [[p['name'], p['description'], p['version']] for p in self.packages]
		self.window.show_quick_panel(names, self.on_done)

	def on_done(self, picked):
		sublime.status_message(self.packages[picked]['name'])
