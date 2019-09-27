#!/usr/bin/env bash
#存放运行文件
/bin/mkdir "/task"
#存放日志文件
/bin/mkdir "/var/log/monitor"
#创建一个初始文件
/bin/touch "/var/log/monitor/systeminfo.log"
#写入计划任务
echo '*/30 * * * * /bin/bash /task/sysinfo.sh &' >>/var/spool/cron/root