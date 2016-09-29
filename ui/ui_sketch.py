import numpy as np
import cv2

class UISketch:
    def __init__(self, npx, scale, accu=True):
        self.npx = npx
        self.scale = scale
        self.nc = 3
        self.img = np.zeros((npx, npx, self.nc), np.uint8)
        self.mask = np.zeros((npx, npx, 1), np.uint8)
        self.width = 1

    def update(self, points, color):
        num_pnts = len(points)
        c = 255
        for i in range(0, num_pnts - 1):
            pnt1 = (int(points[i].x()/self.scale), int(points[i].y()/self.scale))
            pnt2 = (int(points[i + 1].x()/self.scale), int(points[i + 1].y()/self.scale))
            cv2.line(self.img, pnt1, pnt2, (c,c,c), self.width)
            cv2.line(self.mask, pnt1, pnt2, 255, self.width)



    def update_width(self, d, color):
        self.width = min(20, max(1, self.width+ d))
        return self.width

    def get_constraints(self):
        return self.img, self.mask


    def reset(self):
        self.img = np.zeros((self.npx, self.npx, self.nc), np.uint8)
        self.mask = np.zeros((self.npx, self.npx, 1), np.uint8)


