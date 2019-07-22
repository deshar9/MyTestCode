from pprint import pprint
from jnpr.junos import Device
from jnpr.junos.op.fpc import FpcHwTable
from jnpr.junos.op.fpc import FpcInfoTable

dev = Device(host='192.168.0.5', user='deshar', password='9miraihe')
dev.open()

fpcs = FpcHwTable(dev)
fpcs.get()
jfpcs = FpcInfoTable(dev)
jfpcs.get()


print(fpcs)
pprint(fpcs.keys())
pprint(fpcs.values())
for fpc in fpcs:
         print (fpc.key," Description:", fpc.desc, "Model:", fpc.model,"Serial:", fpc.sn, "Part-number:", fpc.pn)
pprint(jfpcs)
pprint(jfpcs.keys())
pprint(jfpcs.values())


dev.close()