#!/usr/bin/env bash
#
# MOTHERBROOD - Raspberry Pi setup
# Rebuilds the Pi side of the installation on a fresh Bookworm 64-bit image.
#
#   chmod +x setup.sh
#   ./setup.sh
#
# Safe to re-run: every step checks before it acts.
# Some steps need a GUI or a human decision - see MANUAL STEPS at the end.

set -e   # stop on the first error

PD_VERSION="0.56-5"                       # ELSE 1.0-0 rc-14 needs Pd 0.56+
PROJECT_DIR="$HOME/MOTHERBROOD"
ELSE_DIR="$HOME/Documents/else"
BUILD_DIR="$HOME/pd-build"

echo "=== MOTHERBROOD Pi setup ==="

# ─── 1. SYSTEM PACKAGES ────────────────────────────────────
# build-essential..tk-dev are what Pd needs to compile from source.
# libasound2-dev is the important one: without it Pd has no ALSA output.
echo "--- installing packages"
sudo apt update
sudo apt install -y \
  git python3-venv python3-pip \
  alsa-utils \
  build-essential automake autoconf libtool gettext \
  libasound2-dev tk-dev

# ─── 2. SERIAL PORT PERMISSIONS ────────────────────────────
# Reading the mother ESP over USB needs the dialout group.
# Takes effect after logout/login (or reboot).
if id -nG "$USER" | grep -qw dialout; then
  echo "--- $USER already in dialout"
else
  echo "--- adding $USER to dialout (log out and back in for this to apply)"
  sudo usermod -aG dialout "$USER"
fi

# ─── 3. DAC HAT (PCM5122) ──────────────────────────────────
# The Pi does not detect an audio HAT on its own - the overlay names the chip.
# Onboard audio goes off so the HAT is the only sound card.
CONFIG="/boot/firmware/config.txt"                 # Bookworm path
[ -f "$CONFIG" ] || CONFIG="/boot/config.txt"      # older path

echo "--- configuring DAC HAT in $CONFIG"
if grep -q "^dtoverlay=hifiberry-dacplus" "$CONFIG"; then
  echo "    overlay already present"
else
  # [all] makes sure the line is not trapped inside a model-specific section
  printf '\n[all]\ndtoverlay=hifiberry-dacplus\n' | sudo tee -a "$CONFIG" > /dev/null
  echo "    overlay added (reboot required)"
fi

if grep -q "^dtparam=audio=on" "$CONFIG"; then
  sudo sed -i 's/^dtparam=audio=on/dtparam=audio=off/' "$CONFIG"
  echo "    onboard audio disabled (reboot required)"
fi

# ─── 4. PURE DATA 0.56 FROM SOURCE ─────────────────────────
# Debian only ships 0.55, which ELSE 1.0 refuses to run on.
# This installs to /usr/local/bin/pd; Debian's stays at /usr/bin/pd.
if [ -x /usr/local/bin/pd ]; then
  echo "--- Pd already built at /usr/local/bin/pd"
else
  echo "--- building Pd $PD_VERSION (several minutes)"
  mkdir -p "$BUILD_DIR"
  cd "$BUILD_DIR"

  if [ ! -d "pure-data-$PD_VERSION" ]; then
    wget "https://github.com/pure-data/pure-data/archive/refs/tags/$PD_VERSION.tar.gz"
    tar xf "$PD_VERSION.tar.gz"
  fi

  cd "pure-data-$PD_VERSION"
  ./autogen.sh                 # the git/tag source has no ready-made configure
  ./configure --enable-alsa
  make -j4
  sudo make install
  sudo ldconfig
fi

/usr/local/bin/pd -nogui -version 2>&1 | head -1 || true

# ─── 5. PYTHON ENVIRONMENT ─────────────────────────────────
# The venv belongs to this machine and is never committed to git.
if [ -d "$PROJECT_DIR" ]; then
  echo "--- setting up venv in $PROJECT_DIR"
  cd "$PROJECT_DIR"
  [ -d venv ] || python3 -m venv venv
  ./venv/bin/pip install --upgrade pip
  if [ -f requirements.txt ]; then
    ./venv/bin/pip install -r requirements.txt
  else
    ./venv/bin/pip install pyserial python-osc
  fi
else
  echo "--- $PROJECT_DIR not found; clone the repo, then re-run this script"
fi

# ─── 6. AUDIO MIXER ────────────────────────────────────────
# The PCM5122's internal Digital volume starts muted - silent DAC, working driver.
echo "--- unmuting the HAT (fails harmlessly until after the reboot)"
amixer -c sndrpihifiberry sset Digital unmute        2>/dev/null || true
amixer -c sndrpihifiberry sset Digital 80%           2>/dev/null || true
sudo alsactl store                                   2>/dev/null || true

# ─── DONE ──────────────────────────────────────────────────
cat <<'EOF'

=== automated steps done ===

MANUAL STEPS (need a GUI or a human decision):

1. REBOOT if the DAC overlay or onboard audio changed.

2. Check the HAT is there and audible:
     aplay -l
     speaker-test -D plughw:CARD=sndrpihifiberry -c 2 -t sine
   If silent, open  alsamixer -c sndrpihifiberry  and unmute "Digital" (M key).
   Then:  sudo alsactl store

3. Install ELSE externals (needs the desktop - Deken has no CLI here):
     open Pd  ->  Help -> Find externals  ->  search "else"  ->  install
   It lands in ~/Documents/else . If the folder is named with a version,
   rename it to plain "else" or update PD_EXTERNALS_PATH in the code.
   Verify:
     /usr/local/bin/pd -verbose -nogui -path ~/Documents/else -lib else -send "pd quit"
   Expect the ELSE banner with no "needs at least Pd 0.56" error.

4. Point the GUI Pd at ELSE too (Preferences -> Path), so patches open the
   same way in the editor as they run headless. Also check the desktop
   launcher runs /usr/local/bin/pd and not Debian's older /usr/bin/pd:
     grep Exec /usr/share/applications/*puredata*

5. Find the mother ESP's serial port and update hardwareConstants.py:
     ls /dev/serial/by-id/
   Always use the by-id path, never /dev/ttyUSB0.

6. Check these constants in hardwareConstants.py:
     MOTHER_PORT           the by-id path from step 5
     MOTHER_BAUD           115200, matching Serial.begin on the mother
     PD_BINARY             /usr/local/bin/pd
     PD_EXTERNALS_PATH     /home/<user>/Documents/else
     PD_AUDIO_DEVICE_NAME  "snd_rpi_hifiberry_dacplus (plug-in)"
   The Pd audio device NUMBER is looked up by name at startup, never stored.

7. Run it:
     cd ~/MOTHERBROOD && source venv/bin/activate && python3 -m main

EOF