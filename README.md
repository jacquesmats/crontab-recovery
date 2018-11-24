# Crontab Recovery

This code is for you all out there who deleted accidentaly the crontab file and do not had backup. Maybe because the E key is right next the R key on keyboard!
It was inspired in the PHP code from [@dangreenisrael](https://github.com/dangreenisrael) which saved my life on November, 2018. Since it is very useful and aparently there is no solution once it is done, here it is.
That may sound trivial for a couple of crontab lines, but for a big file with a bunch of projects this can save a lot of time.
The code is writen in Python and there is no need for further extensions. It basicaly reads your cron log and reconstitute the crontab file.

## Instructions

First things first, you will need to extract the logs from your now lost crontab. So, to take the last week log, execute:
```
zgrep -i cron /var/log/syslog*
```
Now save it in a txt file called "crontab_log". Or choose another name, but have in mind that you will need to change it in the code. Make sure as well, that the code and the 'crontab_log.txt' are in the same folder.
After save it, you can either run crontab_recovery from you terminal or open and run it somewhere, I used Jupyter. In any case, you will have to change the user's name which you want to recover the crontab. Please, change it at line 2:
```
# Set which user's crontab do you want to restore
usr = "ubuntu"
```
Thats it! Your crontab recovery file should be at the same folder, under the name of "recovered_crontab.txt".

The code was writen in a rush, in a couple minutes, so I'll be glad to receive your optimizations!