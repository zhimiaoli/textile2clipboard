import sublime, sublime_plugin
import textile

class t2c(sublime_plugin.WindowCommand):
    def run(self):
		view = self.window.active_view()
		if view:
			if view.substr(view.sel()[0]):
				contents = view.substr(view.sel()[0])
				message = u"selection converted and copied to clipboard"
			else:
				contents = view.substr(sublime.Region(0, view.size()))
				message = u"converted and copied to clipboard"
	        tx = textile.textile(contents)
	        sublime.set_clipboard(tx)
	        sublime.status_message(message)