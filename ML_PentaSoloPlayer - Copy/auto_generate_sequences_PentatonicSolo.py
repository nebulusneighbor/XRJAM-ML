import os
import time

'''
READ ME
Auto generates polyphonic sequences using polyphony rnn

GENERATE_COMMAND is the command fed to the command line with the given PRIMER_MIDI_FILE location to generate
polyphonic sequences; this command is run every few seconds.

See the in-code comments for a more thorough explanation.
'''

PRIMER_MIDI_FILE = r'C:\Users\ptgyo\OneDrive\Documents\XRJAM\ML\MIDIOutput.midi.mid'
BUNDLE_FILE = r"C:\Users\ptgyo\OneDrive\Documents\XRJAM\ML\ML_PentaSoloPlayer\pentatonicModel_rnn.mag"
OUTPUT_DIR = r"C:\Users\ptgyo\OneDrive\Documents\XRJAM\ML\ML_PentaSoloPlayer\generated_pentatonicSolo"

GENERATE_COMMAND = f'''
polyphony_rnn_generate \
--bundle_file={BUNDLE_FILE} \
--output_dir={OUTPUT_DIR} \
--num_outputs=2 \
--num_steps=256 \
--primer_midi={PRIMER_MIDI_FILE}  \
--condition_on_primer=false \
--inject_primer_during_generation=true
'''

def main():
    # Run any commands that need to be run first, like getting to the right directory.
        #os.system("cd Downloads/<whereever polyphony is located>")

    # While loop set to true - calls the function to run the command automatically until the program is stopped.
    while True:
        run_command(GENERATE_COMMAND)
        time.sleep(30) # Change this number to change how often the command is run to generate new polyphonic sequences.


def run_command(generate_command):
    # os.system feeds whatever string it is given to the command line, we give it the generate command here to run that command.
    command_result = os.system(generate_command)
    # command_result holds the result of running the command; if the command runs successfully command_result will be 0.
    # If it's not 0, there was an error running the command.
    print("command ran with exit code %d" % command_result)


if __name__ == '__main__':
    main()
