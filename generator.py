import imageio 
import imgaug as ia
from imgaug import augmenters as iaa
ia.seed(4)

def load_image(image):
	img = imageio.imread(image)
	return img
# 0.1 1
def augment(img,path):
	for i in range(70):
		rotate = iaa.Affine(rotate=(0, 0.1))
		image_aug0 = rotate.augment_image(img)
		mul = iaa.Multiply((0.8, 1))
		image_aug = mul.augment_image(image_aug0)
		print(img.shape)
		print(image_aug.shape)
		plt.imsave('/home/jeffin/Documents/test_aug/{}__{}.jpg'.format(path.split("/")[-1].split(".")[0],str(i)),image_aug)



