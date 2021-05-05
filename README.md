# findVaccine

Find open slots in India to get vaccinated against CoVID-19 

* This is a barebones `python` script to find an open slot to get vaccinated
* Currently configured to generate audio (beep) alert if an open slot is available for ages 18+
* Currently works for Thane and Mumbai only

Usage: 
```
$ python main.py
```

#[TODO]

* Check following references:
    * [Exception Handling: blog post](https://findwork.dev/blog/advanced-usage-python-requests-timeouts-retries-hooks/)
    * [Exception handling: documentation](https://docs.python-requests.org/en/latest/user/quickstart/#errors-and-exceptions)

# Setting up `beepy`
There are a few dependencies that didn't get installed automatically. To manually install dependencies, run:
'''
$ sudo apt-get install -y python3-dev libasound2-dev
'''
Then
'''
$ pip3 install beepy
'''
