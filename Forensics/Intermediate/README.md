# Name
Vat of Acid 2

## Author
@witchofthewires

## Overview
Oops! It turns out that TRISS doesn't want to restore the boiling vat of acid to the manufacturer-recommended 437 degrees Fahrenheit. TRISS has been in the boiling acid game for a *long* time, and they've got a secret temperature guaranteed to maximize the rate of reaction and create a perfect product every time, just like Grandma used to make. The secret temperature is so secret, in fact, that no one at TRISS knows what it is! Grandma TRISS comes and sets it before the conference every year, and physical access records show that this year she did so just before the PLC was hacked. 

We can't admit to Grandma TRISS that we were hacked, or that the secret temperature wasn't stored in an enterprise secrets vault for use in our incident response/disaster recovery plans - she'll be so disappointed in us!! Can you recover Grandma's secret boiling acid temperature from the PCAP?

The flag has format "BarSides{TEMPERATURE_IN_FAHRENHEIT}". For instance, if the temperature is 500 degrees F, the flag is simply "BarSides{500}".

## Setup
This challenge uses the PCAP previously provided for Forensics Beginner.

## Flag
BarSides{491}
