#!/usr/bin/env bash
#
# author: batterm
# date: 2019/08/28
# usage: webserver cpu status
#前提：解决windows传送shell脚本空行问题
#yum -y install dos2unix
#dos2unix sysinfo.sh
DATE=$(date +'%Y-%m-%d %H:%M:%S')
# 检测命令是否存在
if ! which bc &>/dev/null; then
	yum -y install bc-1.06.95-13.el7.x86_64 &>/dev/null
	if [ $? -eq 0 ];then
		echo "bc command installed"
	fi
fi
if ! which vmstat &>/dev/null; then
	yum -y install procps-ng &>/dev/null
	if [ $? -eq 0 ];then
		echo "vmstat command installed"
	fi
fi
#cpu
US=$(vmstat | awk 'BEGIN{ FS=" " }NR==3{ print $13 }')
SY=$(vmstat | awk 'BEGIN{ FS=" " }NR==3{ print $14 }')
ID=$(vmstat | awk 'BEGIN{ FS=" " }NR==3{ print $15 }')
cpuused=$((${US}+${SY}))
#memory
TOTAL=$(free -mw | awk 'BEGIN{ FS=" " }NR==2{ print $2 }')
USE=$(free -mw | awk 'BEGIN{ FS=" " }NR==2{ print $3 }')
FREE=$(free -mw | awk 'BEGIN{ FS=" " }NR==2{ print $4 }')
CACHE=$(free -mw | awk 'BEGIN{ FS=" " }NR==2{ print $7 }')
memused=$(echo "((${USE}+${CACHE})/${TOTAL})*100" | bc -ql)
memfree=$(echo "(${FREE}/${TOTAL})*100" | bc -ql)
#disk
diskused=$(df -Th | awk 'BEGIN{ FS=" " }NR==2{ print $6 }')
fileSize=$(du -sh /var/log/monitor/systeminfo.log | awk '{ print $1 }')
if [ "fileSize" == "2.1M" ];then
  mv /var/log/monitor/systeminfo.{log,log.bak-${DATE}}
  touch /var/log/monitor/systeminfo.log
else
  echo "\"${DATE}\" - \"${HOSTNAME}\" - {\"cpu\":{\"used\":${cpuused},\"idle\":${ID}},\"memory\":{\"used\":${memused},\"free\":${memfree}},\"disk\":{\"used\":\"${diskused}\"}}" >>/var/log/monitor/systeminfo.log
fi
