#   The scripts for using Tapelion in the Bourne-Again Shell.
#   Copyright (C) 2019  Dante James Falzone
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program. If not, see <https://www.gnu.org/licenses/>.

# A single command to read data from the tape.
tapelion_read() {
    cd ~/tapelion;
    python3 ./demod.py;
}

# A single command to write data to the tape.
tapelion_write() {
    cd ~/tapelion;
    g++ tapewrite.cpp -o tapewrite;
    ./tapewrite;
}
