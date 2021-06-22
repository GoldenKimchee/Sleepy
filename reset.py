from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

def reset_volume():
    volume_value = 0.5
    sessions = AudioUtilities.GetAllSessions() # Get all sessions currently playing audio

    for session in sessions:
        if session.Process and session.Process.name() == 'chrome.exe':  # If session is running
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            volume.SetMasterVolume(volume_value, None)
