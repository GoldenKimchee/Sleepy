from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from reset import reset_volume
import time

def main():
    volume, play_time = music_settings()
    play_music(volume, play_time)

def ask_reset():
    valid_responses = ["y", "n"]
    while True:
        response = input("(Recommended) Would you like to reset the volume? (y/n)")
        if response not in valid_responses:
            print("Please answer 'y' or 'n'.")
        reset_volume()
        print("Volume was reset.")
        break

def play_music(volume_value, play_time):
    while volume_value > 0:
        sessions = AudioUtilities.GetAllSessions() # Get all sessions currently playing audio
        for session in sessions:
            if session.Process and session.Process.name() == 'chrome.exe':
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                print(volume.GetMasterVolume())
                volume.SetMasterVolume(volume_value, None)
        hours = int(play_time[0]) * 60 * 60
        minutes = int(play_time[1]) * 60
        total_time = hours + minutes
        section = volume_value * 10
        time.sleep(total_time / section)
        volume_value = volume_value - 0.1


def check_time(time):
    for i in time[0]:  # Check hours
        try:
            int(i)
        except TypeError:
            print("The hours must be in whole numbers.")
            return False
        except Exception:
            print("Something bad happened.")
            return False

    for i in time[1]:  # Check minutes
        try:
            int(i)
        except TypeError:
            print("The minutes must be in whole numbers.")
            return False
        except Exception:
            print("Something bad happened.")
            return False

    return [int(time[0]), int(time[1])]


def ask_volume():
    print("Volume can be set to a decimal / whole number from 0 - 1 (e.g. 0.5)")
    volume = float(input("Set volume to... "))
    return volume, True


def ask_play_time():
    print("Time can be set with a colon in-between, hours to minutes (e.g. 2:30)")
    play_time = input("Play for... ")
    return play_time, True

def music_settings():
    volume = -1
    ask_again_volume = False

    play_time = ""
    ask_again_play_time = False

    while not (volume >= 0 and volume <= 1):
        if ask_again_volume:
            print("Please enter a valid volume amount.")

        volume, ask_again_volume = ask_volume()

    while not (":" in play_time):
        if ask_again_play_time:
            print("Please enter a valid time limit.")

        play_time, ask_again_play_time = ask_play_time()

    play_time = play_time.split(":", 1)
    valid_time = check_time(play_time)

    if valid_time:
        return volume, play_time

if __name__ == "__main__":
    main()




