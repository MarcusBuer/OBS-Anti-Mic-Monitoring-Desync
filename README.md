# OBS Anti Mic-Monitoring Desync

This OBS Script is a workaround on issues of audio monitoring desync that can happen due to buffer drift, usually caused by high CPU usage.

If your OBS audio monitoring gets delayed over time, this script might mitigate the issue.


## Installation

You can either download the `AntiMicMonitoringDesync.py` file directly from github, or clone this project using the command `git clone https://github.com/MechanicallyDev/OBS-Anti-Mic-Monitoring-Desync.git`.

To use this script you need to have Python installed on your machine, on the version 3.6 (due to OBS scripting module compatibility) and configure your OBS to locate the Python folder (OBS => Tools->Scripts->Python settings).


## Usage

On OBS, open the scripts panel on Tools->Scripts, click on the `+` button to add a script, and select the script file you downloaded / cloned from github.

On the right side you can select which input device you want to automatically re-sync, and how often the sync should be done.

![OBS Script Panel](https://github.com/MechanicallyDev/OBS-Anti-Mic-Monitoring-Desync/blob/702686b032313de596f1033ca23b11812604900f/script%20panel.png)


## Contributing

Contributions are always welcome! 

If you have any sugestion or issue, please leave an [issue](https://github.com/MechanicallyDev/OBS-Anti-Mic-Monitoring-Desync/issues).


## FAQ

#### What does this script do?

This script disables and immediately re-enables a choosen audio input device in a set interval (default: every minute).

This makes the buffer buildup disapear, forcing OBS to generate a more reasonable buffer, decreasing latency.


#### Does it work on Windows / Linux?

Yes, the script is using the OBS API to get all sources that are inputs (including both audio and video), independently of platform.

If for some reason OBS does not show any sources, please load the script and open an [issue](https://github.com/MechanicallyDev/OBS-Anti-Mic-Monitoring-Desync/issues), including your OBS log (Help menu > Log Files > Upload Current/Last Log File).


#### Can I use this script with more than one input at the same time?

Yes, just copy and paste the `AntiMicMonitoringDesync.py` file several times on a folder, and add several instances of the script on OBS (one for each file). Each instance can control one audio input.


#### Will I notice when the script runs?

It is possible in some instances to notice the monitoring disabling and re-enabling, like when the script runs while the cpu is still in high load, but even then it is barely noticiable, only giving a small noise for a few milliseconds.


#### Will my viewers be able to notice the effect of this script?

No, this script only works on the monitoring side of OBS, the audio continues to be sent to your viewers even while your monitoring is off, so it doesn't affect the audio currenly being recorded or streamed.
