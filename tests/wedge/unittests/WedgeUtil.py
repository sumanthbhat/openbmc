from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import sys
import os
try:
    currentPath = os.getcwd()
    commonPath = currentPath.replace('wedge/unittests', 'common')
    sys.path.insert(0, commonPath)
except Exception:
    pass
import BaseUtil


class WedgeUtil(BaseUtil.BaseUtil):

    # Sensors
    SensorCmd = '/usr/bin/sensors'

    # Fans
    GetFanCmd = '/usr/local/bin/get_fan_speed.sh 1'
    SetFanCmd = '/usr/local/bin/set_fan_speed.sh 0'
    KillControlCmd = ['/usr/local/bin/watchdog_ctrl.sh off', '/usr/bin/killall -USR1 fand']
    StartControlCmd = 'sh /etc/init.d/setup-fan.sh'

    def get_speed(self, info):
        """
        Supports getting fan speed for wedge
        """
        info = info.split(':')[1].split(',')
        speed = int(info[0])
        return speed

    def get_fan_test(self, info):
        info = info.split('\n')
        goodRead = ['Fan', 'RPMs:']
        for line in info:
            if len(line) == 0:
                continue
            for word in goodRead:
                if word not in line:
                    return False
            val = line.split(':')[1].split(',')
            if len(val) != 2:
                return False
        return True

    # EEPROM
    ProductName = ['Wedge']
    EEPROMCmd = '/usr/bin/weutil'

    # Power Cycle
    PowerCmdOn = '/usr/local/bin/wedge_power.sh on'
    PowerCmdOff = '/usr/local/bin/wedge_power.sh off'
    PowerCmdReset = '/usr/local/bin/wedge_power.sh reset'
    PowerCmdStatus = '/usr/local/bin/wedge_power.sh status'
    PowerHW = 'source /usr/local/bin/board-utils.sh && wedge_is_us_on && echo "OK" || echo "NOK"'

    # sol
    solCmd = '/usr/local/bin/sol.sh'
    solCloseConnection = ['\r', 'CTRL-l', chr(127)]  # send CTRL-l DEL

    def solConnectionClosed(self, info):
        if 'Connection closed' in info:
            return True
        else:
            return False

    # watchdog
    daemonProcessesKill = ['/usr/bin/killall fand']
