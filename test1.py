from pprint import pprint
from jnpr.junos import Device
from jnpr.junos.op.fpc import FpcHwTable
from jnpr.junos.op.fpc import FpcInfoTable
from jnpr.junos.op.xcvr import XcvrTable


dev = Device(host='192.168.0.5', user='deshar', password='9miraihe')
dev.open()

print('test message')
fpcs = FpcHwTable(dev)
fpcs.get()

#print(fpcs)
#pprint(fpcs.keys())
#pprint(fpcs.values())
#for fpc in fpcs:
#         print (fpc.key," Description:", fpc.desc, "Model:", fpc.model,"Serial:", fpc.sn, "Part-number:", fpc.pn)

#print(dev.cli("show chassis hardware"))
#inv = dev.rpc.get_chassis_inventory()
#print("model: %s" % inv.findtext('chassis/description'))
#print("serial-number: %s" %inv.findtext('chassis/serial-number'))

xcvr_db = XcvrTable(dev)
xcvr_db.get()
pprint(xcvr_db.values())
pprint(xcvr_db.items())

dev.close()