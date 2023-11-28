import picamera
import os
import time


class Dataset:
    def __init__(self, time_sleep: int = 0.5):
        self.time_sleep: int = time_sleep
        self.path: str = 'dataset/'
        self.extension: str = '.png'
        self.camera = picamera.PiCamera()
        time.sleep(2)

    def get_number_picture(self) -> int:
        return len(os.listdir(self.path))

    def take_picture(self):
        self.camera.capture(self.path +
                            str(self.get_number_picture()) +
                            self.extension)

    def run(self):
        while True:
            time.sleep(self.time_sleep)
            self.take_picture()


if __name__ == '__main__':
    Dataset(10).run()
