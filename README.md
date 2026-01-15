# Embedded OCR-to-Speech System for Visually Impaired Users

## About
This repository contains the code for a wearable device that helps visually impaired users to read text in natural scene conditions. There is also a version of the script that can be run on Windows/POSIX-compliant machines to test functionality. Both versions are capable of taking a picture, performing optical character recognition on it, and producing a text-to-speech output for the user.

This script uses [RapidOCR](https://github.com/RapidAI/RapidOCR) for text detection/recognition and [Piper](https://github.com/rhasspy/piper) for text-to-speech functionality (thank you Danny!).

This project is still in progress, so check back every once in a while for updates!

Expected completion: April 2026

## Setup for POSIX/Windows

*Ensure that you have Python version 3.10.0 or later installed on your system.*

```
python --version
```

**NOTE:** *Since this project uses the pynput package for monitoring keyboard events, this script will not work on Linux DEs using the Wayland Protocol and requires sudo permissions to work on MacOS.*

Run the following commands in a terminal.

#### Download/Clone the repository in any directory you'd like.

```
git clone https://github.com/seaflop/capstone/tree/testing
```

#### Navigate to the `capstone` directory.

```
cd capstone
```

#### Activate a Python virtual environment.

POSIX:

```
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```
python -m venv .venv
.venv\Scripts\Activate
```

#### Download the required packages.

```
pip insatll --upgrade pip
pip install -r requirements.txt
```

#### Run the Script

Run the script from the `capstone` directory, and provide the path to the image you'd like to test on.
If you wish to specify a specific image you would like to test on, use the `-i` flag.
If you would like to open the webcam to take a picture to test on, use the `-w` flag.

POSIX:

```
python ./src/main.py -i "pathtoyourimagehere.jpg"
```

or

```
python ./src/main.py -w
```

Windows:

```
python .\src\main.py -i "pathtoyourimagehere.jpg"
```

or

```
python .\src\main.py -w
```

The script will prompt you for input when it is ready to run. This may take some time, especially on the first run, as all the models will have to be downloaded first.

Press Space to start the script.

If you specified `-w`, press Space to take a picture, or Esc to exit.

You can exit the script at any time by pressing the Esc key.

Audio playback can be paused/resumed by pressing the spacebar.