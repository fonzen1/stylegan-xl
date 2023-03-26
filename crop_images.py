from PIL import Image
import os

# set the path for the source folder
src_folder = "../suadd-2023-semantic-segmentation/public_dataset/semantic_annotations"

# set the path for the destination folder
dst_folder = "../cropped_dataset/semantic_annotations"

# define the new size to crop to (width, height)
new_size = (1024, 1024)

# loop through all the files in the source folder
for filename in os.listdir(src_folder):
    # open the image file
    with Image.open(os.path.join(src_folder, filename)) as im:
        # calculate the center coordinates of the image
        width, height = im.size
        left = (width - new_size[0])/2
        top = (height - new_size[1])/2
        right = (width + new_size[0])/2
        bottom = (height + new_size[1])/2
        # crop the image to the center coordinates
        cropped_im = im.crop((left, top, right, bottom))
        # set the new filename for the cropped image
        new_filename = "cropped_" + filename
        # save the cropped image to the destination folder
        cropped_im.save(os.path.join(dst_folder, new_filename))
