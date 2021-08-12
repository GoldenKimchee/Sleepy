from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

def main():
    ask_reset()

def ask_reset():
    valid_responses = ["y", "n"]
    while True:
        response = input("(Recommended) Would you like to reset the volume? (y/n)").lower()
        if response not in valid_responses:
            print("Please answer 'y' or 'n'.")
        reset_volume()
        print("Volume was reset.")
        break

def reset_volume():
    sessions = AudioUtilities.GetAllSessions() # Get all sessions currently playing audio

    for session in sessions:
        if session.Process and session.Process.name() == 'chrome.exe':  # If session is running
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            volume.SetMasterVolume(1, None)

if __name__ == "__main__":
    main()