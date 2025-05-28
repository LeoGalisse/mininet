#!/bin/bash

switches=$(sudo ovs-vsctl list-br)

for sw in $switches
do
    echo "Adicionando regras ARP/IP de flood para $sw..."
    sudo ovs-ofctl del-flows $sw
    sudo ovs-ofctl add-flow $sw "dl_type=0x806,actions=flood"   # ARP
    sudo ovs-ofctl add-flow $sw "dl_type=0x800,actions=flood"   # IP
done

echo "Regras ARP/IP adicionadas!"
