#!/usr/bin/env python
from __future__ import print_function
import csv
import sys
import time
import argparse
from selenium import  webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import settings

class FpsCapturer:
    def __init__(self, args):
        self.webdriver_pathname = settings.WEBDRIVER_PATH
        self.webgl_sample_url = settings.WEBGL_SAMPLE_URL
        self.duration = None
        self.number = None
        if args.time:
            self.duration = args.time * 3600
        elif args.min:
            self.duration = args.min * 60
        else:
            self.number = args.number

        self.data_file = args.file
        self.draw_chart = args.withchart
        self.data = []

        self.d = DesiredCapabilities.CHROME
        self.d['loggingPrefs'] = {'browser': 'ALL'}
        self.webdriver = webdriver.Chrome(executable_path=self.webdriver_pathname, desired_capabilities=self.d)
        self.webdriver.get(self.webgl_sample_url)
        time.sleep(settings.SAMPLE_INITIALIZATION_TIME)

    def start(self):
        start_time = time.time()
        start_count = 0
        while True:
            this_time = time.time()
            localtime = time.localtime(this_time)
            if this_time - start_time >= self.duration:
                break
            if self.number and start_count >= self.number:
                break
            fps = self.webdriver.find_element_by_id('fps').get_attribute('innerText')
            time_value = '%02d:%02d:%02d' % (localtime.tm_hour, localtime.tm_min, localtime.tm_sec)
            fps_value = str(fps)
            record = (time_value, fps_value)
            self.data.append(record)
            print('fps:'.join(['[' + record[0] + ']', record[1]]))
            time.sleep(1)
            if self.number:
                start_count += 1

        self.webdriver.quit()

        with open(self.data_file, 'wb') as fp:
            csv_writer = csv.writer(fp)
            csv_writer.writerow(['Time', 'Fps'])
            for record in self.data:
                csv_writer.writerow(record)


def main():
    parser = argparse.ArgumentParser(description='A utility to get the fps data of webgl samples')
    parser.add_argument('-t', '--time', type=int,
                        help='specify the duration you want go get the fps, in hour.')
    parser.add_argument('-m', '--min', type=int, default = 5,
                        help = 'specify the duration in minute, useful when --time is less than 1 hour and not set,'
                               ' default value is 5 minutes.')
    parser.add_argument('-f', '--file', type=str, default='fps.csv',
                        help='specify the fps data file to store in csv format, default value is fps.csv.')
    parser.add_argument('-n', '--number', help='specify the number of capturing the fps data.')
    parser.add_argument('-c', '--withchart', action='store_true',
                        help='specify whether generate the fps data chart.')
    args = parser.parse_args()
    print(args)
    fps_capturer = FpsCapturer(args)
    fps_capturer.start()


if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.err.write('Testing interrupted!')
        sys.exit(1)
