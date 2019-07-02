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
parser.add_argument('--dir_path', help='path of the image')
parser.add_argument('--save_path', help='path of the augmented images to be saved')
parser.add_argument('--ext', help='extension of images to be saved')


def load_image(image):
	img = imageio.imread(image)
	return img
# 0.1 1
def augment(img,save_dir):
	for i in range(10):
		rotate = iaa.Affine(rotate=(0, 0.1))
		image_aug0 = rotate.augment_image(img)
		mul = iaa.Multiply((0.8, 1))
		image_aug = mul.augment_image(image_aug0)
		# :/ need improvement
		plt.imsave(os.path.join(save_dir,args.image_path.split("/")[-1].split(".")[0]+str(i)+str(args.ext)),image_aug)

def augment_dir():
	check_structure_and_call(args.dir_path)
	print("{} categories found".format(len(os.listdir(args.dir_path))))
	for cats in os.listdir(args.dir_path):
		if os.listdir(os.path.join(args.dir_path,cats)) == []:
			print("No images found in {} skipping :( ".format(cats))
		for f in os.listdir(os.path.join(args.dir_path,cats)):
			print(f)

def check_structure_and_call(dataset_path):
	for i in os.listdir(dataset_path):
		if not os.path.isdir(os.path.join(dataset_path,i)):
			print("Folder structure not satisfied")
			exit()
	for i in os.listdir(os.path.join(dataset_path)):
		for j in os.listdir(os.path.join(dataset_path,i)):
			if not os.path.isfile(os.path.join(dataset_path,i,j)):
				print("error inside catagory")
				exit()
	print("Passed Folder structure :) ")



args = parser.parse_args()
if args.image_path == None:
	if args.dir_path == None:
		print("Image path cannot be empty :( ")
		exit()

# sample usage python3 generator.py --dir_path=/path/to/dataset

if __name__ == "__main__":
	# augment(load_image(args.image_path),args.save_path)
	# check_structure_and_call(args.dir_path)
	augment_dir()