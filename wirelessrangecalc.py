#Range Calculator
#P(dBm) = 10 · log10(P(mW))
#Maximum path loss = transmit power – receiver sensitivity + gains – losses – fade margin
#Distance (km) = 10(maximum path loss – 32.44 – 20log(f))/20
import math
f = int(input("Enter the WiFi Frequency in (MHz): "))
transmit = int(input("Enter the transmit power (dBm): "))
receive = int(input("Enter the receiver sensitivity (dBm): "))
tgain = 6 #dBi #Modify as per the Wireless Equipment Standards
rgain = 6 #dBi
fade = 12 #dB
loss = 0 #dB
maxpathloss = (transmit - receive + tgain + rgain - loss - fade)
print(f"Max Path Loss is: {maxpathloss} dB")
x = math.log10(f)
distance = 10**((maxpathloss - 32.44 - (20*x))/20)
print(f"The range of WiFi is: {distance} Km")
