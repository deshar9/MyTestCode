
from jnpr.junos import Device
from jnpr.junos.op.fpc import FpcHwTable
#from jnpr.junos.op.fpc import FpcMiReHwTable

dev = Device(host='192.168.0.5', user='deshar', password='9miraihe')
dev.open()

fpcs = FpcHwTable(dev)
fpcs.get()
print(fpcs)

for fpc in fpcs:
         print (fpc.key," Description:", fpc.desc, "Model:", fpc.model,"Serial:", fpc.sn, "Part-number:", fpc.pn)


dev.close()