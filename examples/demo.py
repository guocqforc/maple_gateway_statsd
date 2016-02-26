# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '../')

from maple_gateway_statsd import StatReporter
from statsd import StatsClient


def main():
    statsd_client = StatsClient()
    maple_gateway_statsd_client = StatReporter(
        'path1',
        'path2',
        statsd_client,
        lambda name: 'cn.vimer.%s' % name
    )
    maple_gateway_statsd_client.report()

if __name__ == '__main__':
    main()
