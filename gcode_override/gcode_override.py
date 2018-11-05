# coding=utf-8

import octoprint.plugin
from   octoprint.events   import Events
from   octoprint.settings import settings
from   gcode_file         import GCodeFile


class GcodeOverridePlugin(octoprint.plugin.StartupPlugin,
                          octoprint.plugin.SettingsPlugin,
                          octoprint.plugin.AssetPlugin,
                          octoprint.plugin.TemplatePlugin,
                          octoprint.plugin.EventHandlerPlugin,
                          octoprint.printer.PrinterCallback):
    gcode_file = None

    def on_event(self, event, payload):
        if event == Events.FILE_SELECTED:
            self._logger.info("Gcode file selected: %s" % payload["name"])
            gcode_file = GCodeFile(payload)
            gcode_file.analyze()

            self._logger.info("GCode Analysis Complete. Travel Speed: %s", gcode_file.travel_speed)
            self._plugin_manager.send_plugin_message(self._plugin_name, dict(travel_speed = gcode_file.travel_speed))

    def push_analysis_info(self):
        self._logger.info("Push Info - Travel Speed: %s", self.travel_speed)
        self._plugin_manager.send_plugin_message(self._plugin_name, dict(travel_speed = travel_speed))

    def get_settings_defaults(self):
        return dict(feedrate_multiplier="60")

    def get_template_configs(self):
        return [
            dict(type="settings", custom_bindings=False),
            dict(type="tab", custom_bindings=False)
        ]

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
                displayName="GCODE Override Plugin",
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
        self._logger.info("[DEBUG] GCODE OVERRIDE: Feedrate Multiplier = %s" % self._settings.get(["feedrate_multiplier"]))
