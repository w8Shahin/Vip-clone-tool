#!/bin/bash

# SHAHIN VIP GOLD TOOL - AUTO SETUP SCRIPT
# OWNER: SHAHIN BIN AHMED

echo -e "\033[1;92m[•] Updating System Packages...\033[1;97m"
pkg update && pkg upgrade -y

echo -e "\033[1;92m[•] Installing Python and Git...\033[1;97m"
pkg install python git -y

echo -e "\033[1;92m[•] Installing Espeak for Voice Alert...\033[1;97m"
pkg install espeak -y

echo -e "\033[1;92m[•] Installing Python Libraries (Requests, BS4, Futures)...\033[1;97m"
pip install requests bs4 futures

echo -e "\033[1;92m[•] Setting up Storage Permission...\033[1;97m"
termux-setup-storage

echo -e "\033[1;92m[•] All Setup Done! Starting SHAHIN VIP TOOL...\033[1;97m"
sleep 2

# Ekhane jodi apnar main file-er nam
