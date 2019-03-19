"""
    Program for reading information from Tapelion tapes.
    Copyright (C) 2019 Dante James Falzone

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
import sys
from aubio import source
from aubio import pitch as freq
import numpy as np
import re
import pyaudio
import wave

original_data = []

def get_from_tape():
    print("(When entering data, it should be noted that uppercase characters tend to work better than lowercase.)")
    x = input()
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = x
    WAVE_OUTPUT_FILENAME = "tape_input.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Reading from audio input...")

    frames = []

    for i in range(0, int(RATE / int(CHUNK) * int(RECORD_SECONDS))):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Done reading.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    print("Processing data...")
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


    win_s = 4096
    hop_s = 512

    s = source("tape_input.wav", 44100, hop_s)
    samplerate = s.samplerate

    tolerance = 0.8

    pitch_o = freq("yin", win_s, hop_s, samplerate)
    pitch_o.set_unit("midi")
    pitch_o.set_tolerance(tolerance)

    pitches = []
    confidences = []

    total_frames = 0
    while True:
        samples, read = s()
        pitch = pitch_o(samples)[0]
        pitches += [pitch]
        confidence = pitch_o.get_confidence()
        confidences += [confidence]
        total_frames += read
        if read < hop_s: break


    #print("Average frequency = " + str(np.array(pitches).mean()) + " hz")

    numbers = []
    for x in pitches:
        if int(x) in range (62, 63):
            numbers.append("0")
        elif int(x) in range (73, 74):
            numbers.append("1")
        elif int(x) in range (78, 82):
            numbers.append("2")
        elif int(x) in range (84, 87):
            numbers.append("3")
        elif int(x) in range (88, 89):
            numbers.append("4")
        elif int(x) in range (91, 92):
            numbers.append("5")
        elif int(x) in range (94, 95):
            numbers.append("6")
        elif int(x) in range (96, 97):
            numbers.append("7")
        elif int(x) in range (98, 99):
            numbers.append("8")
        elif int(x) in range (100, 101):
            numbers.append("9")
        elif int(x) == 102:
            numbers.append("NULL")

    #print(pitches)

    aux_list = []
    for i in range(len(numbers)):
        if not numbers[i] == numbers[i-1]:
            aux_list.append(numbers[i])

    #print(aux_list)

    interpret = ''.join(aux_list)

    #print(interpret)

    text_chunks = interpret.split("ULL")

    print(','.join(text_chunks))

    output = []

    def ascii_to_char(text):
        codeb = re.search('\d+N', text)
        space = re.search('032N', text)
        exclm = re.search('03N',  text)
        dblqt = re.search('034N', text)
        hshtg = re.search('035N', text)
        dollr = re.search('036N', text)
        perid = re.search('046N', text)
        comma = re.search('04N',  text)
        newln = re.search('012N', text)
        A = re.search('065N', text)
        B = re.search('06N', text)
        C = re.search('067N', text)
        D = re.search('068N', text)
        E = re.search('069N', text)
        F = re.search('070N', text)
        G = re.search('071N', text)
        H = re.search('072N', text)
        I = re.search('073N', text)
        J = re.search('074N', text)
        K = re.search('075N', text)
        L = re.search('076N', text)
        M = re.search('07N', text)
        N = re.search('078N', text)
        O = re.search('079N', text)
        P = re.search('080N', text)
        Q = re.search('081N', text)
        R = re.search('082N', text)
        S = re.search('083N', text)
        T = re.search('084N', text)
        U = re.search('085N', text)
        V = re.search('086N', text)
        W = re.search('087N', text)
        X = re.search('08N', text)
        Y = re.search('089N', text)
        Z = re.search('090N', text)
        lower = re.search('980N', text)
        apost = re.search('039N', text) # '
        prcnt = re.search('037N', text) # %
        amprs = re.search('038N', text) # &
        opren = re.search('040N', text) # (
        closp = re.search('041N', text) # )
        aster = re.search('042N', text) # *
        pluss = re.search('043N', text) # +
        minus = re.search('045N', text) # -
        fslsh = re.search('047N', text) # /
        zero  = re.search('048N', text) # 0
        one   = re.search('049N', text) # 1
        two   = re.search('050N', text) # 2
        three = re.search('051N', text) # 3
        four  = re.search('052N', text) # 4
        five  = re.search('053N', text) # 5
        six   = re.search('054N', text) # 6
        seven = re.search('05N', text)  # 7
        eight = re.search('056N', text) # 8
        nine  = re.search('057N', text) # 9
        colon = re.search('058N', text) # :
        semic = re.search('059N', text) # ;
        opena = re.search('060N', text) # <
        equal = re.search('061N', text) # =
        closa = re.search('062N', text) # >
        quest = re.search('063N', text) # ?
        atsgn = re.search('064N', text) # @
        opnbr = re.search('091N', text) # [
        bcksl = re.search('092N', text) # \
        closb = re.search('093N', text) # ]
        dimak = re.search('094N', text) # ^
        under = re.search('095N', text) # _
        acute = re.search('096N', text) # `
        openc = re.search('123N', text) # {
        pipes = re.search('124N', text) # |
        closc = re.search('125N', text) # }
        tilde = re.search('126N', text) # ~

        if space:
            output.append(' ')
        elif exclm:
            output.append('!')
        elif dblqt:
            output.append('"')
        elif hshtg:
            output.append('#')
        elif dollr:
            output.append('$')
        elif perid:
            output.append('.')
        elif comma:
            output.append(',')
        elif A:
            output.append('A')
        elif B:
            output.append('B')
        elif C:
            output.append('C')
        elif D:
            output.append('D')
        elif E:
            output.append('E')
        elif F:
            output.append('F')
        elif G:
            output.append('G')
        elif H:
            output.append('H')
        elif I:
            output.append('I')
        elif J:
            output.append('J')
        elif K:
            output.append('K')
        elif L:
            output.append('L')
        elif M:
            output.append('M')
        elif N:
            output.append('N')
        elif O:
            output.append('O')
        elif P:
            output.append('P')
        elif Q:
            output.append('Q')
        elif R:
            output.append('R')
        elif S:
            output.append('S')
        elif T:
            output.append('T')
        elif U:
            output.append('U')
        elif V:
            output.append('V')
        elif W:
            output.append('W')
        elif X:
            output.append('X')
        elif Y:
            output.append('Y')
        elif Z:
            output.append('Z')
        elif newln:
            output.append('\n')
        elif lower:
            output.append('܍')
        elif apost:
            output.append('\'')
        elif prcnt:
            output.append('%')
        elif amprs:
            output.append('&')
        elif opren:
            output.append('(')
        elif closp:
            output.append(')')
        elif aster:
            output.append('*')
        elif pluss:
            output.append('+')
        elif minus:
            output.append('-')
        elif fslsh:
            output.append('/')
        elif zero:
            output.append('0')
        elif one:
            output.append('1')
        elif two:
            output.append('2')
        elif three:
            output.append('3')
        elif four:
            output.append('4')
        elif five:
            output.append('5')
        elif six:
            output.append('6')
        elif seven:
            output.append('7')
        elif eight:
            output.append('8')
        elif nine:
            output.append('9')
        elif colon:
            output.append(':')
        elif semic:
            output.append(';')
        elif opena:
            output.append('<')
        elif equal:
            output.append('=')
        elif closa:
            output.append('>')
        elif quest:
            output.append('?')
        elif atsgn:
            output.append('@')
        elif opnbr:
            output.append('[')
        elif bcksl:
            output.append('\\')
        elif closb:
            output.append(']')
        elif dimak:
            output.append('^')
        elif under:
            output.append('_')
        elif acute:
            output.append('`')
        elif openc:
            output.append('{')
        elif pipes:
            output.append('|')
        elif closc:
            output.append('}')
        elif tilde:
            output.append('~')

        else:
            if codeb:
                output.append('␕') # prints the ascii "negative acknowledgement" character

    for x in text_chunks:
        ascii_to_char(x)

    format = []
    for i in range (0, len(output)):
        try:
            if output[i] == "܍":
                output[i + 1] = output[i + 1].lower()
                output.remove(output[i])
        except IndexError:
            continue
    return(''.join(output))

print("Make sure you know ahead of time the start and end times for your data.")
print("Would you like to use error-checking? This is an experimental feature and takes three times as long,")
print("but it might help preserve your data. [y/n]")
choice = input()
if choice == "y":
    print("Set your recording medium to the start position of your data.")
    print("Then type in how many seconds to read.")
    first_pass = get_from_tape()
    print("Now rewind back to the start position of your data to read the data a second time.")
    print("Then type in once more how many seconds to read.")
    second_pass = get_from_tape()
    print("Now rewind again to the start position of your data to read a third time.")
    print("Then type in for the third and last time how many seconds to read.")
    third_pass = get_from_tape()

    # Error-checking algorithm
    def reconstruct(x, y, z):
        x_list = []
        y_list = []
        z_list = []
        for char in x:
            x_list.append(char)
        for char in y:
            y_list.append(char)
        for char in z:
            z_list.append(char)

        # Pick out the characters that match; reject errors and non-
        # matching characters.
        x_y_common = []
        for i in range (0, len(x_list)):
            try:
                if x_list[i] == y_list[i]:
                    x_y_common.append(x_list[i])
                elif y_list[i] == "␕":
                    x_y_common.append(x_list[i])
                elif x_list[i] == "␕":
                    x_y_common.append(y_list[i])
                elif x_list[i] != y_list[i]:
                    x_y_common.append("␕")
            except IndexError:
                x_y_common.append(x_list[i])


        y_z_common = []
        for i in range (0, len(y_list)): # github.com/DanteFalzone0
            try:
                if y_list[i] == z_list[i]:
                    y_z_common.append(y_list[i])
                elif y_list[i] == "␕":
                    y_z_common.append(z_list[i])
                elif z_list[i] == "␕":
                    y_z_common.append(y_list[i])
                elif z_list[i] != y_list[i]:
                    y_z_common.append("␕")
            except IndexError:
                y_z_common.append(y_list[i])

        x_z_common = []
        for i in range (0, len(z_list)):
            try:
                if z_list[i] == x_list[i]:
                    x_z_common.append(x_list[i])
                elif z_list[i] == "␕":
                    x_z_common.append(x_list[i])
                elif x_list[i] == "␕":
                    x_z_common.append(z_list[i])
                elif z_list[i] != x_list[i]:
                    x_z_common.append("␕")
            except IndexError:
                x_z_common.append(z_list[i])

        opt0 = ''.join(x_y_common)
        opt1 = ''.join(y_z_common)
        opt2 = ''.join(x_z_common)

        # If any of the results don't have error characters, print that one.
        if "␕" in opt0:
            if "␕" in opt1:
                if "␕" in opt2:
                    try:
                        # If all of the results have error characters, try running them through the algorithm again.
                        reconstruct(opt0, opt1, opt2)
                    except RecursionError:
                        # If running the results through the algorithm a bunch of times doesn't help,
                        # weight them according to how many errors they have and print the one with the least.
                        xweight = 0
                        yweight = 0
                        zweight = 0
                        for char in opt0:
                            if char == "␕":
                                xweight += 1
                        for char in opt1:
                            if char == "␕":
                                yweight += 1
                        for char in opt2:
                            if char == "␕":
                                zweight += 1
                        if xweight >= yweight >= zweight:
                            print(opt2)
                        elif xweight >= zweight >= yweight:
                            print(opt1)
                        elif yweight >= zweight >= xweight:
                            print(opt0)
                        elif yweight >= xweight >= zweight:
                            print(opt2)
                        elif zweight >= yweight >= xweight:
                            print(opt0)
                        elif zweight >= xweight >= yweight:
                            print(opt1)
                else:
                    print(opt2)
            else:
                print(opt1)
        else:
            print(opt0)

    print("Finished processing data.")
    print("There may be corrupted characters in your data. Look over it to make corrections.")
    print("Data input:")
    for x in original_data:
        print(x)
    print("Data processed for error removal:")
    reconstruct(first_pass, second_pass, third_pass)
else:
    print("Set your recording medium to the start position of your data.")
    print("Then type in how many seconds to read from the medium.")
    print(get_from_tape())
