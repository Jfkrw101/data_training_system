import glob
import os
import random
import shutil

def split_dataset(input_path,output_path):
    current_dir = os.path.expanduser(input_path)
    output_dir = os.path.expanduser(output_path)

    percentage_train = 70

    train_file = os.path.join(current_dir, 'train.txt')
    test_file = os.path.join(current_dir, 'test.txt')

    image_paths = glob.glob(os.path.join(current_dir, "*.jpg"))

    random.shuffle(image_paths)
    train_dir = os.path.join(output_dir, 'train')
    test_dir = os.path.join(output_dir, 'test')

    # Calculate the split index
    split_index = int(len(image_paths) * (percentage_train / 100.0))

    # Split into train and test sets
    train_paths = image_paths[:split_index]
    test_paths = image_paths[split_index:]

    file_train = open(train_file, 'w')
    file_test = open(test_file, 'w')

    for path in train_paths:
        title, ext = os.path.splitext(os.path.basename(path))
        dest_path = os.path.join(train_dir, title + '.jpg')
        shutil.copy2(path, dest_path)

    for path in test_paths:
        title, ext = os.path.splitext(os.path.basename(path))
        dest_path = os.path.join(test_dir, title + '.jpg')
        shutil.copy2(path, dest_path)


    train_file = os.path.join(output_dir, 'train.txt')
    test_file = os.path.join(output_dir, 'test.txt')

    with open(train_file, 'w') as file_train:
        for path in train_paths:
            title, ext = os.path.splitext(os.path.basename(path))
            file_train.write(os.path.join(train_dir, title + '.jpg') + "\n")

    with open(test_file, 'w') as file_test:
        for path in test_paths:
            title, ext = os.path.splitext(os.path.basename(path))
            file_test.write(os.path.join(test_dir, title + '.jpg') + "\n")
    file_train.close()
    file_test.close()
