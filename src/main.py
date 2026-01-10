import file_locations as fl
from capstone import Capstone

from pynput import keyboard
import time
import argparse
import sys
import os

"""
    This function checks for key presses.
    It is used as part of the keyboard.Listener() for the on_press parameter.
    Returns False to stop the listener.
"""
def on_press(key):
    global c, stop_flag, started
    try: 
        if (key == keyboard.Key.space):
            if (not started):
                started = True
            if (c.is_paused and not c.is_stopped):
                c.resume(resume_sound_file_location=fl.resume_sound_path)
            elif (not c.is_paused and not c.is_stopped):
                c.pause(pause_sound_file_location=fl.pause_sound_path)
        elif (key == keyboard.Key.esc):
            stop_flag = True
            started = False
            if (not c.is_stopped):
                c.stop()
            #return False # Stops the keyboard listener
    except AttributeError:
        pass

def main():
    global c, stop_flag

    if (stop_flag):
        return
    c.play(fl.ready_sound_path)

    print("Press SPACE to start the script.")
    print("While the script is running press SPACE to pause/resume and ESC to exit.")
    print("(Note that it may take some time to terminate the program as it finishes whatever operation is was currently doing)")
    print("Waiting for input...")

    global started
    started = False
    while (not started):
        if (stop_flag):
            return
        time.sleep(0.1)
    
    if (stop_flag):
        return
    c.create_path(os.path.basename(os.path.dirname(fl.ocr_path)), 
                  os.path.basename(os.path.dirname(fl.tts_path)))
    
    if (stop_flag):
        return
    c.resize_image(fl.image_path)

    if (stop_flag):
        return
    c.ocr(fl.image_path, fl.ocr_path)
    
    if (stop_flag):
        return
    with open(fl.ocr_path, "r") as f:
        text = f.read()

    if (stop_flag):
        return
    c.make_TTS_file(text, fl.tts_path)

    if (stop_flag):
        return
    with open(fl.ocr_path, "r") as f:
        print(f.read())

    if (stop_flag):
        return
    c.play(fl.tts_path)

    started = False

if __name__ == "__main__":

    # Assert Python version >= 3.10
    MIN_VERSION = (3, 10)
    if sys.version_info < MIN_VERSION:
        raise EnvironmentError(f"This script requires Python version {MIN_VERSION[0]}.{MIN_VERSION[1]} or higher.\nYou are using Python version {sys.version_info.major}.{sys.version_info.minor}")

    # Ensure the proper starting directory (i.e. not from src/ and instead from the project root directory)
    if (sys.argv[0] != fl.main_script_path):
        raise RuntimeError(f"Script must be run from {fl.main_script_path}. Got {sys.argv[0]}")
        
    # Define CLI arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image", help="relative path of image file location",
                        default= fl.image_path)
    args = parser.parse_args()

    fl.image_path = args.image

    program_running = True
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    stop_flag = False

    c = Capstone(path_to_voice=fl.voice_path)

    main()

    listener.stop()