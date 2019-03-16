/*
    tapewrite.cpp - a C++ program for writing information on cassette tapes.
    Part of Tapelion.
    Copyright (C) 2019  Dante James Falzone

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
*/
#include <iostream>
#include <cstring>

using namespace std;

/* Each character consists of four  digits,  *
 * the first three representing the places   *
 * of the decimal representation of ascii    *
 * values for the characters and the fourth  *
 * being a "NULL" or buffer tone. They match *
 * to tones as follows:                      *
 * 0 : 300 Hz                                *
 * 1 : 570 Hz                                *
 * 2 : 840 Hz                                *
 * 3 : 1110 Hz                               *
 * 4 : 1380 Hz                               *
 * 5 : 1650 Hz                               *
 * 6 : 1920 Hz                               *
 * 7 : 2190 Hz                               *
 * 8 : 2460 Hz                               *
 * 9 : 2730 Hz                               *
 * NULL : 3000 Hz                            */

void tone(int x) {
    if (x == 0) {
        system("play -n synth 0.125 sin 300");
    } else if (x == 1) {
        system("play -n synth 0.125 sin 570");
    } else if (x == 2) {
        system("play -n synth 0.125 sin 840");
    } else if (x == 3) {
        system("play -n synth 0.125 sin 1110");
    } else if (x == 4) {
        system("play -n synth 0.125 sin 1380");
    } else if (x == 5) {
        system("play -n synth 0.125 sin 1650");
    } else if (x == 6) {
        system("play -n synth 0.125 sin 1920");
    } else if (x == 7) {
        system("play -n synth 0.125 sin 2190");
    } else if (x == 8) {
        system("play -n synth 0.125 sin 2460");
    } else if (x == 9) {
        system("play -n synth 0.125 sin 2730");
    }
}


// Takes 0.5 seconds to play each character.
void asc(int a, int b, int c) {
    tone(a);
    tone(b);
    tone(c);
    system("play -n synth 0.125 sin 3000");
}


// Ascii values used here. A 2250 Hz tone is used to separate bytes.
void to_bin(char x) {
    system("play -n synth 0.25 sin 2250");
    if (x == ' ') {
        asc(0, 3, 2);
    } else if (x == '!') {
        asc(0, 3, 3);
    } else if (x == '"') {
        asc(0, 3, 4);
    } else if (x == '#') {
        asc(0, 3, 5);
    } else if (x == '$') {
        asc(0, 3, 6);
    } else if (x == '.') {
        asc(0, 4, 6);
    } else if (x == ',') {
        asc(0, 4, 4);
    } else if (x == 'A') {
        asc(0, 6, 5);
    } else if (x == 'B') {
        asc(0, 6, 6);
    } else if (x == 'C') {
        asc(0, 6, 7);
    } else if (x == 'D') {
        asc(0, 6, 8);
    } else if (x == 'E') {
        asc(0, 6, 9);
    } else if (x == 'F') {
        asc(0, 7, 0);
    } else if (x == 'G') {
        asc(0, 7, 1);
    } else if (x == 'H') {
        asc(0, 7, 2);
    } else if (x == 'I') {
        asc(0, 7, 3);
    } else if (x == 'J') {
        asc(0, 7, 4);
    } else if (x == 'K') {
        asc(0, 7, 5);
    } else if (x == 'L') {
        asc(0, 7, 6);
    } else if (x == 'M') {
        asc(0, 7, 7);
    } else if (x == 'N') {
        asc(0, 7, 8);
    } else if (x == 'O') {
        asc(0, 7, 9);
    } else if (x == 'P') {
        asc(0, 8, 0);

    /* A random thought I just had: the digits of a           *
     * binary number can be thought of as forking             *
     * points along a tree. For example, suppose I            *
     * have a chunk of 3 bits. This can be mapped out         *
     * as follows:                                            *
     *                                                        *
     *                     START                              *
     *                    /     \                             *
     *                   /       \                            *
     *                  /         \                           *
     *                 1           0                          *
     *                / \         / \                         *
     *               /   \       /   \                        *
     *              1     0     1     0                       *
     *             / \   / \   / \   / \                      *
     *            1   0 1   0 1   0 1   0                     *
     *                                                        *
     * so that any possible 3-digit binary number can         *
     * be described as a specific path along this tree.       *
     * For example, `110` would be `left-left-right`.         *
     *                                                        *
     * Technically this is true for all number bases in       *
     * the set of real numbers of base n where n is a         *
     * whole number. But it works more complexly as n         *
     * approaches infinity; for example, creating such        *
     * a tree for decimal would mean that every node would    *
     * have ten branches.                                     *
     *                                                        *
     * This could also be viewed as a decision tree, or a     *
     * hierarchy of nested categories; for example, the left  *
     * half of the above tree could be thought of as `numbers *
     * that are equal to or greater than four`.               */

    } else if (x == 'Q') {
        asc(0, 8, 1);
    } else if (x == 'R') {
        asc(0, 8, 2);
    } else if (x == 'S') {
        asc(0, 8, 3);
    } else if (x == 'T') {
        asc(0, 8, 4);
    } else if (x == 'U') {
        asc(0, 8, 5);
    } else if (x == 'V') {
        asc(0, 8, 6);
    } else if (x == 'W') {
        asc(0, 8, 7);
    } else if (x == 'X') {
        asc(0, 8, 8);
    } else if (x == 'Y') {
        asc(0, 8, 9);
    } else if (x == 'Z') {
        asc(0, 9, 0);

    } else {
        cout << "FATAL ERROR invalid/unrecognized char" << endl;
    }
}


int main(void) {
    cout << "Type in the string that you wish to translate and press ENTER." << endl;
    string input;
    getline(cin, input);
    system("play -n synth 1 sin 3250"); // Demaracate start of file
    for (int i = 0; i < strlen(input.c_str()); i++) { // Convert the file into audio (stdin for the moment)
        to_bin(input.c_str()[i]);
        cout << input.c_str()[i];
    }
    system("play -n synth 1 sin 3250"); // Demarcate end of file
    cout << "Finished.\n";
    cout << "Loading time: ";
    float time = 2 + (0.5 * strlen(input.c_str()));
    cout << time << " seconds\n";
    cout << "Amount of data: ";
    float filesize = strlen(input.c_str());
    cout << filesize << " bytes (approx. " << (filesize / 1024) << " KB)\n";
    return 0;
}
