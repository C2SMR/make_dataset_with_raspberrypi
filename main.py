import subprocess
import os
import time
import sys
import requests


class Dataset:
    def __init__(self, time_sleep: int = 0.5):
        self.time_sleep: int = time_sleep
        self.path: str = 'dataset/'
        self.extension: str = '.png'
        self.api_path: str = ('https://api.c2smr.fr/machine/'
                              'add_picture_alert_or_moment')
        self.api_key: str = sys.argv[1]
        self.city: str = sys.argv[2]
        self.name_extension_count: int = self.get_number_picture()

        self.run()

    def get_number_picture(self) -> int:
        return len(os.listdir(self.path))

    def take_picture(self):
        subprocess.call(['sudo', 'libcamera-jpeg', '-o',
                         f'{self.city}-dataset-{self.name_extension_count}'
                         f'{self.extension}'])

    def send_picture(self):
        try:
            requests.post(self.api_path, json={
                "key": self.api_key,
            }, files={
                'file': open(f'{self.city}-dataset-'
                             f'{self.name_extension_count}.'
                             f'{self.extension}', 'rb')
            })
        except Exception:
            pass

    def run(self):
        while True:
            time.sleep(self.time_sleep)
            self.take_picture()
            self.send_picture()
            self.name_extension_count += 1


if __name__ == '__main__':
    Dataset(10)
