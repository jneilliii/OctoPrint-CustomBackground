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
				custombackground=["jpg", "bmp", "png"]
			)
		)
	
	##-- Image upload preprocessor hook	
	def custombackgroundupload(self, path, file_object, links=None, printer_profile=None, allow_overwrite=True, *args, **kwargs):
		img_extensions = [".jpg", ".bmp", ".png"]
		name, extension = os.path.splitext(file_object.filename)
		if extension in img_extensions:
			self._logger.info("Setting background url for " + path)
			self._settings.set(["background_url"],"/downloads/files/local/" + path)
			self._settings.save()
			self._plugin_manager.send_plugin_message(self._identifier, dict(type="reload"))
		return file_object
		
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
		"octoprint.filemanager.preprocessor": __plugin_implementation__.custombackgroundupload
	}