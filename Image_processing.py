import numpy as np
import matplotlib.pyplot as plt
import os
import sys
from tqdm import tqdm

DATA_DIR = './DATASET_MNIST/'
TEST_IMAGES_FILENAMES = DATA_DIR+'t10k-images.idx3-ubyte'
TEST_LABELS_FILENAMES = DATA_DIR+'t10k-labels.idx1-ubyte'
TRAIN_IMAGES_FILENAMES = DATA_DIR+'train-images.idx3-ubyte'
TRAIN_IMAGES_FILENAMES = DATA_DIR+'train-labels.idx1-ubyte'

def bytes_to_int(bytes_data):
    return int.from_bytes(bytes_data , 'big')

def read_images(file_name):
    images = []
    print('fghj')
    with open(file_name , 'rb') as fp:
        magic_number = bytes_to_int(fp.read(4))
        no_images = bytes_to_int(fp.read(4))
        no_rows = bytes_to_int(fp.read(4))
        no_columns = bytes_to_int(fp.read(4))
        print(no_images)
        print(no_rows)
        print(no_columns)
        for images_index in tqdm(range(no_images)):
            image = []
            for row_index in range(no_rows):
                row = []
                for col_index in range(no_columns):
                    pixels = fp.read(1)
                    row.append(pixels)
                image.append(row)
            images.append(image)
    return images




def main():
    Train_images = read_images(TEST_IMAGES_FILENAMES)
    print(len(Train_images))
    print(Train_images)



if __name__ == '__main__':
    main()