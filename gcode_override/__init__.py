# coding=utf-8
from __future__ import absolute_import
from .gcode_override import GcodeOverridePlugin

__plugin_name__ = "GCODE Override"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = GcodeOverridePlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
