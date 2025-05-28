**Relatório de Exercício Mininet: Topologia Linear e Testes de Desempenho**

  * **Data:** 15 de maio de 2025
  * **Ambiente:** Mininet executado via WSL2 no Windows 11

**1. Criação da Topologia de Rede**

**1.1. Comando de Criação**
A topologia de rede foi criada utilizando o seguinte comando no terminal Mininet:

```bash
sudo mn --topo linear,6 --mac --link tc,bw=25
```
![topologia](https://github.com/user-attachments/assets/69451bec-d2ad-4e38-8c41-4e2027bc1863)

**1.2. Descrição da Topologia**

  * `--topo linear,6`: Especifica uma topologia linear composta por 6 switches (s1 a s6). Por padrão, cada switch em uma topologia linear no Mininet tem um host conectado a ele (h1 a h6).
      * h1 conectado a s1
      * h2 conectado a s2
      * ...
      * h6 conectado a s6
      * E os switches conectados em sequência: s1-s2, s2-s3, s3-s4, s4-s5, s5-s6.
  * Controlador: Foi utilizado o controlador padrão do Mininet (`OVSController`), que opera em `127.0.0.1:6653`, pois nenhum controlador específico (`--controller`) foi definido no comando.

**1.3. Configuração de Endereços MAC**

  * `--mac`: Esta opção foi utilizada para garantir que os endereços MAC dos hosts fossem definidos de forma simples e sequencial (ex: h1 com MAC `00:00:00:00:00:01`, h2 com `00:00:00:00:00:02`, e assim por diante). As interfaces dos switches também recebem endereços MAC automaticamente.

**1.4. Configuração de Largura de Banda**

  * `--link tc,bw=25`: Configura todos os links da topologia (entre hosts e switches, e entre switches) para terem uma largura de banda de 25 Mbps, utilizando o `tc` (Traffic Control) do Linux.

**1.5. Observações Durante a Criação**
Durante a criação dos links, foram observadas as seguintes mensagens de erro/aviso repetidamente:

```
*** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
```

Esses avisos são emitidos pelo Hierarchical Token Bucket (`htb`) do `tc`. Eles geralmente indicam que o "quantum" (uma unidade de dados que uma classe pode retirar do buffer) pode ser muito grande em relação à taxa configurada, especialmente para taxas de bits mais baixas ou dependendo da configuração do kernel. Embora apareçam como erros, geralmente não impedem o funcionamento da limitação de banda, mas podem introduzir pequenas imprecisões.

**2. Inspeção de Informações da Rede**

Após a criação da topologia, os seguintes comandos foram utilizados para inspecionar a rede:

**2.1. Listagem de Nós**
Comando:

```bash
mininet> nodes
```

Saída:

```
available nodes are:
c0 h1 h2 h3 h4 h5 h6 s1 s2 s3 s4 s5 s6
```

Isso confirma a presença do controlador `c0`, 6 hosts (`h1` a `h6`) e 6 switches (`s1` a `s6`).

**2.2. Listagem Detalhada dos Nós (Dump)**
Comando:

```bash
mininet> dump
```

Saída:

```
<Host h1: h1-eth0:10.0.0.1 pid=13617>
<Host h2: h2-eth0:10.0.0.2 pid=13619>
<Host h3: h3-eth0:10.0.0.3 pid=13621>
<Host h4: h4-eth0:10.0.0.4 pid=13623>
<Host h5: h5-eth0:10.0.0.5 pid=13625>
<Host h6: h6-eth0:10.0.0.6 pid=13627>
<OVSSwitch s1: lo:127.0.0.1,s1-eth1:None,s1-eth2:None pid=13632>
<OVSSwitch s2: lo:127.0.0.1,s2-eth1:None,s2-eth2:None,s2-eth3:None pid=13635>
<OVSSwitch s3: lo:127.0.0.1,s3-eth1:None,s3-eth2:None,s3-eth3:None pid=13638>
<OVSSwitch s4: lo:127.0.0.1,s4-eth1:None,s4-eth2:None,s4-eth3:None pid=13641>
<OVSSwitch s5: lo:127.0.0.1,s5-eth1:None,s5-eth2:None,s5-eth3:None pid=13644>
<OVSSwitch s6: lo:127.0.0.1,s6-eth1:None,s6-eth2:None pid=13647>
<OVSController c0: 127.0.0.1:6653 pid=13610>
```

Esta saída confirma os endereços IP atribuídos aos hosts e as interfaces dos switches.

**2.3. Listagem de Interfaces**
Comando:

```bash
mininet> intfs
```

Saída:

```
h1: h1-eth0
h2: h2-eth0
h3: h3-eth0
h4: h4-eth0
h5: h5-eth0
h6: h6-eth0
s1: lo,s1-eth1,s1-eth2
s2: lo,s2-eth1,s2-eth2,s2-eth3
s3: lo,s3-eth1,s3-eth2,s3-eth3
s4: lo,s4-eth1,s4-eth2,s4-eth3
s5: lo,s5-eth1,s5-eth2,s5-eth3
s6: lo,s6-eth1,s6-eth2
c0:
```

Lista todas as interfaces de rede criadas para os hosts e switches.

**2.4. Verificação de Conexões (Rede)**
Comando:

```bash
mininet> net
```

Saída:

```
h1 h1-eth0:s1-eth1
h2 h2-eth0:s2-eth1
h3 h3-eth0:s3-eth1
h4 h4-eth0:s4-eth1
h5 h5-eth0:s5-eth1
h6 h6-eth0:s6-eth1
s1 lo:  s1-eth1:h1-eth0 s1-eth2:s2-eth2
s2 lo:  s2-eth1:h2-eth0 s2-eth2:s1-eth2 s2-eth3:s3-eth2
s3 lo:  s3-eth1:h3-eth0 s3-eth2:s2-eth3 s3-eth3:s4-eth2
s4 lo:  s4-eth1:h4-eth0 s4-eth2:s3-eth3 s4-eth3:s5-eth2
s5 lo:  s5-eth1:h5-eth0 s5-eth2:s4-eth3 s5-eth3:s6-eth2
s6 lo:  s6-eth1:h6-eth0 s6-eth2:s5-eth3
c0
```

Detalha as conexões entre as interfaces dos hosts e as portas (interfaces) dos switches, confirmando a topologia linear.

**2.5. Informações do Host h1 (IP, MAC)**

  * Comando `h1 ifconfig`:
    ```
    mininet> h1 ifconfig
    h1-eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            inet 10.0.0.1  netmask 255.0.0.0  broadcast 10.255.255.255
            ether 00:00:00:00:00:01  txqueuelen 1000  (Ethernet)
            ...
    lo: ...
    ```
  * Comando `h1 ip addr`:
    ```
    mininet> h1 ip addr
    2: h1-eth0@if7: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc htb state UP group default qlen 1000
        link/ether 00:00:00:00:00:01 brd ff:ff:ff:ff:ff:ff link-netnsid 0
        inet 10.0.0.1/8 brd 10.255.255.255 scope global h1-eth0
           valid_lft forever preferred_lft forever
        ...
    ```
    Ambos os comandos confirmam:
      * **IP de h1:** `10.0.0.1`
      * **MAC de h1-eth0:** `00:00:00:00:00:01`

**2.6. Informações do Switch s1 (Interfaces, MACs)**

  * Comando `s1 ifconfig` (saída relevante para interfaces do switch s1):

    ```
    mininet> s1 ifconfig
    s1-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            ether 82:6f:36:ca:c0:61  txqueuelen 1000  (Ethernet)
            ...
    s1-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            ether fa:69:49:04:88:06  txqueuelen 1000  (Ethernet)
            ...
    lo: ...
    (Nota: A interface `eth0` com IP `172.25.134.146` que aparece na saída completa do `s1 ifconfig` é provavelmente a interface de rede do WSL2 herdada no namespace, não uma porta Mininet do switch s1 para a topologia interna.)
    ```

    MACs das interfaces do switch `s1` envolvidas na topologia:

      * **MAC de s1-eth1:** `82:6f:36:ca:c0:61` (conectada a h1-eth0)
      * **MAC de s1-eth2:** `fa:69:49:04:88:06` (conectada a s2-eth2)

**2.7. Conectividade Geral**
Comando:

```bash
mininet> pingall
```

Saída:

```
*** Ping: testing ping reachability
h1 -> h2 h3 h4 h5 h6
h2 -> h1 h3 h4 h5 h6
h3 -> h1 h2 h4 h5 h6
h4 -> h1 h2 h3 h5 h6
h5 -> h1 h2 h3 h4 h6
h6 -> h1 h2 h3 h4 h5
*** Results: 0% dropped (30/30 received)
```

Confirma que todos os hosts conseguem se comunicar entre si.

**3. Teste de Desempenho com iperf (TCP)**

**3.1. Configuração do Servidor TCP (h1)**

  * Obtenção do IP do Servidor (h1):
    ```bash
    mininet> py h1.IP()
    10.0.0.1
    ```
  * Comando para iniciar o servidor `iperf` no `h1` na porta 5555:
    ```bash
    mininet> h1 iperf -s -p 5555 &
    ```
  * Confirmação (saída parcial do servidor `iperf` no `h1` após conexão do cliente):
    ```
    ------------------------------------------------------------
    Server listening on TCP port 5555
    TCP window size: 85.3 KByte (default)
    ------------------------------------------------------------
    [  1] local 10.0.0.1 port 5555 connected with 10.0.0.2 port 42054 (icwnd/mss/irtt=14/1448/3201)
    ```

**3.2. Configuração do Cliente (h2) e Execução do Teste**

  * Comando para iniciar o cliente `iperf` no `h2`, conectando-se a `h1` (10.0.0.1) na porta 5555, com relatório a cada 1 segundo por 15 segundos:
    ```bash
    mininet> h2 iperf -c 10.0.0.1 -p 5555 -i 1 -t 15
    ```
  * Resultados Detalhados do `iperf` (saída no cliente `h2`):
    ```
    ------------------------------------------------------------
    Client connecting to 10.0.0.1, TCP port 5555
    TCP window size: 85.3 KByte (default)
    ------------------------------------------------------------
    [  1] local 10.0.0.2 port 44638 connected with 10.0.0.1 port 5555 (icwnd/mss/irtt=14/1448/2838)
    [ ID] Interval       Transfer     Bandwidth
    [  1] 0.0000-1.0000 sec  3.88 MBytes  32.5 Mbits/sec
    [  1] 1.0000-2.0000 sec  3.00 MBytes  25.2 Mbits/sec
    [  1] 2.0000-3.0000 sec  2.62 MBytes  22.0 Mbits/sec
    [  1] 3.0000-4.0000 sec  3.00 MBytes  25.2 Mbits/sec
    [  1] 4.0000-5.0000 sec  2.62 MBytes  22.0 Mbits/sec
    [  1] 5.0000-6.0000 sec  3.12 MBytes  26.2 Mbits/sec
    [  1] 6.0000-7.0000 sec  2.50 MBytes  21.0 Mbits/sec
    [  1] 7.0000-8.0000 sec  3.12 MBytes  26.2 Mbits/sec
    [  1] 8.0000-9.0000 sec  2.62 MBytes  22.0 Mbits/sec
    [  1] 9.0000-10.0000 sec  3.00 MBytes  25.2 Mbits/sec
    [  1] 10.0000-11.0000 sec  3.00 MBytes  25.2 Mbits/sec
    [  1] 11.0000-12.0000 sec  2.62 MBytes  22.0 Mbits/sec
    [  1] 12.0000-13.0000 sec  3.12 MBytes  26.2 Mbits/sec
    [  1] 13.0000-14.0000 sec  2.62 MBytes  22.0 Mbits/sec
    [  1] 14.0000-15.0000 sec  3.00 MBytes  25.2 Mbits/sec
    [  1] 15.0000-15.4478 sec   128 KBytes  2.34 Mbits/sec
    [  1] 0.0000-15.4478 sec  44.0 MBytes  23.9 Mbits/sec
    ```
  * Resultado do Servidor `iperf`:
    ```
    [ ID] Interval        Transfer     Bandwidth
    [  1] 0.0000-15.4478 sec  44.0 MBytes  23.9 Mbits/sec
    ```

**3.3. Análise dos Resultados do iperf**
A largura de banda configurada nos links foi de 25 Mbps. O teste `iperf` entre `h1` e `h2` (que estão conectados através de `s1` e `s2`, atravessando o link `s1-s2`, o link `h1-s1` e `h2-s2`, todos com 25 Mbps) mostrou uma largura de banda média de **23.9 Mbits/sec**.
Este valor é próximo do limite configurado de 25 Mbps, com a diferença sendo atribuível ao overhead dos protocolos (TCP/IP, Ethernet) e possivelmente às pequenas imprecisões do `tc` (conforme os avisos `sch_htb`).
Os relatórios por segundo mostram uma variação na taxa de transferência, o que é normal para TCP, mas geralmente orbitando o limite da banda.

**3.4. Verificação e Encerramento do Processo do Servidor iperf**

  * Verificando o processo `iperf` no `h1`:
    ```bash
    mininet> h1 ps -ef | grep iperf
    root       13984   13617  0 20:09 pts/4    00:00:00 iperf -s -p 5555
    root       13997   13617  0 20:10 pts/4    00:00:00 grep iperf
    ```
  * Encerrando o shell do host `h1` (e consequentemente o processo `iperf` filho):
    ```bash
    mininet> h1 kill 13617
    ```
    Isso efetivamente encerrou o servidor `iperf` ao terminar o shell do nó `h1` onde o servidor `iperf` estava sendo executado.

```bash
cplusplus@Galisse:~$ sudo mn --topo linear,6 --mac --link tc,bw=25
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2 h3 h4 h5 h6
*** Adding switches:
s1 s2 s3 s4 s5 s6
*** Adding links:
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(h1, s1) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(h2, s2) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(h3, s3) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(h4, s4) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(h5, s5) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(h6, s6) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s2, s1) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s3, s2) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s4, s3) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s5, s4) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s6, s5)
*** Configuring hosts
h1 h2 h3 h4 h5 h6
*** Starting controller
c0
*** Starting 6 switches
s1 s2 s3 s4 s5 s6 ...(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.

*** Starting CLI:
mininet> nodes
available nodes are:
c0 h1 h2 h3 h4 h5 h6 s1 s2 s3 s4 s5 s6
mininet> dump
<Host h1: h1-eth0:10.0.0.1 pid=13617>
<Host h2: h2-eth0:10.0.0.2 pid=13619>
<Host h3: h3-eth0:10.0.0.3 pid=13621>
<Host h4: h4-eth0:10.0.0.4 pid=13623>
<Host h5: h5-eth0:10.0.0.5 pid=13625>
<Host h6: h6-eth0:10.0.0.6 pid=13627>
<OVSSwitch s1: lo:127.0.0.1,s1-eth1:None,s1-eth2:None pid=13632>
<OVSSwitch s2: lo:127.0.0.1,s2-eth1:None,s2-eth2:None,s2-eth3:None pid=13635>
<OVSSwitch s3: lo:127.0.0.1,s3-eth1:None,s3-eth2:None,s3-eth3:None pid=13638>
<OVSSwitch s4: lo:127.0.0.1,s4-eth1:None,s4-eth2:None,s4-eth3:None pid=13641>
<OVSSwitch s5: lo:127.0.0.1,s5-eth1:None,s5-eth2:None,s5-eth3:None pid=13644>
<OVSSwitch s6: lo:127.0.0.1,s6-eth1:None,s6-eth2:None pid=13647>
<OVSController c0: 127.0.0.1:6653 pid=13610>
mininet> intfs
h1: h1-eth0
h2: h2-eth0
h3: h3-eth0
h4: h4-eth0
h5: h5-eth0
h6: h6-eth0
s1: lo,s1-eth1,s1-eth2
s2: lo,s2-eth1,s2-eth2,s2-eth3
s3: lo,s3-eth1,s3-eth2,s3-eth3
s4: lo,s4-eth1,s4-eth2,s4-eth3
s5: lo,s5-eth1,s5-eth2,s5-eth3
s6: lo,s6-eth1,s6-eth2
c0:
mininet> net
h1 h1-eth0:s1-eth1
h2 h2-eth0:s2-eth1
h3 h3-eth0:s3-eth1
h4 h4-eth0:s4-eth1
h5 h5-eth0:s5-eth1
h6 h6-eth0:s6-eth1
s1 lo:  s1-eth1:h1-eth0 s1-eth2:s2-eth2
s2 lo:  s2-eth1:h2-eth0 s2-eth2:s1-eth2 s2-eth3:s3-eth2
s3 lo:  s3-eth1:h3-eth0 s3-eth2:s2-eth3 s3-eth3:s4-eth2
s4 lo:  s4-eth1:h4-eth0 s4-eth2:s3-eth3 s4-eth3:s5-eth2
s5 lo:  s5-eth1:h5-eth0 s5-eth2:s4-eth3 s5-eth3:s6-eth2
s6 lo:  s6-eth1:h6-eth0 s6-eth2:s5-eth3
c0
mininet> h1 ifconfig
h1-eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.0.1  netmask 255.0.0.0  broadcast 10.255.255.255
        inet6 fe80::200:ff:fe00:1  prefixlen 64  scopeid 0x20<link>
        ether 00:00:00:00:00:01  txqueuelen 1000  (Ethernet)
        RX packets 108  bytes 8456 (8.4 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 12  bytes 996 (996.0 B)
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
2: h1-eth0@if7: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc htb state UP group default qlen 1000
    link/ether 00:00:00:00:00:01 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.0.0.1/8 brd 10.255.255.255 scope global h1-eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::200:ff:fe00:1/64 scope link
       valid_lft forever preferred_lft forever
mininet> h1 arp -n
mininet> s1 ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1382
        inet 172.25.134.146  netmask 255.255.240.0  broadcast 172.25.143.255
        inet6 fe80::215:5dff:fede:5978  prefixlen 64  scopeid 0x20<link>
        ether 00:15:5d:de:59:78  txqueuelen 1000  (Ethernet)
        RX packets 33039  bytes 35899028 (35.8 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 5997  bytes 446174 (446.1 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 3306  bytes 364209 (364.2 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 3306  bytes 364209 (364.2 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s1-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::806f:36ff:feca:c061  prefixlen 64  scopeid 0x20<link>
        ether 82:6f:36:ca:c0:61  txqueuelen 1000  (Ethernet)
        RX packets 13  bytes 1066 (1.0 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 108  bytes 8456 (8.4 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s1-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::f869:49ff:fe04:8806  prefixlen 64  scopeid 0x20<link>
        ether fa:69:49:04:88:06  txqueuelen 1000  (Ethernet)
        RX packets 96  bytes 7500 (7.5 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 22  bytes 1716 (1.7 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s2-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::80f4:b5ff:fe5d:ee28  prefixlen 64  scopeid 0x20<link>
        ether 82:f4:b5:5d:ee:28  txqueuelen 1000  (Ethernet)
        RX packets 13  bytes 1086 (1.0 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 110  bytes 8596 (8.5 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s2-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::ecbc:28ff:fe87:c0de  prefixlen 64  scopeid 0x20<link>
        ether ee:bc:28:87:c0:de  txqueuelen 1000  (Ethernet)
        RX packets 22  bytes 1716 (1.7 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 96  bytes 7500 (7.5 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s2-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::6018:f3ff:fec4:12d  prefixlen 64  scopeid 0x20<link>
        ether 62:18:f3:c4:01:2d  txqueuelen 1000  (Ethernet)
        RX packets 79  bytes 6190 (6.1 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 41  bytes 3202 (3.2 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s3-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::804c:d7ff:fec7:ddf0  prefixlen 64  scopeid 0x20<link>
        ether 82:4c:d7:c7:dd:f0  txqueuelen 1000  (Ethernet)
        RX packets 12  bytes 996 (996.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 110  bytes 8596 (8.5 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s3-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::8430:8bff:fe97:4ec8  prefixlen 64  scopeid 0x20<link>
        ether 86:30:8b:97:4e:c8  txqueuelen 1000  (Ethernet)
        RX packets 41  bytes 3202 (3.2 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 79  bytes 6190 (6.1 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s3-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::20ac:dbff:fe7c:75a7  prefixlen 64  scopeid 0x20<link>
        ether 22:ac:db:7c:75:a7  txqueuelen 1000  (Ethernet)
        RX packets 60  bytes 4704 (4.7 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 61  bytes 4774 (4.7 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s4-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::5467:21ff:fe0b:efda  prefixlen 64  scopeid 0x20<link>
        ether 56:67:21:0b:ef:da  txqueuelen 1000  (Ethernet)
        RX packets 12  bytes 996 (996.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 112  bytes 8772 (8.7 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s4-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::2088:f8ff:fef1:d3d3  prefixlen 64  scopeid 0x20<link>
        ether 22:88:f8:f1:d3:d3  txqueuelen 1000  (Ethernet)
        RX packets 61  bytes 4774 (4.7 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 60  bytes 4704 (4.7 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s4-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::2072:1aff:fe13:dcba  prefixlen 64  scopeid 0x20<link>
        ether 22:72:1a:13:dc:ba  txqueuelen 1000  (Ethernet)
        RX packets 41  bytes 3218 (3.2 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 81  bytes 6346 (6.3 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s5-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::a415:adff:fe35:773b  prefixlen 64  scopeid 0x20<link>
        ether a6:15:ad:35:77:3b  txqueuelen 1000  (Ethernet)
        RX packets 12  bytes 996 (996.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 112  bytes 8784 (8.7 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s5-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::8c33:4ff:fe6d:9ad7  prefixlen 64  scopeid 0x20<link>
        ether 8e:33:04:6d:9a:d7  txqueuelen 1000  (Ethernet)
        RX packets 81  bytes 6346 (6.3 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 41  bytes 3218 (3.2 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s5-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::b8e5:4eff:fe74:a1be  prefixlen 64  scopeid 0x20<link>
        ether ba:e5:4e:74:a1:be  txqueuelen 1000  (Ethernet)
        RX packets 21  bytes 1662 (1.6 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 100  bytes 7832 (7.8 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s6-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::6c8c:d1ff:fe64:a527  prefixlen 64  scopeid 0x20<link>
        ether 6e:8c:d1:64:a5:27  txqueuelen 1000  (Ethernet)
        RX packets 13  bytes 1082 (1.0 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 111  bytes 8698 (8.6 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s6-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::d0d7:96ff:fed1:d50c  prefixlen 64  scopeid 0x20<link>
        ether d2:d7:96:d1:d5:0c  txqueuelen 1000  (Ethernet)
        RX packets 100  bytes 7832 (7.8 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 21  bytes 1662 (1.6 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

mininet> s1 ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet 10.255.255.254/32 brd 10.255.255.254 scope global lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1382 qdisc mq state UP group default qlen 1000
    link/ether 00:15:5d:de:59:78 brd ff:ff:ff:ff:ff:ff
    inet 172.25.134.146/20 brd 172.25.143.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::215:5dff:fede:5978/64 scope link
       valid_lft forever preferred_lft forever
7: s1-eth1@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc htb master ovs-system state UP group default qlen 1000
    link/ether 82:6f:36:ca:c0:61 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet6 fe80::806f:36ff:feca:c061/64 scope link
       valid_lft forever preferred_lft forever
8: s2-eth1@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc htb master ovs-system state UP group default qlen 1000
    link/ether 82:f4:b5:5d:ee:28 brd ff:ff:ff:ff:ff:ff link-netnsid 1
    inet6 fe80::80f4:b5ff:fe5d:ee28/64 scope link
       valid_lft forever preferred_lft forever
9: s3-eth1@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc htb master ovs-system state UP group default qlen 1000
    link/ether 82:4c:d7:c7:dd:f0 brd ff:ff:ff:ff:ff:ff link-netnsid 2
    inet6 fe80::804c:d7ff:fec7:ddf0/64 scope link
       valid_lft forever preferred_lft forever
10: s4-eth1@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc htb master ovs-system state UP group default qlen 1000
    link/ether 56:67:21:0b:ef:da brd ff:ff:ff:ff:ff:ff link-netnsid 3
    inet6 fe80::5467:21ff:fe0b:efda/64 scope link
       valid_lft forever preferred_lft forever
11: s5-eth1@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc htb master ovs-system state UP group default qlen 1000
    link/ether a6:15:ad:35:77:3b brd ff:ff:ff:ff:ff:ff link-netnsid 4
    inet6 fe80::a415:adff:fe35:773b/64 scope link
       valid_lft forever preferred_lft forever
12: s6-eth1@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc htb master ovs-system state UP group default qlen 1000
    link/ether 6e:8c:d1:64:a5:27 brd ff:ff:ff:ff:ff:ff link-netnsid 5
    inet6 fe80::6c8c:d1ff:fe64:a527/64 scope link
       valid_lft forever preferred_lft forever
13: s1-eth2@s2-eth2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc htb master ovs-system state UP group default qlen 1000
    link/ether fa:69:49:04:88:06 brd ff:ff:ff:ff:ff:ff
    inet6 fe80::f869:49ff:fe04:8806/64 scope link
       valid_lft forever preferred_lft forever
14: s2-eth2@s1-eth2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc htb master ovs-system state UP group default qlen 1000
    link/ether ee:bc:28:87:c0:de brd ff:ff:ff:ff:ff:ff
    inet6 fe80::ecbc:28ff:fe87:c0de/64 scope link
       valid_lft forever preferred_lft forever
15: s2-eth3@s3-eth2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc htb master ovs-system state UP group default qlen 1000
    link/ether 62:18:f3:c4:01:2d brd ff:ff:ff:ff:ff:ff
    inet6 fe80::6018:f3ff:fec4:12d/64 scope link
       valid_lft forever preferred_lft forever
16: s3-eth2@s2-eth3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc htb master ovs-system state UP group default qlen 1000
    link/ether 86:30:8b:97:4e:c8 brd ff:ff:ff:ff:ff:ff
    inet6 fe80::8430:8bff:fe97:4ec8/64 scope link
       valid_lft forever preferred_lft forever
17: s3-eth3@s4-eth2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc htb master ovs-system state UP group default qlen 1000
    link/ether 22:ac:db:7c:75:a7 brd ff:ff:ff:ff:ff:ff
    inet6 fe80::20ac:dbff:fe7c:75a7/64 scope link
       valid_lft forever preferred_lft forever
18: s4-eth2@s3-eth3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc htb master ovs-system state UP group default qlen 1000
    link/ether 22:88:f8:f1:d3:d3 brd ff:ff:ff:ff:ff:ff
    inet6 fe80::2088:f8ff:fef1:d3d3/64 scope link
       valid_lft forever preferred_lft forever
19: s4-eth3@s5-eth2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc htb master ovs-system state UP group default qlen 1000
    link/ether 22:72:1a:13:dc:ba brd ff:ff:ff:ff:ff:ff
    inet6 fe80::2072:1aff:fe13:dcba/64 scope link
       valid_lft forever preferred_lft forever
20: s5-eth2@s4-eth3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc htb master ovs-system state UP group default qlen 1000
    link/ether 8e:33:04:6d:9a:d7 brd ff:ff:ff:ff:ff:ff
    inet6 fe80::8c33:4ff:fe6d:9ad7/64 scope link
       valid_lft forever preferred_lft forever
21: s5-eth3@s6-eth2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc htb master ovs-system state UP group default qlen 1000
    link/ether ba:e5:4e:74:a1:be brd ff:ff:ff:ff:ff:ff
    inet6 fe80::b8e5:4eff:fe74:a1be/64 scope link
       valid_lft forever preferred_lft forever
22: s6-eth2@s5-eth3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc htb master ovs-system state UP group default qlen 1000
    link/ether d2:d7:96:d1:d5:0c brd ff:ff:ff:ff:ff:ff
    inet6 fe80::d0d7:96ff:fed1:d50c/64 scope link
       valid_lft forever preferred_lft forever
23: ovs-system: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether 22:a9:12:5c:1a:f6 brd ff:ff:ff:ff:ff:ff
24: s1: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether 1a:27:f9:6f:3a:43 brd ff:ff:ff:ff:ff:ff
25: s4: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether 4a:c4:54:88:02:42 brd ff:ff:ff:ff:ff:ff
26: s6: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether 1e:4f:65:3c:88:49 brd ff:ff:ff:ff:ff:ff
27: s3: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether 8a:dc:cd:77:33:4a brd ff:ff:ff:ff:ff:ff
28: s5: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether d2:bb:a1:a3:ae:45 brd ff:ff:ff:ff:ff:ff
29: s2: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether 46:b0:0b:f5:8d:48 brd ff:ff:ff:ff:ff:ff
mininet> pingall
*** Ping: testing ping reachability
h1 -> h2 h3 h4 h5 h6
h2 -> h1 h3 h4 h5 h6
h3 -> h1 h2 h4 h5 h6
h4 -> h1 h2 h3 h5 h6
h5 -> h1 h2 h3 h4 h6
h6 -> h1 h2 h3 h4 h5
*** Results: 0% dropped (30/30 received)
mininet> py h1.IP()
10.0.0.1
mininet> h1 iperf -s -p 5555 &
mininet> h2 iperf -c 10.0.0.1 -p 5555 -i 1 -t 15
------------------------------------------------------------
Client connecting to 10.0.0.1, TCP port 5555
TCP window size: 85.3 KByte (default)
------------------------------------------------------------
[  1] local 10.0.0.2 port 44638 connected with 10.0.0.1 port 5555 (icwnd/mss/irtt=14/1448/2838)
[ ID] Interval       Transfer     Bandwidth
[  1] 0.0000-1.0000 sec  3.88 MBytes  32.5 Mbits/sec
[  1] 1.0000-2.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 2.0000-3.0000 sec  2.62 MBytes  22.0 Mbits/sec
[  1] 3.0000-4.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 4.0000-5.0000 sec  2.62 MBytes  22.0 Mbits/sec
[  1] 5.0000-6.0000 sec  3.12 MBytes  26.2 Mbits/sec
[  1] 6.0000-7.0000 sec  2.50 MBytes  21.0 Mbits/sec
[  1] 7.0000-8.0000 sec  3.12 MBytes  26.2 Mbits/sec
[  1] 8.0000-9.0000 sec  2.62 MBytes  22.0 Mbits/sec
[  1] 9.0000-10.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 10.0000-11.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 11.0000-12.0000 sec  2.62 MBytes  22.0 Mbits/sec
[  1] 12.0000-13.0000 sec  3.12 MBytes  26.2 Mbits/sec
[  1] 13.0000-14.0000 sec  2.62 MBytes  22.0 Mbits/sec
[  1] 14.0000-15.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 15.0000-15.4478 sec   128 KBytes  2.34 Mbits/sec
[  1] 0.0000-15.4478 sec  44.0 MBytes  23.9 Mbits/sec
```
