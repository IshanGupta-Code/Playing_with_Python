import os 
import pygame

def play_music(folder, song_name):

    file_path = os.path.join(folder, song_name)

    if not os.path.exists(file_path):
        print("File Not Found!")
        return
    
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    print(f"\nNow playing: {song_name}")
    print("Command: [P]ause, [R]esume, [S]top")

    while True:

        command = input("> ").upper()

        if command == "P":
            pygame.mixer.music.pause()
            print("Paused")
        elif command == "R":
            pygame.mixer.music.unpause()
            print('Resumed')
        elif command == "S":
            pygame.mixer.music.stop()
            print("Stopped")
            return
        else:
            print("Print Invalid Command")
        

def main():
    try:
        pygame.mixer.init()
    except pygame.error as e:
        print("Audio Initilization Failed! ", e)
        return
    
    # Resolve the music folder relative to this script's directory so the
    # program works independent of the current working directory.
    base_dir = os.path.dirname(os.path.abspath(__file__))
    folder = os.path.join(base_dir, "Music")

    if not os.path.isdir(folder):
        print(f"Folder not found at: {folder}")

        # Offer to create the folder so users running from the repo root
        # (or elsewhere) can quickly set up the expected structure.
        answer = input("Would you like to create the folder now? (Y/N): ").strip().upper()
        if answer == "Y":
            try:
                os.makedirs(folder, exist_ok=True)
                print(f"Created folder: {folder}\nAdd your .mp3 files into this directory and re-run the player.")
            except OSError as e:
                print("Failed to create folder:", e)
            return
        else:
            print("Please create the folder and add .mp3 files, or run the script from the directory containing your Music folder.")
            return
    
    mp3_files = [file for file in os.listdir(folder) if file.endswith(".mp3")]

    if not mp3_files:
        print("No .mp3 File Found!")
        return

    while True:
        print("***** MP3 PLAYER *****")
        print("My song list:")

        for index, song in enumerate(mp3_files, start=1):
            print(f"{index}. {song}")

        choice_input = input("\nEnter the song # to play (or 'Q' to quit): ")

        if choice_input.upper() == "Q":
            print("Bye!")
            break

        if not choice_input.isdigit():
            print("Enter a valid number")
            continue

        choice = int(choice_input) - 1

        if 0 <= choice < len(mp3_files):
            play_music(folder, mp3_files[choice])
        else:
            print("Invalid Choice")

        

if __name__ == "__main__":
    main()