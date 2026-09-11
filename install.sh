#!/bin/bash

# 3MS Installer script
# Copyright (C) 2026 Christopher Mattar (3dcoded)

set -e

HH_REPO_URL="https://github.com/moggieuk/Happy-Hare.git"
BASE_CONFIG_URL="https://raw.githubusercontent.com/3DCoded/3MS/refs/heads/main/.base.mmu_config"

BLUE=$'\033[0;34m'
NC=$'\033[0m' # No Color / Reset

cd ~/

# Clone HH repo
WILL_CLONE=0
if [[ " $@ " =~ " -f" ]]; then
    echo "Force overwrite enabled. Removing existing Happy-Hare directory..."
    rm -rf Happy-Hare
    WILL_CLONE=1
elif [ -d "Happy-Hare" ]; then
    echo "Happy-Hare directory already exists. Pass -f to force overwrite."
else 
    WILL_CLONE=1
fi

if [ $WILL_CLONE -eq 1 ]; then
    echo "Cloning Happy-Hare repository..."
    git clone $HH_REPO_URL > /dev/null 2>&1
fi

cd Happy-Hare

# Copy base config
if [ -f ".mmu_config" ]; then
    printf "Config already exists. Overwrite? (y/n) "
    read -r answer
    if [ "$answer" = "y" ]; then
        cp .mmu_config .mmu_config.bak
        echo "Backup of existing config created as .mmu_config.bak"
        echo "Overwriting existing config..."
        wget $BASE_CONFIG_URL -O .mmu_config > /dev/null 2>&1
    else
        echo "Keeping existing config. No changes made."
    fi
else
    echo "Installing base configuration..."
    wget $BASE_CONFIG_URL -O .mmu_config > /dev/null 2>&1
fi

# Prompt user
echo "Next steps:"
echo "1. Run ${BLUE}./install.sh -i${NC}"
echo "2. Update any settings specific to your setup (non-kit builds)"
echo "3. Specify your serial address in the installer"
echo "4. Press Q, Y, then Enter to continue installation"
echo "5. Visit ${BLUE}https://3ms.3dcoded.xyz${NC} for further instructions"
echo "${BLUE}Happy Colorful Printing!${NC}"

printf "Press enter to open the installer or q to quit... "
read -r input
if [[ "$input" == "q" ]]; then
    echo "Exiting installer."
    exit 0
fi

./install.sh -i