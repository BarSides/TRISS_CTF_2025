# Name

Loose Lips Sink Scripts

## Authors

@sludgeworks + @weezy

## Difficulty

Beginner

## Overview

The deeper you dig, the clearer it becomes that the intern was never really the
problem. Bad habits start higher up. The seasoned engineers talk about "secure
pipelines" while accidentally committing secrets into their own repositories.
Every account you open tells the same story: carelessness can be passed down
like tribal knowledge.  

Check how the "professionals" have been handling their automation, and you might
understand where the intern learned it.

## Setup

This challenge must be unlocked only after the following flag(s) has been
submitted:

- `Intern Secrets`
- `Never Look Back`

## Hint

Even the best engineers leave a trace when they think no one's looking

## Flag

`flag{NobodyLikesSecrets}`

## Solution Summary

The `stabby` account contains a user-scoped Actions variable with key `FLAG` and
value `flag{NobodyLikesSecrets}`. After authenticating as `stabby`, the
participant can navigate to "User Settings" -> "Actions" -> "Variables", and
read the value directly.

This challenge reinforces basic enumeration habits and encourages participants
to explore legitimate UI features rather than jump immediately to exploitation.
Difficulty is "Beginner" since no advanced tooling or privilege escalation is
required.
