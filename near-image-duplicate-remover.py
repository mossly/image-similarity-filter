import os
import cv2
import numpy as np

# Define the directory containing the images
directory = input("Enter directory path: ")

# Define the threshold for image similarity
similarity_threshold = input("Enter similarity threshold: ")


# Create an empty list to hold the filenames of the images we want to keep
kept_filenames = []

# Loop over all files in the directory
for filename1 in os.listdir(directory):
    if not filename1.endswith(".png"):
        continue
    filepath1 = os.path.join(directory, filename1)
    img1 = cv2.imread(filepath1)
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    # Flag to keep track of whether we should keep the current image
    keep_image = True

    # Loop over all images that we have already decided to keep
    for kept_filename in kept_filenames:
        filepath2 = os.path.join(directory, kept_filename)
        img2 = cv2.imread(filepath2)
        gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

        # Compute the absolute difference between the two grayscale images
        diff = cv2.absdiff(gray1, gray2)

        # Threshold the difference image to identify the pixels that differ the most
        threshold = 20
        diff[diff < threshold] = 0
        diff[diff >= threshold] = 255

        # Compute the percentage of non-zero pixels in the difference image
        num_pixels = diff.shape[0] * diff.shape[1]
        num_diff_pixels = np.count_nonzero(diff)
        similarity = 1 - (num_diff_pixels / num_pixels)

        # If the images are very similar, don't keep the current image
        if similarity > similarity_threshold:
            keep_image = False
            print(f"Deleting {kept_filename} as it differs by {num_diff_pixels} from {filename1}")
            break
        else:
            print(f"Preserving {kept_filename} as it differs by {num_diff_pixels} from {filename1}")

    # If we should keep the current image, add its filename to the list of kept filenames
    if keep_image:
        kept_filenames.append(filename1)

# Remove all images that we didn't keep
for filename in os.listdir(directory):
    if filename.endswith(".png") and filename not in kept_filenames:
        filepath = os.path.join(directory, filename)
        os.remove(filepath)