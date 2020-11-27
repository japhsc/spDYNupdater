# spDYN updater

Update your IPv4/IPv6 IP on spdns.de:

## Return codes
```
abuse 		Der Host kann nicht aktualisiert werden, da er aufgrund vorheriger fehlerhafter Updateversuche gesperrt ist.
badauth 	Ein ungültiger Benutzername und/oder ein ungültiges Kennwort wurde eingegeben.
good 		Die Hostname wurde erfolgreich auf die neue IP aktualisiert.
!yours 		Der angegebene Host kann nicht unter diesem Benutzer-Account verwendet werden.
notfqdn 	Der angegebene Host ist kein FQDN.
numhost 	Es wurde versucht, mehr als 20 Hosts in einer Anfrage zu aktualisieren.
nochg 		Die IP hat sich zum letzten Update nicht geändert. Werden innerhalb eines kurzen Zeitraumes weiterhin Updateversuche dieses Hosts vorgenommen, wird dieser für eine bestimmte Zeitspanne keine Updates mehr entgegen nehmen können.
nohost 		Der angegebene Host existiert nicht oder wurde gelöscht.
fatal 		Der angegebene Host wurde manuell deaktiviert. 
```

## Add updater as conjob

edit cronjobs for root
``sudo crontab -e``

```
# after reboot
@reboot python3 /home/pi/spdyn_updater.py

# every 5 minutes
*/5 * * * * python3 /home/pi/spdyn_updater.py

# every hour
@hourly python3 /home/pi/spdyn_updater.py
```

### debug cronjob
list jobs
``crontab -l``

read log messages
``grep CRON /var/log/syslog``

