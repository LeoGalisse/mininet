# Relatório de Exercício Mininet: Topologia Árvore e Topologia Customizada

* **Data:** 28 de maio de 2025
* **Ambiente:** Mininet executado via WSL2 no Windows 11

## 1. Criação da Topologia de Rede em Árvore

### 1.1. Comando de Criação

A topologia de árvore (profundidade 4, ramificação 3) foi criada com o comando:

```bash
sudo mn --topo tree,depth=4,fanout=3 --mac --link tc,bw=35
```

### 1.2. Descrição da Topologia

* **Estrutura:**

  * 1 switch raiz, que se ramifica em 3 switches filhos.
  * Cada switch, por sua vez, ramifica-se em 3 novos switches, formando uma árvore até a profundidade 4.
  * Nos switches das folhas, há hosts conectados.
* **Total:** 40 switches (s1-s40), 81 hosts (h1-h81).
* **Controlador:** O padrão do Mininet.
* **MAC:** Sequenciais, do tipo `00:00:00:00:00:01` até `00:00:00:00:00:51` para os hosts.
* **Banda:** 35 Mbps para todos os links (`tc` Linux).

Obs: além do script de criação, foi necessário adicionar forwarding nos switches devido a erro de comunicação entre os hosts

```bash
mininet> h1 ping -c 3 h81
PING 10.0.0.81 (10.0.0.81) 56(84) bytes of data.
From 10.0.0.1 icmp_seq=1 Destination Host Unreachable
From 10.0.0.1 icmp_seq=2 Destination Host Unreachable
From 10.0.0.1 icmp_seq=3 Destination Host Unreachable

--- 10.0.0.81 ping statistics ---
3 packets transmitted, 0 received, +3 errors, 100% packet loss, time 2029ms
pipe 3
```

Para isso foi desenvolvido o `add-flood.sh` para que isso seja feito de forma rápida e eficaz, sendo necessário ser executado sempre que uma nova topologia fosse adicionada. (bash3.md)

### 1.3. Desenho Ilustrativo da Topologia

A visualização da árvore foi gerada usando o script Python `draw_mininet_tree.py`, que utiliza a biblioteca `networkx` para criar o grafo da árvore:

![Topologia em árvore gerada pelo script draw\_mininet\_tree.py](Figure_1.png)

### 1.4. Inspeção da Rede

Após a criação, os seguintes comandos foram utilizados:

```bash
mininet> h1 ifconfig
h1-eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.0.1  netmask 255.0.0.0  broadcast 10.255.255.255
        inet6 fe80::200:ff:fe00:1  prefixlen 64  scopeid 0x20<link>
        ether 00:00:00:00:00:01  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

mininet> h1 ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: h1-eth0@if1021: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc htb state UP group default qlen 1000
    link/ether 00:00:00:00:00:01 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.0.0.1/8 brd 10.255.255.255 scope global h1-eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::200:ff:fe00:1/64 scope link
       valid_lft forever preferred_lft forever
mininet> h1 ping -c 1 h2
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=1.59 ms

--- 10.0.0.2 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 1.588/1.588/1.588/0.000 ms
mininet> h1 arp -n
Address                  HWtype  HWaddress           Flags Mask            Iface
10.0.0.2                 ether   00:00:00:00:00:02   C                     h1-eth0
mininet> s1 ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1382
        inet 172.25.134.146  netmask 255.255.240.0  broadcast 172.25.143.255
        inet6 fe80::215:5dff:fede:560f  prefixlen 64  scopeid 0x20<link>
        ether 00:15:5d:de:56:0f  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s1-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::109a:eaff:fe4c:f982  prefixlen 64  scopeid 0x20<link>
        ether 12:9a:ea:4c:f9:82  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
...

s9-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::18e1:1eff:fe2c:5d77  prefixlen 64  scopeid 0x20<link>
        ether 1a:e1:1e:2c:5d:77  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

Esses comandos retornaram a lista de todos os hosts, switches, controladores, suas interfaces, conexões, IPs e MACs, confirmando a correta construção da topologia. (bash1.md)

### 1.5. Teste de Conectividade

O comando `ping` foi utilizado para validar a comunicação entre os hosts:

```bash
mininet> h2 tcpdump -i h2-eth0 -n icmp &
mininet> h1 ping -c 3 h2
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=1.63 ms
64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=0.404 ms
64 bytes from 10.0.0.2: icmp_seq=3 ttl=64 time=0.291 ms

--- 10.0.0.2 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2005ms
rtt min/avg/max/mdev = 0.291/0.776/1.634/0.608 ms
mininet> h2 jobs
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on h2-eth0, link-type EN10MB (Ethernet), snapshot length 262144 bytes
14:24:02.715764 IP 10.0.0.1 > 10.0.0.2: ICMP echo request, id 11715, seq 1, length 64
14:24:02.715871 IP 10.0.0.2 > 10.0.0.1: ICMP echo reply, id 11715, seq 1, length 64
14:24:03.717095 IP 10.0.0.1 > 10.0.0.2: ICMP echo request, id 11715, seq 2, length 64
14:24:03.717178 IP 10.0.0.2 > 10.0.0.1: ICMP echo reply, id 11715, seq 2, length 64
14:24:04.719299 IP 10.0.0.1 > 10.0.0.2: ICMP echo request, id 11715, seq 3, length 64
14:24:04.719380 IP 10.0.0.2 > 10.0.0.1: ICMP echo reply, id 11715, seq 3, length 64
[1]+  Running                 tcpdump -i h2-eth0 -n icmp &
mininet> h2 kill %1

6 packets captured
6 packets received by filter
0 packets dropped by kernel
mininet> h4 tcpdump -i h4-eth0 -n icmp &
mininet> h1 ping -c 3 h4
PING 10.0.0.4 (10.0.0.4) 56(84) bytes of data.
64 bytes from 10.0.0.4: icmp_seq=1 ttl=64 time=5.56 ms
64 bytes from 10.0.0.4: icmp_seq=2 ttl=64 time=1.91 ms
64 bytes from 10.0.0.4: icmp_seq=3 ttl=64 time=1.07 ms

--- 10.0.0.4 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2004ms
rtt min/avg/max/mdev = 1.071/2.846/5.562/1.950 ms
mininet> h4 jobs
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on h4-eth0, link-type EN10MB (Ethernet), snapshot length 262144 bytes
14:25:49.482237 IP 10.0.0.1 > 10.0.0.4: ICMP echo request, id 11726, seq 1, length 64
14:25:49.482621 IP 10.0.0.4 > 10.0.0.1: ICMP echo reply, id 11726, seq 1, length 64
14:25:50.480728 IP 10.0.0.1 > 10.0.0.4: ICMP echo request, id 11726, seq 2, length 64
14:25:50.481014 IP 10.0.0.4 > 10.0.0.1: ICMP echo reply, id 11726, seq 2, length 64
14:25:51.482133 IP 10.0.0.1 > 10.0.0.4: ICMP echo request, id 11726, seq 3, length 64
14:25:51.482281 IP 10.0.0.4 > 10.0.0.1: ICMP echo reply, id 11726, seq 3, length 64
[1]+  Running                 tcpdump -i h4-eth0 -n icmp &
mininet> h4 kill %1

6 packets captured
6 packets received by filter
0 packets dropped by kernel
mininet> h81 tcpdump -i h81-eth0 -n icmp &
mininet> h1 ping -c 3 h81
PING 10.0.0.81 (10.0.0.81) 56(84) bytes of data.
64 bytes from 10.0.0.81: icmp_seq=1 ttl=64 time=8.97 ms
64 bytes from 10.0.0.81: icmp_seq=2 ttl=64 time=0.866 ms
64 bytes from 10.0.0.81: icmp_seq=3 ttl=64 time=1.21 ms

--- 10.0.0.81 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
rtt min/avg/max/mdev = 0.866/3.682/8.972/3.743 ms
mininet> h81 jobs
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on h81-eth0, link-type EN10MB (Ethernet), snapshot length 262144 bytes
14:26:38.002600 IP 10.0.0.1 > 10.0.0.81: ICMP echo request, id 11735, seq 1, length 64
14:26:38.002726 IP 10.0.0.81 > 10.0.0.1: ICMP echo reply, id 11735, seq 1, length 64
14:26:38.997281 IP 10.0.0.1 > 10.0.0.81: ICMP echo request, id 11735, seq 2, length 64
14:26:38.997387 IP 10.0.0.81 > 10.0.0.1: ICMP echo reply, id 11735, seq 2, length 64
14:26:39.999093 IP 10.0.0.1 > 10.0.0.81: ICMP echo request, id 11735, seq 3, length 64
14:26:39.999174 IP 10.0.0.81 > 10.0.0.1: ICMP echo reply, id 11735, seq 3, length 64
[1]+  Running                 tcpdump -i h81-eth0 -n icmp &
mininet> h81 kill %1

6 packets captured
6 packets received by filter
0 packets dropped by kernel
```

### 1.6 Testes com iperf

O comando `iperf` foi utilizado alterar os hosts para servidor e cliente e re comunicarem entre si.

35 Mbps

```bash
mininet> py h1.IP()
10.0.0.1
mininet> h1 iperf -s -p 5555 &
mininet> h2 iperf -c 10.0.0.1 -p 5555 -i 1 -t 20
------------------------------------------------------------
Client connecting to 10.0.0.1, TCP port 5555
TCP window size: 85.3 KByte (default)
------------------------------------------------------------
[  1] local 10.0.0.2 port 33958 connected with 10.0.0.1 port 5555 (icwnd/mss/irtt=14/1448/1453)
[ ID] Interval       Transfer     Bandwidth
[  1] 0.0000-1.0000 sec  4.25 MBytes  35.7 Mbits/sec
[  1] 1.0000-2.0000 sec  4.12 MBytes  34.6 Mbits/sec
[  1] 2.0000-3.0000 sec  3.88 MBytes  32.5 Mbits/sec
[  1] 3.0000-4.0000 sec  4.12 MBytes  34.6 Mbits/sec
[  1] 4.0000-5.0000 sec  4.00 MBytes  33.6 Mbits/sec
[  1] 5.0000-6.0000 sec  4.00 MBytes  33.6 Mbits/sec
[  1] 6.0000-7.0000 sec  4.00 MBytes  33.6 Mbits/sec
[  1] 7.0000-8.0000 sec  3.88 MBytes  32.5 Mbits/sec
[  1] 8.0000-9.0000 sec  4.00 MBytes  33.6 Mbits/sec
[  1] 9.0000-10.0000 sec  4.00 MBytes  33.6 Mbits/sec
[  1] 10.0000-11.0000 sec  4.00 MBytes  33.6 Mbits/sec
[  1] 11.0000-12.0000 sec  4.00 MBytes  33.6 Mbits/sec
[  1] 12.0000-13.0000 sec  3.88 MBytes  32.5 Mbits/sec
[  1] 13.0000-14.0000 sec  4.00 MBytes  33.6 Mbits/sec
[  1] 14.0000-15.0000 sec  4.00 MBytes  33.6 Mbits/sec
[  1] 15.0000-16.0000 sec  4.00 MBytes  33.6 Mbits/sec
[  1] 16.0000-17.0000 sec  4.00 MBytes  33.6 Mbits/sec
[  1] 17.0000-18.0000 sec  4.25 MBytes  35.7 Mbits/sec
[  1] 18.0000-19.0000 sec  3.88 MBytes  32.5 Mbits/sec
[  1] 19.0000-20.0000 sec  4.00 MBytes  33.6 Mbits/sec
[  1] 0.0000-20.1657 sec  80.4 MBytes  33.4 Mbits/sec
mininet> exit
*** Stopping 1 controllers
c0
*** Stopping 120 links
........................................................................................................................
*** Stopping 40 switches
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s27 s28 s29 s30 s31 s32 s33 s34 s35 s36 s37 s38 s39 s40
*** Stopping 81 hosts
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39 h40 h41 h42 h43 h44 h45 h46 h47 h48 h49 h50 h51 h52 h53 h54 h55 h56 h57 h58 h59 h60 h61 h62 h63 h64 h65 h66 h67 h68 h69 h70 h71 h72 h73 h74 h75 h76 h77 h78 h79 h80 h81
*** Done
completed in 649.678 seconds
```

25 Mbps

```bash
cplusplus@Galisse:~$ sudo mn --topo tree,depth=4,fanout=3 --mac --link tc,bw=25
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39 h40 h41 h42 h43 h44 h45 h46 h47 h48 h49 h50 h51 h52 h53 h54 h55 h56 h57 h58 h59 h60 h61 h62 h63 h64 h65 h66 h67 h68 h69 h70 h71 h72 h73 h74 h75 h76 h77 h78 h79 h80 h81
*** Adding switches:
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s27 s28 s29 s30 s31 s32 s33 s34 s35 s36 s37 s38 s39 s40
*** Adding links:
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s40, h81)
*** Configuring hosts
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39 h40 h41 h42 h43 h44 h45 h46 h47 h48 h49 h50 h51 h52 h53 h54 h55 h56 h57 h58 h59 h60 h61 h62 h63 h64 h65 h66 h67 h68 h69 h70 h71 h72 h73 h74 h75 h76 h77 h78 h79 h80 h81
*** Starting controller
c0
*** Starting 40 switches
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s27 s28 s29 s30 s31 s32 s33 s34 s35 s36 s37 s38 s39 s40 ...(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.

*** Starting CLI:
mininet> h1 ping -c 3 h81
PING 10.0.0.81 (10.0.0.81) 56(84) bytes of data.
From 10.0.0.1 icmp_seq=1 Destination Host Unreachable
From 10.0.0.1 icmp_seq=2 Destination Host Unreachable
From 10.0.0.1 icmp_seq=3 Destination Host Unreachable

--- 10.0.0.81 ping statistics ---
3 packets transmitted, 0 received, +3 errors, 100% packet loss, time 2029ms
pipe 3
mininet> h1 ping -c 3 h81
PING 10.0.0.81 (10.0.0.81) 56(84) bytes of data.
64 bytes from 10.0.0.81: icmp_seq=1 ttl=64 time=6.42 ms
64 bytes from 10.0.0.81: icmp_seq=2 ttl=64 time=1.73 ms
64 bytes from 10.0.0.81: icmp_seq=3 ttl=64 time=1.41 ms

--- 10.0.0.81 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2004ms
rtt min/avg/max/mdev = 1.413/3.186/6.418/2.288 ms
mininet> h1 iperf -s -p 5555 &
mininet> py h1.IP()
10.0.0.1
mininet> h2 iperf -c 10.0.0.1 -p 5555 -i 1 -t 20
------------------------------------------------------------
Client connecting to 10.0.0.1, TCP port 5555
TCP window size: 85.3 KByte (default)
------------------------------------------------------------
[  1] local 10.0.0.2 port 33610 connected with 10.0.0.1 port 5555 (icwnd/mss/irtt=14/1448/1055)
[ ID] Interval       Transfer     Bandwidth
[  1] 0.0000-1.0000 sec  4.25 MBytes  35.7 Mbits/sec
[  1] 1.0000-2.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 2.0000-3.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 3.0000-4.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 4.0000-5.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 5.0000-6.0000 sec  2.25 MBytes  18.9 Mbits/sec
[  1] 6.0000-7.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 7.0000-8.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 8.0000-9.0000 sec  2.88 MBytes  24.1 Mbits/sec
[  1] 9.0000-10.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 10.0000-11.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 11.0000-12.0000 sec  2.25 MBytes  18.9 Mbits/sec
[  1] 12.0000-13.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 13.0000-14.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 14.0000-15.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 15.0000-16.0000 sec  2.88 MBytes  24.1 Mbits/sec
[  1] 16.0000-17.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 17.0000-18.0000 sec  2.25 MBytes  18.9 Mbits/sec
[  1] 18.0000-19.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 19.0000-20.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 20.0000-20.6661 sec   128 KBytes  1.57 Mbits/sec
[  1] 0.0000-20.6661 sec  58.9 MBytes  23.9 Mbits/sec
mininet> exit
*** Stopping 1 controllers
c0
*** Stopping 120 links
........................................................................................................................
*** Stopping 40 switches
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s27 s28 s29 s30 s31 s32 s33 s34 s35 s36 s37 s38 s39 s40
*** Stopping 81 hosts
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39 h40 h41 h42 h43 h44 h45 h46 h47 h48 h49 h50 h51 h52 h53 h54 h55 h56 h57 h58 h59 h60 h61 h62 h63 h64 h65 h66 h67 h68 h69 h70 h71 h72 h73 h74 h75 h76 h77 h78 h79 h80 h81
*** Done
completed in 112.161 seconds
```

10 Mbps

```bash
cplusplus@Galisse:~$ sudo mn --topo tree,depth=4,fanout=3 --mac --link tc,bw=10
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39 h40 h41 h42 h43 h44 h45 h46 h47 h48 h49 h50 h51 h52 h53 h54 h55 h56 h57 h58 h59 h60 h61 h62 h63 h64 h65 h66 h67 h68 h69 h70 h71 h72 h73 h74 h75 h76 h77 h78 h79 h80 h81
*** Adding switches:
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s27 s28 s29 s30 s31 s32 s33 s34 s35 s36 s37 s38 s39 s40
*** Adding links:
(10.00Mbit) (10.00Mbit) (s1, s2) (10.00Mbit) (10.00Mbit) (s1, s15) (10.00Mbit) (10.00Mbit) (s1, s28) (10.00Mbit) (10.00Mbit) (s2, s3) (10.00Mbit) (10.00Mbit) (s2, s7) (10.00Mbit) (10.00Mbit) (s2, s11) (10.00Mbit) (10.00Mbit) (s3, s4) (10.00Mbit) (10.00Mbit) (s3, s5) (10.00Mbit) (10.00Mbit) (s3, s6) (10.00Mbit) (10.00Mbit) (s4, h1) (10.00Mbit) (10.00Mbit) (s4, h2) (10.00Mbit) (10.00Mbit) (s4, h3) (10.00Mbit) (10.00Mbit) (s5, h4) (10.00Mbit) (10.00Mbit) (s5, h5) (10.00Mbit) (10.00Mbit) (s5, h6) (10.00Mbit) (10.00Mbit) (s6, h7) (10.00Mbit) (10.00Mbit) (s6, h8) (10.00Mbit) (10.00Mbit) (s6, h9) (10.00Mbit) (10.00Mbit) (s7, s8) (10.00Mbit) (10.00Mbit) (s7, s9) (10.00Mbit) (10.00Mbit) (s7, s10) (10.00Mbit) (10.00Mbit) (s8, h10) (10.00Mbit) (10.00Mbit) (s8, h11) (10.00Mbit) (10.00Mbit) (s8, h12) (10.00Mbit) (10.00Mbit) (s9, h13) (10.00Mbit) (10.00Mbit) (s9, h14) (10.00Mbit) (10.00Mbit) (s9, h15) (10.00Mbit) (10.00Mbit) (s10, h16) (10.00Mbit) (10.00Mbit) (s10, h17) (10.00Mbit) (10.00Mbit) (s10, h18) (10.00Mbit) (10.00Mbit) (s11, s12) (10.00Mbit) (10.00Mbit) (s11, s13) (10.00Mbit) (10.00Mbit) (s11, s14) (10.00Mbit) (10.00Mbit) (s12, h19) (10.00Mbit) (10.00Mbit) (s12, h20) (10.00Mbit) (10.00Mbit) (s12, h21) (10.00Mbit) (10.00Mbit) (s13, h22) (10.00Mbit) (10.00Mbit) (s13, h23) (10.00Mbit) (10.00Mbit) (s13, h24) (10.00Mbit) (10.00Mbit) (s14, h25) (10.00Mbit) (10.00Mbit) (s14, h26) (10.00Mbit) (10.00Mbit) (s14, h27) (10.00Mbit) (10.00Mbit) (s15, s16) (10.00Mbit) (10.00Mbit) (s15, s20) (10.00Mbit) (10.00Mbit) (s15, s24) (10.00Mbit) (10.00Mbit) (s16, s17) (10.00Mbit) (10.00Mbit) (s16, s18) (10.00Mbit) (10.00Mbit) (s16, s19) (10.00Mbit) (10.00Mbit) (s17, h28) (10.00Mbit) (10.00Mbit) (s17, h29) (10.00Mbit) (10.00Mbit) (s17, h30) (10.00Mbit) (10.00Mbit) (s18, h31) (10.00Mbit) (10.00Mbit) (s18, h32) (10.00Mbit) (10.00Mbit) (s18, h33) (10.00Mbit) (10.00Mbit) (s19, h34) (10.00Mbit) (10.00Mbit) (s19, h35) (10.00Mbit) (10.00Mbit) (s19, h36) (10.00Mbit) (10.00Mbit) (s20, s21) (10.00Mbit) (10.00Mbit) (s20, s22) (10.00Mbit) (10.00Mbit) (s20, s23) (10.00Mbit) (10.00Mbit) (s21, h37) (10.00Mbit) (10.00Mbit) (s21, h38) (10.00Mbit) (10.00Mbit) (s21, h39) (10.00Mbit) (10.00Mbit) (s22, h40) (10.00Mbit) (10.00Mbit) (s22, h41) (10.00Mbit) (10.00Mbit) (s22, h42) (10.00Mbit) (10.00Mbit) (s23, h43) (10.00Mbit) (10.00Mbit) (s23, h44) (10.00Mbit) (10.00Mbit) (s23, h45) (10.00Mbit) (10.00Mbit) (s24, s25) (10.00Mbit) (10.00Mbit) (s24, s26) (10.00Mbit) (10.00Mbit) (s24, s27) (10.00Mbit) (10.00Mbit) (s25, h46) (10.00Mbit) (10.00Mbit) (s25, h47) (10.00Mbit) (10.00Mbit) (s25, h48) (10.00Mbit) (10.00Mbit) (s26, h49) (10.00Mbit) (10.00Mbit) (s26, h50) (10.00Mbit) (10.00Mbit) (s26, h51) (10.00Mbit) (10.00Mbit) (s27, h52) (10.00Mbit) (10.00Mbit) (s27, h53) (10.00Mbit) (10.00Mbit) (s27, h54) (10.00Mbit) (10.00Mbit) (s28, s29) (10.00Mbit) (10.00Mbit) (s28, s33) (10.00Mbit) (10.00Mbit) (s28, s37) (10.00Mbit) (10.00Mbit) (s29, s30) (10.00Mbit) (10.00Mbit) (s29, s31) (10.00Mbit) (10.00Mbit) (s29, s32) (10.00Mbit) (10.00Mbit) (s30, h55) (10.00Mbit) (10.00Mbit) (s30, h56) (10.00Mbit) (10.00Mbit) (s30, h57) (10.00Mbit) (10.00Mbit) (s31, h58) (10.00Mbit) (10.00Mbit) (s31, h59) (10.00Mbit) (10.00Mbit) (s31, h60) (10.00Mbit) (10.00Mbit) (s32, h61) (10.00Mbit) (10.00Mbit) (s32, h62) (10.00Mbit) (10.00Mbit) (s32, h63) (10.00Mbit) (10.00Mbit) (s33, s34) (10.00Mbit) (10.00Mbit) (s33, s35) (10.00Mbit) (10.00Mbit) (s33, s36) (10.00Mbit) (10.00Mbit) (s34, h64) (10.00Mbit) (10.00Mbit) (s34, h65) (10.00Mbit) (10.00Mbit) (s34, h66) (10.00Mbit) (10.00Mbit) (s35, h67) (10.00Mbit) (10.00Mbit) (s35, h68) (10.00Mbit) (10.00Mbit) (s35, h69) (10.00Mbit) (10.00Mbit) (s36, h70) (10.00Mbit) (10.00Mbit) (s36, h71) (10.00Mbit) (10.00Mbit) (s36, h72) (10.00Mbit) (10.00Mbit) (s37, s38) (10.00Mbit) (10.00Mbit) (s37, s39) (10.00Mbit) (10.00Mbit) (s37, s40) (10.00Mbit) (10.00Mbit) (s38, h73) (10.00Mbit) (10.00Mbit) (s38, h74) (10.00Mbit) (10.00Mbit) (s38, h75) (10.00Mbit) (10.00Mbit) (s39, h76) (10.00Mbit) (10.00Mbit) (s39, h77) (10.00Mbit) (10.00Mbit) (s39, h78) (10.00Mbit) (10.00Mbit) (s40, h79) (10.00Mbit) (10.00Mbit) (s40, h80) (10.00Mbit) (10.00Mbit) (s40, h81)
*** Configuring hosts
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39 h40 h41 h42 h43 h44 h45 h46 h47 h48 h49 h50 h51 h52 h53 h54 h55 h56 h57 h58 h59 h60 h61 h62 h63 h64 h65 h66 h67 h68 h69 h70 h71 h72 h73 h74 h75 h76 h77 h78 h79 h80 h81
*** Starting controller
c0
*** Starting 40 switches
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s27 s28 s29 s30 s31 s32 s33 s34 s35 s36 s37 s38 s39 s40 ...(10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit)
*** Starting CLI:
mininet> py h1.IP()
10.0.0.1
mininet> h1 iperf -s -p 5555 &
mininet> h2 iperf -c 10.0.0.1 -p 5555 -i 1 -t 20
------------------------------------------------------------
Client connecting to 10.0.0.1, TCP port 5555
TCP window size: 85.3 KByte (default)
------------------------------------------------------------
[  1] local 10.0.0.2 port 60952 connected with 10.0.0.1 port 5555 (icwnd/mss/irtt=14/1448/1556)
[ ID] Interval       Transfer     Bandwidth
[  1] 0.0000-1.0000 sec  3.38 MBytes  28.3 Mbits/sec
[  1] 1.0000-2.0000 sec  1.12 MBytes  9.42 Mbits/sec
[  1] 2.0000-3.0000 sec  1.18 MBytes  9.90 Mbits/sec
[  1] 3.0000-4.0000 sec  1.12 MBytes  9.38 Mbits/sec
[  1] 4.0000-5.0000 sec  1.18 MBytes  9.90 Mbits/sec
[  1] 5.0000-6.0000 sec  1.18 MBytes  9.90 Mbits/sec
[  1] 6.0000-7.0000 sec  1.18 MBytes  9.90 Mbits/sec
[  1] 7.0000-8.0000 sec  1.18 MBytes  9.90 Mbits/sec
[  1] 8.0000-9.0000 sec  1.12 MBytes  9.38 Mbits/sec
[  1] 9.0000-10.0000 sec  1.18 MBytes  9.90 Mbits/sec
[  1] 10.0000-11.0000 sec   636 KBytes  5.21 Mbits/sec
[  1] 11.0000-12.0000 sec  1.12 MBytes  9.38 Mbits/sec
[  1] 12.0000-13.0000 sec  1.18 MBytes  9.90 Mbits/sec
[  1] 13.0000-14.0000 sec  1.18 MBytes  9.90 Mbits/sec
[  1] 14.0000-15.0000 sec  1.18 MBytes  9.90 Mbits/sec
[  1] 15.0000-16.0000 sec  1.12 MBytes  9.38 Mbits/sec
[  1] 16.0000-17.0000 sec  1.18 MBytes  9.90 Mbits/sec
[  1] 17.0000-18.0000 sec  1.18 MBytes  9.90 Mbits/sec
[  1] 18.0000-19.0000 sec  1.18 MBytes  9.90 Mbits/sec
[  1] 19.0000-20.0000 sec  1.18 MBytes  9.90 Mbits/sec
[  1] 20.0000-21.8800 sec  60.7 KBytes   264 Kbits/sec
[  1] 0.0000-21.8800 sec  25.0 MBytes  9.59 Mbits/sec
mininet> exit
*** Stopping 1 controllers
c0
*** Stopping 120 links
........................................................................................................................
*** Stopping 40 switches
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s27 s28 s29 s30 s31 s32 s33 s34 s35 s36 s37 s38 s39 s40
*** Stopping 81 hosts
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39 h40 h41 h42 h43 h44 h45 h46 h47 h48 h49 h50 h51 h52 h53 h54 h55 h56 h57 h58 h59 h60 h61 h62 h63 h64 h65 h66 h67 h68 h69 h70 h71 h72 h73 h74 h75 h76 h77 h78 h79 h80 h81
*** Done
completed in 79.383 seconds
```

5 Mbps

```bash
cplusplus@Galisse:~$ sudo mn --topo tree,depth=4,fanout=3 --mac --link tc,bw=5
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39 h40 h41 h42 h43 h44 h45 h46 h47 h48 h49 h50 h51 h52 h53 h54 h55 h56 h57 h58 h59 h60 h61 h62 h63 h64 h65 h66 h67 h68 h69 h70 h71 h72 h73 h74 h75 h76 h77 h78 h79 h80 h81
*** Adding switches:
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s27 s28 s29 s30 s31 s32 s33 s34 s35 s36 s37 s38 s39 s40
*** Adding links:
(5.00Mbit) (5.00Mbit) (s1, s2) (5.00Mbit) (5.00Mbit) (s1, s15) (5.00Mbit) (5.00Mbit) (s1, s28) (5.00Mbit) (5.00Mbit) (s2, s3) (5.00Mbit) (5.00Mbit) (s2, s7) (5.00Mbit) (5.00Mbit) (s2, s11) (5.00Mbit) (5.00Mbit) (s3, s4) (5.00Mbit) (5.00Mbit) (s3, s5) (5.00Mbit) (5.00Mbit) (s3, s6) (5.00Mbit) (5.00Mbit) (s4, h1) (5.00Mbit) (5.00Mbit) (s4, h2) (5.00Mbit) (5.00Mbit) (s4, h3) (5.00Mbit) (5.00Mbit) (s5, h4) (5.00Mbit) (5.00Mbit) (s5, h5) (5.00Mbit) (5.00Mbit) (s5, h6) (5.00Mbit) (5.00Mbit) (s6, h7) (5.00Mbit) (5.00Mbit) (s6, h8) (5.00Mbit) (5.00Mbit) (s6, h9) (5.00Mbit) (5.00Mbit) (s7, s8) (5.00Mbit) (5.00Mbit) (s7, s9) (5.00Mbit) (5.00Mbit) (s7, s10) (5.00Mbit) (5.00Mbit) (s8, h10) (5.00Mbit) (5.00Mbit) (s8, h11) (5.00Mbit) (5.00Mbit) (s8, h12) (5.00Mbit) (5.00Mbit) (s9, h13) (5.00Mbit) (5.00Mbit) (s9, h14) (5.00Mbit) (5.00Mbit) (s9, h15) (5.00Mbit) (5.00Mbit) (s10, h16) (5.00Mbit) (5.00Mbit) (s10, h17) (5.00Mbit) (5.00Mbit) (s10, h18) (5.00Mbit) (5.00Mbit) (s11, s12) (5.00Mbit) (5.00Mbit) (s11, s13) (5.00Mbit) (5.00Mbit) (s11, s14) (5.00Mbit) (5.00Mbit) (s12, h19) (5.00Mbit) (5.00Mbit) (s12, h20) (5.00Mbit) (5.00Mbit) (s12, h21) (5.00Mbit) (5.00Mbit) (s13, h22) (5.00Mbit) (5.00Mbit) (s13, h23) (5.00Mbit) (5.00Mbit) (s13, h24) (5.00Mbit) (5.00Mbit) (s14, h25) (5.00Mbit) (5.00Mbit) (s14, h26) (5.00Mbit) (5.00Mbit) (s14, h27) (5.00Mbit) (5.00Mbit) (s15, s16) (5.00Mbit) (5.00Mbit) (s15, s20) (5.00Mbit) (5.00Mbit) (s15, s24) (5.00Mbit) (5.00Mbit) (s16, s17) (5.00Mbit) (5.00Mbit) (s16, s18) (5.00Mbit) (5.00Mbit) (s16, s19) (5.00Mbit) (5.00Mbit) (s17, h28) (5.00Mbit) (5.00Mbit) (s17, h29) (5.00Mbit) (5.00Mbit) (s17, h30) (5.00Mbit) (5.00Mbit) (s18, h31) (5.00Mbit) (5.00Mbit) (s18, h32) (5.00Mbit) (5.00Mbit) (s18, h33) (5.00Mbit) (5.00Mbit) (s19, h34) (5.00Mbit) (5.00Mbit) (s19, h35) (5.00Mbit) (5.00Mbit) (s19, h36) (5.00Mbit) (5.00Mbit) (s20, s21) (5.00Mbit) (5.00Mbit) (s20, s22) (5.00Mbit) (5.00Mbit) (s20, s23) (5.00Mbit) (5.00Mbit) (s21, h37) (5.00Mbit) (5.00Mbit) (s21, h38) (5.00Mbit) (5.00Mbit) (s21, h39) (5.00Mbit) (5.00Mbit) (s22, h40) (5.00Mbit) (5.00Mbit) (s22, h41) (5.00Mbit) (5.00Mbit) (s22, h42) (5.00Mbit) (5.00Mbit) (s23, h43) (5.00Mbit) (5.00Mbit) (s23, h44) (5.00Mbit) (5.00Mbit) (s23, h45) (5.00Mbit) (5.00Mbit) (s24, s25) (5.00Mbit) (5.00Mbit) (s24, s26) (5.00Mbit) (5.00Mbit) (s24, s27) (5.00Mbit) (5.00Mbit) (s25, h46) (5.00Mbit) (5.00Mbit) (s25, h47) (5.00Mbit) (5.00Mbit) (s25, h48) (5.00Mbit) (5.00Mbit) (s26, h49) (5.00Mbit) (5.00Mbit) (s26, h50) (5.00Mbit) (5.00Mbit) (s26, h51) (5.00Mbit) (5.00Mbit) (s27, h52) (5.00Mbit) (5.00Mbit) (s27, h53) (5.00Mbit) (5.00Mbit) (s27, h54) (5.00Mbit) (5.00Mbit) (s28, s29) (5.00Mbit) (5.00Mbit) (s28, s33) (5.00Mbit) (5.00Mbit) (s28, s37) (5.00Mbit) (5.00Mbit) (s29, s30) (5.00Mbit) (5.00Mbit) (s29, s31) (5.00Mbit) (5.00Mbit) (s29, s32) (5.00Mbit) (5.00Mbit) (s30, h55) (5.00Mbit) (5.00Mbit) (s30, h56) (5.00Mbit) (5.00Mbit) (s30, h57) (5.00Mbit) (5.00Mbit) (s31, h58) (5.00Mbit) (5.00Mbit) (s31, h59) (5.00Mbit) (5.00Mbit) (s31, h60) (5.00Mbit) (5.00Mbit) (s32, h61) (5.00Mbit) (5.00Mbit) (s32, h62) (5.00Mbit) (5.00Mbit) (s32, h63) (5.00Mbit) (5.00Mbit) (s33, s34) (5.00Mbit) (5.00Mbit) (s33, s35) (5.00Mbit) (5.00Mbit) (s33, s36) (5.00Mbit) (5.00Mbit) (s34, h64) (5.00Mbit) (5.00Mbit) (s34, h65) (5.00Mbit) (5.00Mbit) (s34, h66) (5.00Mbit) (5.00Mbit) (s35, h67) (5.00Mbit) (5.00Mbit) (s35, h68) (5.00Mbit) (5.00Mbit) (s35, h69) (5.00Mbit) (5.00Mbit) (s36, h70) (5.00Mbit) (5.00Mbit) (s36, h71) (5.00Mbit) (5.00Mbit) (s36, h72) (5.00Mbit) (5.00Mbit) (s37, s38) (5.00Mbit) (5.00Mbit) (s37, s39) (5.00Mbit) (5.00Mbit) (s37, s40) (5.00Mbit) (5.00Mbit) (s38, h73) (5.00Mbit) (5.00Mbit) (s38, h74) (5.00Mbit) (5.00Mbit) (s38, h75) (5.00Mbit) (5.00Mbit) (s39, h76) (5.00Mbit) (5.00Mbit) (s39, h77) (5.00Mbit) (5.00Mbit) (s39, h78) (5.00Mbit) (5.00Mbit) (s40, h79) (5.00Mbit) (5.00Mbit) (s40, h80) (5.00Mbit) (5.00Mbit) (s40, h81)
*** Configuring hosts
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39 h40 h41 h42 h43 h44 h45 h46 h47 h48 h49 h50 h51 h52 h53 h54 h55 h56 h57 h58 h59 h60 h61 h62 h63 h64 h65 h66 h67 h68 h69 h70 h71 h72 h73 h74 h75 h76 h77 h78 h79 h80 h81
*** Starting controller
c0
*** Starting 40 switches
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s27 s28 s29 s30 s31 s32 s33 s34 s35 s36 s37 s38 s39 s40 ...(5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit)
*** Starting CLI:
mininet> h1 iperf -s -p 5555 &
mininet> h2 iperf -c 10.0.0.1 -p 5555 -i 1 -t 20
------------------------------------------------------------
Client connecting to 10.0.0.1, TCP port 5555
TCP window size: 85.3 KByte (default)
------------------------------------------------------------
[  1] local 10.0.0.2 port 44796 connected with 10.0.0.1 port 5555 (icwnd/mss/irtt=14/1448/2339)
[ ID] Interval       Transfer     Bandwidth
[  1] 0.0000-1.0000 sec  2.88 MBytes  24.1 Mbits/sec
[  1] 1.0000-2.0000 sec   580 KBytes  4.75 Mbits/sec
[  1] 2.0000-3.0000 sec   636 KBytes  5.21 Mbits/sec
[  1] 3.0000-4.0000 sec   573 KBytes  4.69 Mbits/sec
[  1] 4.0000-5.0000 sec   508 KBytes  4.16 Mbits/sec
[  1] 5.0000-6.0000 sec   701 KBytes  5.74 Mbits/sec
[  1] 6.0000-7.0000 sec   573 KBytes  4.69 Mbits/sec
[  1] 7.0000-8.0000 sec   508 KBytes  4.16 Mbits/sec
[  1] 8.0000-9.0000 sec   701 KBytes  5.74 Mbits/sec
[  1] 9.0000-10.0000 sec   508 KBytes  4.16 Mbits/sec
[  1] 10.0000-11.0000 sec   701 KBytes  5.74 Mbits/sec
[  1] 11.0000-12.0000 sec   573 KBytes  4.69 Mbits/sec
[  1] 12.0000-13.0000 sec   318 KBytes  2.61 Mbits/sec
[  1] 13.0000-14.0000 sec   573 KBytes  4.69 Mbits/sec
[  1] 14.0000-15.0000 sec   636 KBytes  5.21 Mbits/sec
[  1] 15.0000-16.0000 sec   573 KBytes  4.69 Mbits/sec
[  1] 16.0000-17.0000 sec   508 KBytes  4.16 Mbits/sec
[  1] 17.0000-18.0000 sec   701 KBytes  5.74 Mbits/sec
[  1] 18.0000-19.0000 sec   573 KBytes  4.69 Mbits/sec
[  1] 19.0000-20.0000 sec   636 KBytes  5.21 Mbits/sec
[  1] 20.0000-25.0234 sec  62.2 KBytes   101 Kbits/sec
[  1] 0.0000-25.0234 sec  13.8 MBytes  4.61 Mbits/sec
```

## 2. Topologia Customizada

### 2.1. Criação da Topologia Customizada

Para a topologia customizada, foi criado um arquivo Python `topology.py`:

Comando de execução:

```bash
cplusplus@Galisse:~$ sudo python3 topology.py
*** Creating network
*** Adding hosts:
h1 h2 h3 h4 h5 h6
*** Adding switches:
s1 s2 s3 s4
*** Adding links:
(h1, s1) (h2, s1) (h3, s2) (h4, s3) (h5, s4) (h6, s4) (s1, s2) (s1, s3) (s2, s4) (s3, s4)
*** Configuring hosts
h1 h2 h3 h4 h5 h6
*** Starting controller

*** Starting 4 switches
s1 s2 s3 s4 ...
*** Starting CLI:
mininet> pingall
*** Ping: testing ping reachability
h1 -> h2 h3 h4 h5 h6
h2 -> h1 h3 h4 h5 h6
h3 -> h1 h2 h4 h5 h6
h4 -> h1 h2 h3 h5 h6
h5 -> h1 h2 h3 h4 h6
h6 -> h1 h2 h3 h4 h5
*** Results: 0% dropped (30/30 received)
```

* 4 switches (s1-s4), 6 hosts (h1-h6), com ligações personalizadas.

### 2.2. Desenho Ilustrativo da Topologia Customizada

Foi usado o script `draw_mininet_tree2.py` para visualizar a topologia customizada, resultando em:

![Topologia customizada](Figure_2.png)

### 2.3. Inspeção da Rede

Comandos utilizados:

```bash
mininet> nodes
available nodes are:
h1 h2 h3 h4 h5 h6 s1 s2 s3 s4
mininet> net
h1 h1-eth0:s1-eth1
h2 h2-eth0:s1-eth2
h3 h3-eth0:s2-eth1
h4 h4-eth0:s3-eth1
h5 h5-eth0:s4-eth1
h6 h6-eth0:s4-eth2
s1 lo:  s1-eth1:h1-eth0 s1-eth2:h2-eth0 s1-eth3:s2-eth2 s1-eth4:s3-eth2
s2 lo:  s2-eth1:h3-eth0 s2-eth2:s1-eth3 s2-eth3:s4-eth3
s3 lo:  s3-eth1:h4-eth0 s3-eth2:s1-eth4 s3-eth3:s4-eth4
s4 lo:  s4-eth1:h5-eth0 s4-eth2:h6-eth0 s4-eth3:s2-eth3 s4-eth4:s3-eth3
mininet> dump
<Host h1: h1-eth0:10.0.0.1 pid=36291>
<Host h2: h2-eth0:10.0.0.2 pid=36293>
<Host h3: h3-eth0:10.0.0.3 pid=36295>
<Host h4: h4-eth0:10.0.0.4 pid=36297>
<Host h5: h5-eth0:10.0.0.5 pid=36299>
<Host h6: h6-eth0:10.0.0.6 pid=36301>
<OVSSwitch s1: lo:127.0.0.1,s1-eth1:None,s1-eth2:None,s1-eth3:None,s1-eth4:None pid=36306>
<OVSSwitch s2: lo:127.0.0.1,s2-eth1:None,s2-eth2:None,s2-eth3:None pid=36309>
<OVSSwitch s3: lo:127.0.0.1,s3-eth1:None,s3-eth2:None,s3-eth3:None pid=36312>
<OVSSwitch s4: lo:127.0.0.1,s4-eth1:None,s4-eth2:None,s4-eth3:None,s4-eth4:None pid=36315>
mininet> h1 ifconfig
h1-eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.0.1  netmask 255.0.0.0  broadcast 10.255.255.255
        inet6 fe80::200:ff:fe00:1  prefixlen 64  scopeid 0x20<link>
        ether 00:00:00:00:00:01  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

mininet> h1 ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: h1-eth0@if2017: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 00:00:00:00:00:01 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.0.0.1/8 brd 10.255.255.255 scope global h1-eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::200:ff:fe00:1/64 scope link
       valid_lft forever preferred_lft forever
mininet> h1 ping -c 1 h2
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=29.8 ms

--- 10.0.0.2 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 29.768/29.768/29.768/0.000 ms
```

**Confirmação:**
Os comandos mostram as conexões corretas entre hosts e switches, e entre os próprios switches.

### 2.4. Teste de Conectividade

O comando `pingall` indicou comunicação parcial, devido a remoção de algumas regras no switch

```bash
cplusplus@Galisse:~$ sudo ovs-ofctl del-flows s1
cplusplus@Galisse:~$ sudo ovs-ofctl add-flow s1 "in_port=1,actions=output:2"
cplusplus@Galisse:~$ sudo ovs-ofctl add-flow s1 "in_port=2,actions=output:1"
```

```bash
mininet> pingall
*** Ping: testing ping reachability
h1 -> h2 X X X X
h2 -> h1 X X X X
h3 -> X X h4 h5 h6
h4 -> X X h3 h5 h6
h5 -> X X h3 h4 h6
h6 -> X X h3 h4 h5
*** Results: 53% dropped (14/30 received)
```
