import sys

from spotify import Song

if __name__ == '__main__':
    #Main program settings
    input_file = '/home/joserequenaidv/Escritorio/Programación/proyecto-spotify/files/top50.csv'
    output_file = '/home/joserequenaidv/Escritorio/Programación/proyecto-spotify/files/top50_mod.csv'
    relative_bpm = int(sys.argv[1])  # read keyboard input

    #Some basic UX
    while relative_bpm == 0:
         user_input = input("Typing zero? Are you kidding? \nTry again: ")
         relative_bpm = int(user_input)
    if relative_bpm > 0:
        print("Good choice, human! Shake that butt, homie!")
    elif relative_bpm < 0:
        print("Great, buddy. It's time to chill.")

    #Creating our object:
    our_object = Song.load_songs(input_file)

    #Applying changes:
    for changing_object in our_object:
        changing_object.change_speed(relative_bpm)

    #Saving and printing the changes:
    saving_object = Song.save_songs(our_object, output_file)
