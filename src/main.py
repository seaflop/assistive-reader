import file_management as fm
import tts
import ocr

from pynput import keyboard
import time
#from gpiozero import Button


def take_picture():
    return


def on_press(key):
    global running

    try: 
        print(f"attribute error {key}")
        if(key == keyboard.Key.space):
            running = True
            print(f"{key} was pressed")
    except AttributeError:
        print(f"attribute error {key}")
        if(key == keyboard.Key.space):
            running = True
            print(f"{key} was pressed")

def main():
    global running

    fm.init_folders()
    ocr.resize_image(fm.image_path)
    ocr.ocr(fm.image_path)

    with open(fm.ocr_path, "r") as f:
        file_contents = f.read()
    tts.TTS_to_file(file_contents)
    tts.play_audio(fm.tts_path)

def volume_adjust():
    return

def start():
    print("")
    return

def look_in():
    while(True):
        print("Hey, just checking in. Is everything okay?")
        time.sleep(5)

if __name__ == "__main__":
    running = False

    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    print("press space to start script")

    while (True):
        if (running):
            main()
            break
        else:
            time.sleep(0.1)

    listener.stop()
