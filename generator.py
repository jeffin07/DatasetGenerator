import imageio 
import imgaug as ia
from imgaug import augmenters as iaa
import argparse
import matplotlib.pyplot as plt
import os
# :/ But Why ?
ia.seed(4)


parser = argparse.ArgumentParser()

parser.add_argument('--image_path', help='path of the image')
parser.add_argument('--save_path', help='path of the augmented images to be saved')
parser.add_argument('--ext', help='extension of images to be saved')


def load_image(image):
	img = imageio.imread(image)
	return img
# 0.1 1
def augment(img,save_dir):
	for i in range(1):
		rotate = iaa.Affine(rotate=(0, 0.1))
		image_aug0 = rotate.augment_image(img)
		mul = iaa.Multiply((0.8, 1))
		image_aug = mul.augment_image(image_aug0)
		# :/ need improvement
		plt.imsave(os.path.join(save_dir,args.image_path.split("/")[-1].split(".")[0]+str(i)+str(args.ext)),image_aug)
	


args = parser.parse_args()
if args.image_path == None:
	exit()


if __name__ == "__main__":
	augment(load_image(args.image_path),args.save_path)