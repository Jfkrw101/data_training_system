import os
import sys
import subprocess
import time
import argparse
from ultralytics import YOLO


name_of_computer = os.environ.get('USERNAME')
path_dir = f"/home/{name_of_computer}/setup_train" 
dataset_dir = f"{path_dir}/dataset"
images_dir = f"{path_dir}/images"
mask_dir = f"{path_dir}/masks"




def train_darknet(gpus,name_data,cfg,pretrained):
    package_path = os.path.expanduser(path_dir)

    print("Start Data generation and Split text.txt,train.txt ...\n")
    # convertmask image to binary masks
    masks_gen__path = os.path.join(package_path, "masks_gen.py")
    start_time = time.time()
    subprocess.run(["python3", masks_gen__path])
    end_time = time.time()
    elaps_time = end_time - start_time
    hours = int(elaps_time // 3600)
    minutes = int((elaps_time % 3600) // 60)
    seconds = int(elaps_time % 60)
    print(f"Maskgen execution time: {hours} hrs {minutes} mins {seconds} secs")
    


    # data gen
    data_gen_script_path = os.path.join(package_path,"datagen.py")
    start_time = time.time()
    subprocess.run(["python3",data_gen_script_path])
    end_time = time.time()
    elaps_time = end_time - start_time
    hours = int(elaps_time // 3600)
    minutes = int((elaps_time % 3600) // 60)
    seconds = int(elaps_time % 60)
    print(f"Datagen execution time: {hours} hrs {minutes} mins {seconds} secs")
    
    # process split train and test
    process_script_path = os.path.join(package_path, "split_process.py")
    start_time = time.time()
    subprocess.run(["python3", process_script_path])
    end_time = time.time()
    elaps_time = end_time - start_time
    hours = int(elaps_time // 3600)
    minutes = int((elaps_time % 3600) // 60)
    seconds = int(elaps_time % 60)
    print(f"Split execution time: {hours} hrs {minutes} mins {seconds} secs")
    

    print("Data generation and Split test.txt,train.txt complete ...\n")

    print("Start Training with Darknet")
    darknet_path = f"/home/{name_of_computer}/darknet"

    os.chdir(darknet_path)


    start_time = time.time()
    cmd = f"./darknet detector train data/{name_data}.data {path_dir}/cfg/{cfg}.cfg {pretrained} {gpus} -dont_show -map"
    os.system(cmd)
    end_time = time.time()
    elaps_time = end_time - start_time
    hours = int(elaps_time // 3600)
    minutes = int((elaps_time % 3600) // 60)
    seconds = int(elaps_time % 60)
    print(f"Execution time: {hours} hrs {minutes} mins {seconds} secs")
    print("Training completed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train Darknet")
    parser.add_argument("-gpus", default="0", help="Choose number of gpu devices to use (e.g., '-gpus 0,1')")
    parser.add_argument("-name_data", required=True, help="Name of data darknet directory (e.g, '-name_data humans')")
    parser.add_argument("-cfg ",required=True,help="Choose your cfg want to train (e.g., 'yolov4-tiny-humans')")
    parser.add_argument("-pretrained",required=True,help="Choose your pretrained model you want for trainning (e.g., 'yolov4-tiny.conv87)")

    args = parser.parse_args()

    try:
        train_darknet(args.gpus,args.name_data,args.cfg,args.pretrained)
    except Exception as e:
        print("Error occurred during training:", str(e))
        sys.exit(1)
