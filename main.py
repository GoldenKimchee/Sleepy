from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from reset import ask_reset
import time

def main():
    play_time = ask_play_time()
    increments = ask_increments()
    play_music(play_time, increments)
    ask_reset()

def play_music(play_time, increments):
    hours = int(play_time[0]) * 60 * 60
    minutes = int(play_time[1]) * 60
    total_time = hours + minutes
    sleep_time = total_time / increments
    volume_value = 1
    decrease = volume_value / increments

    while volume_value > 0:
        sessions = AudioUtilities.GetAllSessions() # Get all sessions currently playing audio
        for session in sessions:
            if session.Process and session.Process.name() == 'chrome.exe':
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                volume.SetMasterVolume(volume_value, None)
        time.sleep(sleep_time)
        volume_value = round(volume_value - decrease, 3)

def ask_increments():
    ask_again = True

    while ask_again:
        try:
            increments = int(input("In how many increments should the volume decrease? (Enter a whole number) "))
            ask_again = False
        except TypeError:
            print("Please enter a whole number.")
        except Exception:
            print("Something went wrong...")

    return increments


def ask_play_time():
    print("Time can be set with a colon in-between, hours to minutes (e.g. 2:30)")
    ask_again = True

    while ask_again:
        try:
            play_time = input("Play for... ")
            play_time = play_time.split(":", 1)
        except ValueError:
            print("Please enter a time with ':'.")

        try:
            int(play_time[0])
            int(play_time[1])
            ask_again = False
        except ValueError:
            print("Please enter valid numbers with ':'.")
        except Exception:
            print("Something bad happened...")

    return play_time

if __name__ == "__main__":
    main()




