# A single command to read data from the tape.
tapelion_read() {
    python3 ./demod.py;
}

# A single command to write data to the tape.
tapelion_write() {
    g++ tapewrite.cpp -o tapewrite;
    ./tapewrite;
}
