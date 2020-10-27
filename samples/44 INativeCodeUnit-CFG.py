# -*- coding: utf-8 -*-
from com.pnfsoftware.jeb.client.api import IClientContext
from com.pnfsoftware.jeb.core import IRuntimeProject
from com.pnfsoftware.jeb.core.units import IUnit, INativeCodeUnit
from com.pnfsoftware.jeb.core.units.code.asm.cfg import BasicBlock
from com.pnfsoftware.jeb.core.units.code.asm.items import INativeMethodItem

# CFG信息
def Test(ctx):
    assert isinstance(ctx,IClientContext)
    input_path = r"D:\tmp\2\project\about_dex_diff\code\xmly\libFace3D.so"
    unit = ctx.open(input_path);                                    assert isinstance(unit,IUnit)
    prj = ctx.getMainProject();                                     assert isinstance(prj,IRuntimeProject)
    nativeCodeUnit = prj.findUnit(INativeCodeUnit);                 assert isinstance(nativeCodeUnit,INativeCodeUnit)
    bool = nativeCodeUnit.process()

    # method
    method = nativeCodeUnit.getMethod("sub_11110");                 assert isinstance(method,INativeMethodItem)

    # CFG
    nativeMethodDataItem = method.getData()
    if nativeMethodDataItem is not None:
        cfg = nativeMethodDataItem.getCFG()
        print "01 Block               >>> ",cfg.getBlocks()             # 基本快列表
        print "02 size                >>> ",cfg.size()                  # 块个数
        print "03 hasExit             >>> ",cfg.hasExit()               # 是否有出口
        print "04 getEntryBlock       >>> ",cfg.getEntryBlock()         # 入口块
        print "05 getExitBlocks       >>> ",cfg.getExitBlocks()         # 出口块(不唯一)
        print "07 getAddressBlockMap  >>> ",cfg.getAddressBlockMap()    # map<偏移地址,块>
        print "08 getEndAddress       >>> ",hex(cfg.getEndAddress())    # 结尾指令地址
        print "09 doDataFlowAnalysis  >>> ",cfg.doDataFlowAnalysis()    # 执行数据流分析


'''
输出:
01 Block               >>>  [11110h(5), 1111Ah(2), 11120h(5), 1112Eh(5), 1113Ch(6), 1114Ch(3), 11154h(3), 1115Ah(1)] 02 size                >>>  8
03 hasExit             >>>  True
04 getEntryBlock       >>>  11110h(5)
05 getExitBlocks       >>>  [1115Ah(1)]
07 getAddressBlockMap  >>>  {69904L: 11110h(5), 69920L: 11120h(5), 69972L: 11154h(3), 69914L: 1111Ah(2), 69978L: 1115Ah(1), 69948L: 1113Ch(6), 69964L: 1114Ch(3), 69934L: 1112Eh(5)}
08 getEndAddress       >>>  0x1115cL
09 doDataFlowAnalysis  >>>  None
Done.
'''