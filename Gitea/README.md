# CTF Challenges

## Overview

A seemingly innocent fork of an intern project turns into a pipeline-driven
compromise. An exposed workflow contains secrets, those credentials unlock an
account, and a sequence of repository artifacts and user-scoped configuration
values provide the pivot points into progressively more sensitive context. The
chain emphasizes operational hygiene failures rather than exotic exploits,
teaching participants how small misconfigurations and leaked secrets can be
chained into a significant intrusion.

> [!IMPORTANT]
> The `gitea-ctf/gitea/config/app.ini` contains a hardcoded configuration of
> `DOMAIN = gitea.triss.ctf`. This must be updated to reflect the hostname which
> will be used during the competition, or to a hardcoded IP that will be used
> to access the service

## Attack/Escalation Path

1. [X] Initial access through hardcoded password in action
2. [X] Engineer can see commit history (`.env`) containing hardcoded creds for integration role user (Stabby)
3. [X] Stabby can see release with `steelers` creds embedded

## Flags

1. [X] In webhook along with initial access password ([Flag 01 Writeup])
2. [X] jforbes' profile has a flag in location field ([Flag 02 Writeup])
3. [X] Flag in commit from stabby in org repo Pull Request (`.env` file) ([Flag 03 Writeup])
4. [X] stabby's profile has a variable that has a flag in it ([Flag 04 Writeup])
5. [x] flag in openvpn config as b64 blob  `setenv FLAG` in  `# Auth secrets` section ([Flag 05 Writeup])
6. [x] bonus flag in middle of `<ctf>` section of openvpn config ([Flag 06 Writeup])
7. [x] steelers's profile has a flag inside webhook auth header ([Flag 07 Writeup])

## Users

### John Dorian (Intern)

```yaml
username: intern (intern@triss.ctf)
password: c3VwZXJtZW1vcmFibGU=
```

### Justin Forbes (Engineer)

```yaml
username: jforbes (jforbes@triss.ctf)
password: barsides4lyfe
```

### Shane Tabby (Bad developer)

```yaml
username: stabby (stabby@triss.ctf)
password: stabs4death
```

### Scott Teelers (Publisher)

```yaml
username: steelers (steelers@triss.ctf)
password: Goin2SupahBowl!
```

### Adam Aron (Org Admin)

```yaml
username: aaron (aaron@triss.ctf)
password: TRISS4Life!
```

### Admin (gitea admin)

```yaml
username: admin (admin@triss.ctf)
password: c3VwZXJtZW1vcmFibGU=
```


[Flag 01 Writeup]: 01%20-%20Beginner%20-%20Intern%20Secrets.md
[Flag 02 Writeup]: 02%20-%20Beginner%20-%20Access%20Granted.md
[Flag 03 Writeup]: 03%20-%20Intermediate%20-%20Never%20Look%20Back.md
[Flag 04 Writeup]: 04%20-%20Beginner%20-%20Loose%20Lips%20Sink%20Scripts.md
[Flag 05 Writeup]: 05%20-%20Intermediate%20-%20Corporate%20Retreat.md
[Flag 06 Writeup]: 06%20-%20Beginner%20-%20Certified%20Babbler.md
[Flag 07 Writeup]: 07%20-%20Intermediate%20-%20Hook%20Route.md
