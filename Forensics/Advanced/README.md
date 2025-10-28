# Name
Vat of Acid 3

## Author
@witchofthewires

## Overview
Dani says she updated the temperature controller to set a coil indicator when the acid is overheated. However, the HMI must also be updated to display this value, and Dani refuses to do so herself, saying that she and the software 'are enemies now'. The compiled PLC program and HMI view are attached; what data address can the indicator coil be read at? 

The flag has format 'BarSides{DATA_ADDRESS}'. For instance, if the coil indicator has Modbus address %QW1, the flag is 'BarSides{400002}'.

## Setup
Ensure that the files 'plc.st' and 'hmi.json' are attached.

## Flag
BarSides{100241}
