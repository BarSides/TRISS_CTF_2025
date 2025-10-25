# Name

Hook Route

## Authors

@sludgeworks + @weezy

## Difficulty

Medium

## Overview

Every breach has a game plan, even if no one admits to drawing it up. What
started as a rookie mistake turned into a full drive down the field, each
account and artifact another yard gained. The attackers watched, studied the
playbook, and waited for their opening.

The final move was pure execution, a simple hook route that slipped through
unnoticed. It was short, precise, and devastatingly effective. All it took was
one stored configuration, one forgotten header, and the defense never saw it
coming.

You’ve followed every play so far. Now it’s time to read the field yourself. Can
you find the final route that got the attackers into the end zone?

## Setup

- `Intern Secrets`
- `Never Look Back`
- `Corporate Retreat`

## Hint

Check the account settings for anything that looks like a playcall, then decode
what the playbook hides.

## Flag

`flag{ANOTHER_FLAG?!}`

## Solution Summary

After authenticating as the `steelers` user, participants navigate to User Settings then Webhooks. The webhook entry for `https://triss.ctf` contains an Authorization header with a long Base64 string:

```
Vm1wSmQyVkZOVWhTYTJScFRUTkNjbFZzVm5kV2JHeFpZMGhPVjJKR1ZqTldiWGhyVm1zeFdGcEVUbGROYms0MFZsZDRZVmRHVWxsWGJGSlhZbGRSZWxaVldrWlBWa0pTVUZRd1BRPT0
```


The header value is Base64 encoded multiple times. Decoding it repeatedly yields
the flag: `flag{ANOTHER_FLAG?!}`.

This challenge requires players to connect several learned skills from earlier
stages rather than relying on a single trick. The steps involve moderate
enumeration, attention to detail within an application’s user interface, and
layered data decoding. None of these tasks are complex alone, but together they
make up an intermediate-level challenge.
