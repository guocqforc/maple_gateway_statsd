# -*- coding: utf-8 -*-

"""
读取gateway统计数据，并上报数据至statsd
"""

from stat_reader import StatReader
import constants


class StatReporter(object):

    # 需要上报gauge的
    gauge_stat_list = constants.GAUGE_STAT_LIST
    # 需要上报incr的
    incr_stat_list = constants.INCR_STAT_LIST

    stat_reader = None
    statsd_client = None
    statsd_prefix = None

    # 统计上报时的命名转化
    statsd_name_converter = None

    # 上次的stat_reader的结果
    last_stat_result = None

    def __init__(self, stat_tool_path, stat_file_path, statsd_client, statsd_name_converter=None):
        """
        :param stat_tool_path: gateway的统计工具
        :param stat_file_path: gateway的统计文件
        :param statsd_client: statsd_client
        :param statsd_name_converter: statsd统计上报名字转换函数
        :return:
        """

        self.stat_reader = StatReader(stat_tool_path, stat_file_path)
        self.statsd_client = statsd_client
        # 默认是不变
        self.statsd_name_converter = lambda x: x

    def report(self):
        """
        上报
        :return:
        """

        result = self.stat_reader.read()

        for gateway_stat_name in self.gauge_stat_list:
            remote_stat_name = self.statsd_name_converter(gateway_stat_name)
            value = result.get(gateway_stat_name, 0)

            self.statsd_client.gauge(remote_stat_name, value)

        if self.last_stat_result is not None:
            for gateway_stat_name in self.incr_stat_list:
                remote_stat_name = self.statsd_name_converter(gateway_stat_name)
                value = result.get(gateway_stat_name, 0) - self.last_stat_result.get(gateway_stat_name, 0)

                self.statsd_client.incr(remote_stat_name, value)

        self.last_stat_result = result

