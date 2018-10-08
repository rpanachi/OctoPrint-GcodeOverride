# coding=utf-8

import octoprint.plugin

class GcodeOverridePlugin(octoprint.plugin.StartupPlugin,
                          octoprint.plugin.SettingsPlugin,
                          octoprint.plugin.AssetPlugin,
                          octoprint.plugin.TemplatePlugin):

	def __init__(self):
                # noting
		return

	def get_settings_defaults(self):
		return dict(
			# put your plugin's default settings here
		)

	def get_assets(self):
		# Define your plugin's asset files to automatically include in the
		# core UI here.
		return dict(
			js=["js/gcode_override.js"],
			css=["css/gcode_override.css"],
			less=["less/gcode_override.less"]
		)

	def get_update_information(self):
		# Define the configuration for your plugin to use with the Software Update
		# Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
		# for details.
		return dict(
			gcode_override=dict(
				displayName="Gcode Override Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="rpanachi",
				repo="OctoPrint-GcodeOverride",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/rpanachi/OctoPrint-GcodeOverride/archive/{target_version}.zip"
			)
		)

        def on_after_startup(self):
                self._logger.info("[DEBUG] GCODE OVERRIDE: After Startup")
