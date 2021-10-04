# OBS Anti Mic-Monitoring Desync

This OBS Script is a workaround on issues of audio monitoring desync that can happen due to buffer drift, usually caused by high CPU usage, like when loading a game.

If your OBS audio monitoring gets delayed over time, this script may mitigate the issue.


## Installation

You can either download the `AntiMicMonitoringDesync.py` file directly from github, or clone this project using git clone using the command `git clone https://github.com/MechanicallyDev/OBS-Anti-Mic-Monitoring-Desync.git`.

To use this script you need to have Python installed on your machine, on the version 3.6 (due to OBS scripting module compatibility) and configure your OBS to locate the Python folder (Tools->Scripts->Python settings).


## Usage

On OBS, find the script panel on Tools->Scripts, click on the `+` button to add a script, and select the script file you downloaded / cloned from github.
On the right side you can select which input device you want to sync, and how often the sync should be done.

![OBS Script Panel](https://github.com/MechanicallyDev/OBS-Anti-Mic-Monitoring-Desync/blob/702686b032313de596f1033ca23b11812604900f/script%20panel.png)


## Contributing

Contributions are always welcome! If you have any sugestion or issue, please leave an [issue](https://github.com/MechanicallyDev/OBS-Anti-Mic-Monitoring-Desync/issues).


## FAQ

#### What does this script do?

This script disables and immediately re-enables a choosen audio input device in a set interval (default: every minute).
This makes the buffer buildup disapear, forcing OBS to generate a more reasonable buffer, decreasing latency.


#### Can I use this script with more than one input at the same time?

Yes, just copy and paste the `AntiMicMonitoringDesync.py` file several times on the folder, and add several instances on OBS. Each instance can control one audio input.


#### Will I notice when the script runs?

It is possible in some instances to notice the monitoring disabling and re-enabling, like when the script runs while the cpu is still in high load, but even then it is barely noticiable, only giving a small noise for a few milliseconds.


#### Will my viewers be able to notice the effect of this script?

No, this script only works on the monitoring side of OBS, the audio continues to be send to your viewers even while your monitoring is off, so it doesn't affect the audio currenly being recorded or streamed.
