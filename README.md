# Embedded OCR-to-Speech System for Visually Impaired Users

## About

## Setup

### Setup for Raspberry Pi

This project uses a Raspberry Pi CM4 as the main board.

The camera used is the Raspberry Pi Camera Module 3.

The button for input detection is connected to GPIO pin 14.

### Setup for Linux

*Ensure that you have Python version 3.10 or later installed on your system.*

**NOTE:** *Since this project uses the pynput package for monitoring keyboard events, this script will not work on Linux DEs using the Wayland Protocol*

1. Download/Clone the repository.

```
$ git clone github.com/seaflop/capstone
```

2. Navigate to the `capstone` directory.

3. Activate a Python virtual environment.

Linux:

```
$ python3 -m venv .venv
$ source .venv/bin/activate
```

4. Download the required packages.

```
$ pip install -r requirements.txt
```

5. Run the script from the `capstone` directory.

```
$ python ./src/main.py -i "path/to/your/image/here.jpg"
```

## To-do
