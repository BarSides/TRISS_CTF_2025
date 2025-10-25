# Name

Access Granted

## Authors

@sludgeworks + @weezy

## Difficulty

Beginner

## Overview

Good work! You used the intern's sloppy commit to access a user account, but
your work isn't done yet. Enumeration is the name of the game, and every new
profile tells a story if you bother to read it.  

Take a moment to explore the access you've been granted. Sometimes all you need
to do is look in the right location.

## Setup

This challenge must be unlocked only after the following flag(s) has been
submitted:

- `Intern Secrets`

## Hint

When adding content to a repo, remember... it’s all about location, location,
location!

## Flag

`flag{WhereInTheWorld}`

## Solution Summary

After logging into the Gitea instance with the credentials from the previous
challenge (`jforbes:barsides4lyfe`), participants can find the flag by
inspecting the `jforbes` user account. The flag `flag{WhereInTheWorld}` appears
either on the public profile page under "Location" or within the account
settings.

This challenge reinforces basic enumeration habits and encourages participants
to explore legitimate UI features rather than jump immediately to exploitation.
Difficulty is "Beginner" since no advanced tooling or privilege escalation is
required.
