# coding=utf-8
from __future__ import absolute_import
from .gcode_override import GcodeOverridePlugin

# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "GcodeOverride Plugin"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = GcodeOverridePlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

