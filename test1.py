from pprint import pprint
from jnpr.junos import Device
from jnpr.junos.op.fpc import FpcHwTable
from jnpr.junos.op.fpc import FpcMiReHwTable
from jnpr.junos.op.xcvr import XcvrTable

dev = Device(host='192.168.0.5', user='deshar', password='9miraihe')
dev.open()

fpcs = FpcHwTable(dev)
fpcs.get()
mics = FpcMiReHwTable(dev)
mics.get()
xcvrs = XcvrTable(dev)
xcvrs.get()

print(fpcs)
pprint(fpcs.keys())
pprint(fpcs.values())
for fpc in fpcs:
         print (fpc.key," Description:", fpc.desc, "Model:", fpc.model,"Serial:", fpc.sn, "Part-number:", fpc.pn)
pprint(mics)
pprint(mics.keys())
pprint(mics.values())
pprint(xcvrs)
pprint(xcvrs.keys())
pprint(xcvrs.values())

dev.close()