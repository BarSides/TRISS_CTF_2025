# Intern Secrets

## Authors

@sludgeworks + @weezy

## Difficulty

Easy

## Overview

Interns are always causing problems, aren't they? Late to pick up dry cleaning,
getting the wrong lunch orders, and now setting up workflows that send "urgent"
webhooks to their supervisor's personal server.

The good news? Their secret is sitting right in plain sight if you know where to
look. Take a peek at the intern's work, read between the lines, and see what
they've accidentally exposed.

## Setup

1. Stand up the Docker Compose file provided by the author.
2. In `gitea/config/app.ini`, update the following `DOMAIN` field to reflect the
   domain name or IP address the site will be reached at.

```ini
[server]
DOMAIN = gitea.triss.ctf
```

## Hint

Sometimes a little *action* is all you need to make the workflow reveal its
secrets.

## Flag

`flag{BarsidesForLyfe!}`

## Solution Summary

The participant navigates to the public Gitea instance and views the single
repository visible under the "Explore" tab. The only commit introduces a
`.github/workflows/pcg.yaml` file that contains a `curl` command. The URL
includes a Base64-encoded string: `ZmxhZ3tCYXJzaWRlc0Zvckx5ZmUhfQ0K`

Decoding the string reveals the flag `flag{BarsidesForLyfe!}`. The same line
also exposes hardcoded credentials for the user `jforbes`
(`jforbes:barsides4lyfe`). These credentials can be used to authenticate to the
Gitea web interface, revealing additional repositories and unlocking the next
stage of the challenge chain.

No external network requests are required to solve this challenge; decoding
locally is sufficient.

This challenge introduces participants to repository inspection, credential
discovery, and basic encoding recognition. Difficulty is rated "Easy" because
the solution path is direct and relies on fundamental analysis skills rather
than advanced exploitation.
