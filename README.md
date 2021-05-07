# findVaccine

Find open slots in India to get vaccinated against CoVID-19 

* This is a barebones `python` script to find an open slot to get vaccinated
* Currently configured to generate audio (beep) alert if an open slot is available for ages 18+
* Currently works for Thane and Mumbai only

Usage: 
```
$ python3 main.py
```
## Setting up `beepy` and `espeak-ng`
There are a few dependencies that didn't get installed automatically. To manually install dependencies, run:
```
$ sudo apt-get install -y python3-dev libasound2-dev
```
Then
```
$ pip3 install beepy
```
For `espeak-ng` checkout [this](https://github.com/espeak-ng/espeak-ng/blob/master/docs/guide.md) and [this](https://github.com/gooofy/py-espeak-ng)

