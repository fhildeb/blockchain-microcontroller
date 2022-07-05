#Filter
tcp.port == 1883 || udp.port == 1883
tcp && mqtt

#Programm starten
sudo -E wireshark