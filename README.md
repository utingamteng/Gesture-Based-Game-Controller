## Gesture Based Game Controller

This project was made so that gaming without involving physical touch of keyboards. Leveraging YOLOv8n as the base model, the captured gestures were translated into keyboard inputs. This project was meant to offer a more realistic and immersive gameplay experience

## Gesture List

There are five possible gesture that the player can show and it will be translated into a fixed keyboard inputs as shown below :

Thumb       ->   Arrow Left
Pinky       ->   Arrow Right
High Five   ->   Arrow Up
Two         ->   Arrow Down
Flat        ->   Spacebar

## Working Application Folder

This folder consist of the whole working application along with the required libraries/frameworks. Sadly, due to docker containerization problems, you need to manually download the file also installing the required dependencies

## Modeling Folder

This folder consist of files used for training and evaluation of YOLOv8n along with the preproccessed dataset and the results of both training and evaluation process. Some folder has to be downloaded too due to GitHub upload memory limit. Usually lies in .txt files. It's highly adviced to download the zip and extract it into the same folder where the .txt file lives

## Limitations 

1. Gestures and given keys are limited meaning this project can only be applied to games that can be played only by arrow keys and a spacebar
2. Both docker and streamlit cloud don't accept pyautogui which works as a translator between gesture and keyboard inputs. Meaning that user has to download the files on Working APplication Folder manually in order to use it
