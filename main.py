import cv_funcs as f

if __name__ == '__main__':
    image = f.loadGrey('test.JPG')
    f.getDoG(image)

