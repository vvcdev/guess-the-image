## Think like a computer | Computer Image Classification Game using Jetson Inference

## Goal
You have 15 seconds to guess what the computer thinks an image is. The computer is not trained extremely well, so an image of a snake could be identified as a hook, a claw, etc. For more accurate computer guesses, use less detailed but more realistic images.

## How to Play
1. Make sure you have a Jetson Nano with the Jetson Inference library and Python3 installed on your system.
2. Upload the image you want the computer to identify into the "images" folder.
3. Open your terminal and type the following command: `python3 game.py image/filename`
4. Guess the image's identity within the given time!

More details: [Youtube demo]

## How It Works

### Behind the Scenes
The game utilizes the image database in the Jetson Inference library. You can see the code handling this process in `my-recognition.py`.

## Game: 
1. Imports all necessary components of my-recognition.py (which contains the necessary material from the Jetson Inference library)
2. It defines a function called get_user_guess(timeout, possible_classifications) that takes two parameters - the time limit and the possible names of the image in the computer's database
3. The script then parses the command-line arguments using argparse. It expects the user to provide the filename of the image to be processed and an optional argument for the network model to use for classification (default is "googlenet").
4. The script loads the specified image file into shared CPU/GPU memory using jetson.utils.loadImage().
5. It loads the recognition network using jetson.inference.imageNet with the specified or default model.
6. The script retrieves the descriptions of the recognized object from the network.
7. The script then asks the user to guess the classification of the image. The user has 15 seconds to provide their guess.
8. If the user's guess is correct and matches one of the possible classifications, the script prints "Congratulations! You guessed correctly."
9. If the user's guess is incorrect or they fail to guess within the time limit, the script prints "Time's up! The correct answers were:" and displays the list of possible classifications.
10. Finally, the script prints either "You win!" or "You lose!" depending on the user's guess and the result of the game.

