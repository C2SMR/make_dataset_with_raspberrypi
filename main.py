import cv2
import os
import time


class Dataset:
    def __init__(self, time_sleep: int = 0.5):
        self.time_sleep: int = time_sleep
        self.path: str = 'dataset/'
        self.extension: str = '.png'
        self.video: cv2.VideoCapture = cv2.VideoCapture(0)

    def get_number_picture(self) -> int:
        return len(os.listdir(self.path))

    def take_picture(self):
        cv2.imwrite(f'{self.path}'
                    f'{self.get_number_picture()}'
                    f'{self.extension}',
                    self.video.read()[1])

    def run(self):
        while True:
            time.sleep(self.time_sleep)
            self.take_picture()


if __name__ == '__main__':
    Dataset(10).run()
