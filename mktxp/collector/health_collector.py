# coding=utf8
## Copyright (c) 2020 Arseniy Kuznetsov
##
## This program is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License
## as published by the Free Software Foundation; either version 2
## of the License, or (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.


from mktxp.collector.base_collector import BaseCollector
from mktxp.datasource.health_ds import HealthMetricsDataSource


class HealthCollector(BaseCollector):
    ''' System Health Metrics collector
    '''    
    @staticmethod
    def collect(router_entry):
        health_labels = ['voltage', 'temperature', 'cpu_temperature', 'fan1_speed', 'fan2_speed']
        health_records = HealthMetricsDataSource.metric_records(router_entry, metric_labels = health_labels)   
        if health_records:
            for record in health_records:

                if 'voltage' in record:
                    voltage_metrics = BaseCollector.gauge_collector('system_routerboard_voltage', 'Supplied routerboard voltage', [record, ], 'voltage')
                    yield voltage_metrics

                if 'temperature' in record:
                    temperature_metrics = BaseCollector.gauge_collector('system_routerboard_temperature', 'Routerboard current temperature', [record, ], 'temperature')
                    yield temperature_metrics

                if 'cpu_temperature' in record:
                    cpu_temperature_metrics = BaseCollector.gauge_collector('system_cpu_temperature', 'CPU current temperature', [record, ], 'cpu_temperature')
                    yield cpu_temperature_metrics

                if 'fan1_speed' in record:
                    fan_one_speed_metrics = BaseCollector.gauge_collector('system_fan_one_speed', 'System fan 1 current speed', [record, ], 'fan1_speed')
                    yield fan_one_speed_metrics

                if 'fan2_speed' in record:
                    fan_two_speed_metrics = BaseCollector.gauge_collector('system_fan_two_speed', 'System fan 2 current speed', [record, ], 'fan2_speed')
                    yield fan_two_speed_metrics
