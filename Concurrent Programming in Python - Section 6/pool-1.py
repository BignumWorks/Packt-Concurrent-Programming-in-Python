import time
import os
import multiprocessing
from PIL import Image  # pip install pillow if not found
from glob import glob

__author__ = "Mithun"


def create_thumbnail(image_files):
    size = 128, 128

    for image_file in image_files:
        file_name, ext = os.path.splitext(image_file)
        image = Image.open(image_file)
        image.thumbnail(size)

        t_file = file_name + ".t.jpeg"
        image.save(t_file, "jpeg")

        print("Process {}: Thumbnail created for {} as {}".format(multiprocessing.current_process().name, image_file,
                                                                  t_file))


if __name__ == "__main__":
    processor_count = multiprocessing.cpu_count()
    print("Processor Count= {}".format(processor_count))

    image_files = glob(r"C:\happy-face\happy*.jpeg")
    images_per_process = (int)(len(image_files) / processor_count) + 1
    processes = []

    start = time.time()

    for i in range(processor_count):
        if (i + 1) * images_per_process > len(image_files):
            image_file_subset = image_files[i * images_per_process:]
        else:
            image_file_subset = image_files[i * images_per_process:(i + 1) * images_per_process]

        p = multiprocessing.Process(target=create_thumbnail, args=(image_file_subset,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end = time.time()

    print("Total time taken is for thumbnail generation is {} seconds".format(end - start))
