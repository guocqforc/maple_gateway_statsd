# -*- coding: utf-8 -*-
"""
读取gateway统计数据并解析
"""

import os


class StatReader(object):

    stat_tool_path = None
    stat_file_path = None

    def __init__(self, stat_tool_path, stat_file_path):
        """
        :param stat_tool_path: 工具文件的路径
        :param stat_file_path: 统计文件的路径
        :return:
        """

        self.stat_tool_path = stat_tool_path
        self.stat_file_path = stat_file_path

    def read(self):
        """
        读取一次
        :return:
        """

        cmd = '%s -f %s -l 1' % (self.stat_tool_path, self.stat_file_path)

        result = dict()

        for line in os.popen(cmd):
            values = line.split(':')
            if len(values) == 2:
                result[values[0].strip()] = int(values[1].strip())

        return result
