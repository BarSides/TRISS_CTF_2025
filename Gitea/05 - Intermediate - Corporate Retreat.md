# Name

Corporate Retreat

## Authors

@sludgeworks + @weezy

## Difficulty

Intermediate

## Overview

What begins as a careless intern project can ripple through a pipeline and
become the foothold an attacker needs. An exposed repository can lead to
compromised credentials... but does it stop at Gitea access?

With all the access you have uncovered, see if you can find the potential path
into the their corporate network.

## Setup

This challenge must be unlocked only after the following flag(s) has been
submitted:

- `Intern Secrets`
- `Never Look Back`

## Hint

Every release tells a story. Some stories should have stayed unpublished.

## Flag

`flag{ThisIsHowBadGuysGetIn}`

## Solution Summary

Participants enumerate the `PCG` repository "Releases" page, download
`corporate.ovpn` from release `v1.0.0`, and inspect its contents. The file
contains the following environment assignment:

`setenv FLAG ZmxhZ3tUaGlzSXNIb3dCYWRHdXlzR2V0SW59`

The Base64 value decodes to the flag `flag{ThisIsHowBadGuysGetIn}`. No network
access or VPN connection is required; the solve is purely offline inspection and
simple decoding.

The solve requires unpacking releases, recognizing an intentionally obfuscated
flag string, and decoding Base64 to recover the flag. This goes beyond basic UI
enumeration but does not require advanced tooling, so intermediate is
appropriate.
