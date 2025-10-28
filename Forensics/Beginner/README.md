# Name
Vat of Acid 1

## Author
@witchofthewires

## Overview
Like any good hacker con, TRISS keeps a vat of muriatic acid boiling at all times, for reasons which are obvious. However, just before the conference began, someone manipulated the vat temperature controller, taking it from the recommended 437 degrees Fahrenheit to a deadly 842 degrees Fahrenheit!!! Fortunately, like any good hacker con, TRISS also keeps a world-class ICS/OT SOC working at all times, and they've been able to identify a traffic capture containing the malicious manipulation. Since the PLC and HMI are truly airgapped, the attacker must have been physically present in the room with the vat when the attack occurred. By cross-referencing physical access logs with the precise timestamp of the attack, we should be able to find our attacker!

Examine the attached file 'vat_of_acid.pcap', which started capturing at 2025-10-28 0600 EDT. At what time did the attack occur? 

The flag format is "BarSides{GMT_DATETIME_IN_ISO_8601}". For instance, if the attack occured 5s after the capture began, the flag should be "BarSides{2025-10-28 10:00:05.000}". Round to the nearest millisecond.

## Setup
Ensure that 'vat_of_acid.pcap' is attached to the challenge.

## Flag
BarSides{2025-10-28 10:00:15.602}
