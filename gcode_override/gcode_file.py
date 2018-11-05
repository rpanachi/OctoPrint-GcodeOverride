# coding=utf-8

from   threading import Thread, Timer
import threading
import os
import re

class GCodeFile:

    travel_speed    = 0
    travel_feedrate = 0

    def __init__(self, file_selected_payload):
        self.file_name = file_selected_payload['name']
        self.local = file_selected_payload['origin'] == 'local'
        self.file_path = file_selected_payload['file']

    def analyze(self):
        if self.local:
            self.file_size = os.path.getsize(self.file_path)
            gcode = file(self.file_path, "r")
            file_size = os.path.getsize(self.file_path)
            self.get_print_job_layer_information(gcode, file_size)

    def get_print_job_layer_information(self, gcode, file_size):
        regex = re.compile('(F\d+)')

        for line in gcode:
            # Parse line into components
            line_components = self.parse_line(line)
            if not line_components:
                continue

            gCode = line_components[0]
            if gCode == 'G0':
                feedrate = regex.search(line)
                if feedrate:
                    self.travel_speed = feedrate.group(0)
                    print("REGEX G0 TRAVEL: %s" % self.travel_speed)

    def strip_comment(self, line):
        comment_pos = line.find(';')
        if comment_pos == -1:
            return line
        return line[:comment_pos].strip()

    def parse_line(self, line):
        line = self.strip_comment(line)
        if len(line) == 0:
            return None
        if line.find('(') != -1:
            return None
        return line.split()
