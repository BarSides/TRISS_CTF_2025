# Overview

> ## Who Knew
> **Description**\
> I'm sure it was a good idea at some point, but this lack of support has really got me scratching my header.
>
> **Assets**\
> GZIPFILE01.gz

# Walkthrough

We start by right-clicking GZIPFILE01.gz and choosing to extract. That results in this_is_a_clue.txt for us to look at.
```
this_is_a_clue.txt

https://www.youtube.com/watch?v=oHg5SJYRHA0

Did you check the comments?
Did you check the right comments?

```

The youtube video is a RickRoll, and there are close to a quarter million comments, so we probably don't want to read those. The clue also suggests we read the right comments, but where are the right comments?.

A little searching around leads us to find out that the gzip specification contains a "fcomment" in [RFC 1952](https://www.rfc-editor.org/rfc/rfc1952) and that it can contain null terminated string data.\
It also turns out that may common gzip programs and libraries ignore this data. 

We could use a hex editor to examine the file header, but we can also just check for strings:
```
strings GZIPFILE01.gz 
GZIPFILE02.gz
The flag is in the zip file
v-TX
UTsb
SRRR
wU~\
rglW
\~?O
wEDOg
6633s
```

So it looks like there is a comment telling us the flag is in the zip file, but this is a gzip file, right?

```
file GZIPFILE01.gz 
GZIPFILE01.gz: gzip compressed data, was "GZIPFILE02.gz", has comment, last modified: Mon Oct 27 16:18:00 2025, from Unix, original size modulo 2^32 853
```

That shows us that there is a comment in this file, and that the original name was GZIPFILE02.gz, which we did not see when we extracted it with the GUI. Let's try to extract that file on the command line. We'll use the -N option to use the original name stored in the header.

```
gunzip -k -N GZIPFILE01.gz
```
That gives us GZIPFILE02.gz, so we'll try strings on that
```
strings GZIPFILE02.gz 
GZIPFILE03.gz
UEsDBBQACAAIABBhW1sAAAAAAAAAAMYC
GZIPFILE04.gz
AAAIACAAZmxhZy50eHRVVA0ABwCZ/2jf
GZIPFILE05.gz
mP9oAJn/aHV4CwABBOkDAAAE6QMAANPW
;1840
ttts

...

```

It would appear that we have nested gzip files which have what looks to be base64 FCOMMENT sections. Checking the first section we see that it decodes to something that starts with `PK\x03\x04`; the magic number for a zip file.

Since we don't know how many levels of nesting we have, let's use a script to do the extraction.
```bash
#!/bin/bash

CURRENT_FILE="GZIPFILE01.gz"
PREFIX="GZIPFILE"
MAX_EXTRACTS=100

for (( i=1; i <= MAX_EXTRACTS; i++ )); do
    if [ ! -f "$CURRENT_FILE" ]; then
        break
    fi
    
    NEXT_NUM=$((i + 1))
    NEXT_FILENAME=$(printf "%s%02d%s" "$PREFIX" "$NEXT_NUM" ".gz")
    
    gunzip -k -N "$CURRENT_FILE"
    
    if [ $? -ne 0 ]; then
        echo "Failed extacting $CURRENT_FILE"
        break
    fi
    
    if [ -f "$NEXT_FILENAME" ]; then
        CURRENT_FILE="${NEXT_FILENAME}"
    else
        break
    fi
done
```

Now we have all the gzip files, so let's get all the FCOMMENT fields

```
strings -n10 *.gz > fcomments.txt
```
That worked, but there appears to be a bit of duplication that we will need to clean up manually
```
GZIPFILE02.gz
The flag is in the zip file
GZIPFILE03.gz
UEsDBBQACAAIABBhW1sAAAAAAAAAAMYC
GZIPFILE04.gz
AAAIACAAZmxhZy50eHRVVA0ABwCZ/2jf
GZIPFILE05.gz
mP9oAJn/aHV4CwABBOkDAAAE6QMAANPW
GZIPFILE04.gz                    <- duplicate
AAAIACAAZmxhZy50eHRVVA0ABwCZ/2jf <- duplicate
GZIPFILE05.gz                    <- duplicate
mP9oAJn/aHV4CwABBOkDAAAE6QMAANPW <- duplicate
GZIPFILE05.gz                    <- duplicate
mP9oAJn/aHV4CwABBOkDAAAE6QMAANPW <- duplicate
...
```
After the cleanup we have
```
UEsDBBQACAAIABBhW1sAAAAAAAAAAMYC
AAAIACAAZmxhZy50eHRVVA0ABwCZ/2jf
mP9oAJn/aHV4CwABBOkDAAAE6QMAANPW
pRrQ5qpR0KaSUQo1QMNqFKgCauhlmFNi
UXBmSmpxdY6huXlOanypqXFKfJqxSUlp
kXHtgLqMTMOoGJtUMgpiHAYAAFBLBwiM
uFVzRQAAAMYCAABQSwECFAMUAAgACAAQ
YVtbjLhVc0UAAADGAgAACAAgAAAAAAAA
AAAAtIEAAAAAZmxhZy50eHRVVA0ABwCZ
/2jfmP9oAJn/aHV4CwABBOkDAAAE6QMA
AFBLBQYAAAAAAQABAFYAAACbAAAAAAA=
```
We can decode that into our zip file

```
cat fcomments.txt | base64 -d > flag.zip
```
In the zip file we find flag.txt which contains the flag.
```
BarSides{l177le_u53d_f34tur3}
```