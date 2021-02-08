from unittest import TestCase
import unittest
from accuracy.verify_box import accuracy_boxes
from utils import show_result, draw_box 
import cv2
import os
class simple_test(TestCase):
    def test_first(self):
        boxes = [[382, 167, 459, 229, 'car', 'job_3'],
                [169, 160, 400, 271, 'car', 'job_1'],
                [160, 161, 383, 272, 'car', 'job_2'],
                [160, 160, 390, 270, 'car', 'job_4']]
        img = cv2.imread('images/1.jpg')
        image = []
        for box in boxes:
            image.append(draw_box(img, box[:4], box[4]+'/'+box[5]))
        all_img = show_result(image)
        cv2.imshow('before',all_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        acc = accuracy_boxes(boxes)
        results = acc.verify_boxes()
        image = []
        for box in boxes:
            accuracy = results['accuracy_box'].get(box[5])
            if accuracy != None:
                image.append(draw_box(img,box[:4],box[5]+'_'+str(accuracy)+'%'))
            else:
                image.append(draw_box(img,box[:4],box[5]+'_0%'))
        all_img = show_result(image)
        cv2.imshow('after',all_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
if __name__ == '__main__':
    unittest.main(verbosity=2)
