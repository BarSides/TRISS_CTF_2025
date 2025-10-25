# Name

Certified Babbler

## Authors

@sludgeworks + @weezy

## Difficulty

Easy

## Overview

Every organization has that one engineer who cannot resist leaving little
messages where they do not belong. Somewhere in the artifacts you've uncovered,
the same spirit lives on. It is meaningless to machines, but a careful eye will
find the slip—a human voice hidden inside an avalanche of data.

## Setup

This challenge must be unlocked only after the following flag(s) has been
submitted:

- `Intern Secrets`
- `Never Look Back`
- `Corporate Retreat`

## Hint

Even certificates have something to say if you read between the lines.

## Flag

`flag{Ha!MadeYouDigThroughAllThatBase64!}`

## Solution Summary

Participants download `corporate.ovpn` from the release and inspect its
contents. Amid long Base64-like blocks designed to appear as binary data, the
file contains a literal token formatted like an in-challenge marker:
`FlaG{Ha!MadeYouDigThroughAllThatBase64!}`. The token is embedded inside a noisy
block rather than presented as a separate line, so solving requires scanning or
grepping for irregular ASCII within otherwise encoded data.

This challenge is deemed as "Easy" due to no need of decoding the surrounding
block so they can find it with a simple search for the word "flag".
