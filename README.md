# Introduction
This repository contains some useful scripts to monitor fps changes for WebGL samples.

## Environments:
* Windows 7 and above
* Google Chrome
* Python 2.7

## Scripts
* `settings.py`: contains necessary configurations about webdriver and sample URL.
* `fps.py`: This script will accepts time parameter and monitor the fps changes and then store the data generated in this duration. Optionally, a chart for the data will be generated.

## Pre-conditions:
* Config the webdriver.
  Download Google Chrome driver from [here](https://sites.google.com/a/chromium.org/chromedriver/) for your platform. Unzip it and keep the directory as:
  `<your/chrome/driver/workspace>/<version>/chromedriver.exe`. Then update `settings.py` if necessary.
* Install `selenium` package, you might need administrater permission to install it.
  ```
  pip install selenium 
  ```

## Usage:
```
python fps.py -h
usage: fps.py [-h] [-t TIME] [-m MIN] [-f FILE] [-n NUMBER] [-c]

A utility to get the fps data of webgl samples

optional arguments:
  -h, --help            show this help message and exit
  -t TIME, --time TIME  specify the duration you want go get the fps, in hour.
  -m MIN, --min MIN     specify the duration in minute, useful when --time is
                        less than 1 hour and not set, default value is 5
                        minutes.
  -f FILE, --file FILE  specify the fps data file to store in csv format,
                        default value is fps.csv.
  -n NUMBER, --number NUMBER
                        specify the number of capturing the fps data.
  -c, --withchart       specify whether generate the fps data chart.
```

Here is an example:
```
python fps.py -t 1 -f fps_1hour.csv
```

It means the utility will monitor the WebGL sample for 1 hour and store the fps data to file **fps_1hour.csv**.

## Todo
Generate the data chart automatically on Windows.
