# Name

Never Look Back

## Authors

@sludgeworks + @weezy

## Difficulty

Intermediate

## Overview

You now have access to the TRISS organization repository! Recent commits in
their flagship `PCG` repository show an attempt to tune deployment and
optimization parameters, followed by a rollback. The changes are configuration
focused, and something useful was touched during that edit cycle. Is it possible
interns aren't the only ones who make mistakes?

## Setup

This challenge must be unlocked only after the following flag(s) has been
submitted:

- `Intern Secrets`

## Hint

History keeps receipts, check what was added then removed.

## Flag

`flag{MichaelMyersIsMyIdol}`

## Solution Summary

The commit with SHA `f97350f057...` adds a .env file containing the following
entries:

```text
USR=stabby
PWD=stabs4death

# When submitting, remove underscores in following value:
PRIZE=f_l_a_g{MichaelMyersIsMyIdol}
```

The subsequent commit with `SHA 2b4eb27fa0 ...` reverts the addition and deletes
`MyEnvironment.asset`.

The intended flag is encoded in the `PRIZE` value, with underscores meant to be
removed prior to submission. Removing underscores from
`f_l_a_g{MichaelMyersIsMyIdol}` yields the flag `flag{MichaelMyersIsMyIdol}`.

The environment file also exposes credentials `stabby:stabs4death`. These
credentials may be usable to authenticate to the `stabby` account, and is the
next escalation vector for the chain of challenges.

The solve requires inspecting recent commit history and diffs, recognizing an
intentionally obfuscated flag string, and performing a simple transformation to
recover the flag. This goes beyond basic UI enumeration but does not require
privilege escalation or advanced tooling, so intermediate is appropriate.
