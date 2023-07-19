#!/usr/bin/python3

import jetson.inference
import jetson.utils
import argparse
import time

# Function to get user input within a specified timeout
def get_user_guess(timeout, possible_classifications):
    start_time = time.time()
    while time.time() - start_time < timeout:
        user_guess = input("Guess what the computer classified the image as: ")
        if user_guess.lower() in possible_classifications:
            print("Congratulations! You guessed correctly.")
            return True
    print("Time's up! The correct answers were:", ', '.join(possible_classifications))
    return False

# parse the command line
parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str, help="filename of the image to process")
parser.add_argument("--network", type=str, default="googlenet", help="model to use, can be:  googlenet, resnet-18, etc.")
args = parser.parse_args()

# load an image (into shared CPU/GPU memory)
img = jetson.utils.loadImage(args.filename)

# load the recognition network
net = jetson.inference.imageNet(args.network)

# classify the image
class_idx, confidence = net.Classify(img)

# find the object descriptions
possible_classifications = net.GetClassDesc(class_idx).split(',')

# print the result
# print("image is recognized as:", ', '.join(possible_classifications), "(class #{:d}) with {:f}% confidence".format(class_idx, confidence * 100))

# Let the user guess
if get_user_guess(15, [c.strip().lower() for c in possible_classifications]):
    print("You win!")
else:
    print("You lose!")
