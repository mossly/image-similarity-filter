# Image Similarity Filter

This Python script helps to identify and delete similar images in a given directory based on a user-defined similarity threshold. It uses OpenCV to compare images and calculate the similarity percentage. If two images have a similarity percentage greater than the given threshold, one of the images will be deleted.

## Requirements

- Python 3.x
- OpenCV (Install using `pip install opencv-python`)

## Usage

1. Clone this repository or download the script `image_similarity_filter.py`.
2. Place the script in the directory containing the images you want to filter.
3. Open a terminal/command prompt and navigate to the directory containing the script.
4. Run the script using the following command:

```
python image_similarity_filter.py
```

5. Enter the directory path and the similarity threshold when prompted:

```
Enter directory path: /path/to/your/images
Enter similarity threshold: 0.90
```

6. The script will compare each image pair in the directory and delete the images that have a similarity percentage greater than the given threshold.

## Notes

- The script currently supports only `.png` images. You can modify the script to support other image formats by changing the file extension check in the script.
- The similarity threshold should be a float between 0 and 1, where 1 means 100% similarity. A higher threshold will result in fewer images being deleted.
- The script calculates the similarity percentage by counting the number of pixels that differ between the two images. It uses grayscale versions of the images for comparison, which might not always result in the most accurate similarity measurement. You can modify the script to use other methods for comparing images if needed.

## License

This project is licensed under the MIT License
