# coding=utf-8

import octoprint.plugin
import os
import octoprint.filemanager
import octoprint.filemanager.util

class custombackground(octoprint.plugin.AssetPlugin,
				octoprint.plugin.TemplatePlugin,
                octoprint.plugin.SettingsPlugin):
	
	##-- AssetPlugin hooks
	def get_assets(self):
		return dict(js=["js/custombackground.js"])
		
	##-- Settings hooks
	def get_settings_defaults(self):
		return dict(background_url="/static/img/graph-background.png",fillMethod="cover")
	
	##-- Template hooks
	def get_template_configs(self):
		return [dict(type="settings",custom_bindings=True)]

	##-- Image upload extenstion tree hook
	def get_extension_tree(self, *args, **kwargs):
		return dict(
			machinecode=dict(
				custombackground=["jpg", "bmp", "png", "gif"]
			)
		)
	
	##~~ Image upload preprocessor hook	
	def custombackgroundupload(self, path, file_object, links=None, printer_profile=None, allow_overwrite=True, *args, **kwargs):
		img_extensions = [".jpg", ".bmp", ".png", ".gif"]
		name, extension = os.path.splitext(file_object.filename)
		if extension in img_extensions:
			self._logger.info("Setting background url for " + path)
			#file_object.save(self.get_plugin_data_folder() + "/uploaded" + extension)
			octoprint.filemanager.util.StreamWrapper(self.get_plugin_data_folder() + "/uploaded" + extension, file_object.stream()).save(self.get_plugin_data_folder() + "/uploaded" + extension)
			self._logger.info(self.get_plugin_data_folder() + "/uploaded" + extension)
			self._settings.set(["background_url"],"/plugin/custombackground/uploaded" + extension)
			self._settings.save()
			self._plugin_manager.send_plugin_message(self._identifier, dict(type="reload"))
		return file_object
		
	##~~ Routes hook
	def route_hook(self, server_routes, *args, **kwargs):
		from octoprint.server.util.tornado import LargeResponseHandler, UrlProxyHandler, path_validation_factory
		from octoprint.util import is_hidden_path

		return [
				(r"/(.*)", LargeResponseHandler, dict(path=self.get_plugin_data_folder(),
																as_attachment=True,
																path_validation=path_validation_factory(lambda path: not is_hidden_path(path),status_code=404)))
				]
		
	##~~ Softwareupdate hook
	def get_version(self):
		return self._plugin_version
		
	def get_update_information(self):
		return dict(
			custombackground=dict(
				displayName="Custom Background",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="jneilliii",
				repo="OctoPrint-CustomBackground",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/jneilliii/OctoPrint-CustomBackground/archive/{target_version}.zip"
			)
		)

__plugin_name__ = "Custom Background"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = custombackground()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information,
		"octoprint.filemanager.extension_tree": __plugin_implementation__.get_extension_tree,
		"octoprint.filemanager.preprocessor": __plugin_implementation__.custombackgroundupload,
		"octoprint.server.http.routes": __plugin_implementation__.route_hook
	}