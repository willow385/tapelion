# Tapelion
A collection of programs for reading and writing data on cassette tapes with modern computers.

HOW TO USE THESE PROGRAMS.

0. It is advised that you should make a directory called "tapelion", like so:

    `mkdir ~/tapelion`

1. Place all the programs into the tapelion directory.

2. Source the "scripts.sh" file, like so:

    `source scripts.sh`

3. To write to a tape, use the following steps:

    0. Plug the line out (headphones/speaker jack) of your computer into the line in (microphone jack)
    of your tape deck. Make sure that a writable tape is loaded in the tape deck. Also make sure that
    sox is installed and will work with your line out.
    
    1. Use the command `tapelion_write` to write information to the tape. It will prompt you to type in
    a string. As of version 3, valid characters include the full ascii character set.
    
    2. Make sure that your tape deck is recording when you press ENTER to record your string. It is advised
    that you should listen to the data transfer ~~because data is beautiful~~ so that you know when to
    stop recording.

4. To read from the tape, use the following steps:

    0. Plug the line out from your tape deck into the line in to your computer.
    
    1. Use the command `tapelion_read`. Enter in the amount of the tape you wish to read. The program will
    give you a prompt asking if you would like to use error checking; you can try this, but it is slower,
    more complicated, and more prone to bugs.
    
    2. Play the tape while Tapelion loads data from it. Stop the tape when the data transfer is finished.
    The data stored in the tape will be printed to stdout at the bottom of your terminal.


Dependencies:

    Python:
        pip3, aubio, pyaudio, numpy, wave
    C++:
        g++
    Other:
        Bash
        portaudio19-dev (for Pyaudio)
        sox
