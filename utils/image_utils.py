from PIL import Image


def reduce_image_resolution(image_path, resolution_threshold=300):
    """
    :param image_path: absolute path to the image
    :param resolution_threshold: max size of any image side; default=300px
    """
    img = Image.open(image_path)

    if img.height > resolution_threshold or img.width > resolution_threshold:
        output_size = (resolution_threshold, resolution_threshold)
        img.thumbnail(output_size)
        img.save(image_path)
