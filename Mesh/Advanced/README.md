# Name
Meshtastic 2

## Author
@witchofthewires

## Overview
[This challenge requires that Mesh Beginner be solved] Now that you're connected to Triss Mesh, you can sniff Meshberos traffic! This is a sophisticated new flag-granting protocol developed by top BarSides engineers for the purposes of this CTF. When a Flag-Requesting Node transmits 'flag $USER' on a Meshberos channel, a Flag-Granting Node will respond with a Golden Flag for CTF player $USER, valid on any challenge with Meshberos authentication enabled!

List of challenges with Meshberos authentication enabled:
- Meshtastic 2

## Setup
This challenge requires that a Flag-Granting Node and a Flag-Requesting Node be connected over Triss Mesh, a Meshtastic private channel with secret key as specified in the Mesh Beginner challenge. For the purposes of TRISS 2025, the challenge author will bring a LilyGo T-Deck to serve as the FRN and a custom Heltec v3-RPi Zero appliance to serve as the FGN.

## Flag
Flags are unique to each player $USER, with the following format:
BarSides{$md5sum($USER + "turkeyMezzatintSalt")}

For example, the flag for 'witchofthewires' is BarSides{$md5sum("witchofthewiresturkeyMezzatintSalt")}, or "BarSides{283be4cd6e51ba67b890950c583859b9}".
