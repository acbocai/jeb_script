# -*- coding: utf-8 -*-
from com.pnfsoftware.jeb.client.api import IClientContext
from com.pnfsoftware.jeb.core import IRuntimeProject
from com.pnfsoftware.jeb.core.units import IUnit
from com.pnfsoftware.jeb.core.units.code.android import IDexUnit
from com.pnfsoftware.jeb.core.units.code.android.dex import IDexMethodData, IDexCodeItem, IDexMethod

# 访问CFG
def Test(ctx):
    assert isinstance(ctx,IClientContext)
    input_path = r"D:\tmp\2\project\about_dex_diff\code\jsq\jsq.dex"
    sign = "Lnet/cavas/show/aa;->compare(Ljava/lang/Object;Ljava/lang/Object;)I"
    unit = ctx.open(input_path);                                    assert isinstance(unit,IUnit)
    prj = ctx.getMainProject();                                     assert isinstance(prj,IRuntimeProject)
    dexUnit = prj.findUnit(IDexUnit);                               assert isinstance(dexUnit,IDexUnit);
    method = dexUnit.getMethod(sign);                               assert isinstance(method,IDexMethod)
    dexMethodData = method.getData();                               assert isinstance(dexMethodData,IDexMethodData)
    dexCodeItem= dexMethodData.getCodeItem();                       assert isinstance(dexCodeItem,IDexCodeItem)

    # 控制流图
    print("-------------------------------------")
    cfg = dexCodeItem.getControlFlowGraph()
    print "01 Block               >>> ",cfg.getBlocks()             # 基本快列表
    print "02 size                >>> ",cfg.size()                  # 块个数
    print "03 hasExit             >>> ",cfg.hasExit()               # 是否有出口
    print "04 getEntryBlock       >>> ",cfg.getEntryBlock()         # 入口块
    print "05 getExitBlocks       >>> ",cfg.getExitBlocks()         # 出口块(不唯一)
    print "06 getLast             >>> ",cfg.getLast()               # 最后一个块
    print "07 getAddressBlockMap  >>> ",cfg.getAddressBlockMap()    # map<偏移地址,块>
    print "08 getEndAddress       >>> ",hex(cfg.getEndAddress())    # 结尾指令地址
    print "09 formatEdges         >>> ",cfg.formatEdges()           # 输出边(字符串)

    # print " >>> ",cfg.doDataFlowAnalysis()    # 执行数据流分析
    # print " >>> ",cfg.getUseDefChains()       # UD
    # print " >>> ",cfg.getDefUseChains()       # DU
    # print " >>> ",cfg.getFullDefUseChains()   # FDU
    # print " >>> ",cfg.getFullUseDefChains()   # FUD


# 输出
# 01 Block               >>>  [(0-10,5), (14-14,1), (16-16,1), (18-20,3), (24-26,2), (28-2A,2)]
# 02 size                >>>  6
# 03 hasExit             >>>  True
# 04 getEntryBlock       >>>  (0-10,5)
# 05 getExitBlocks       >>>  [(16-16,1)]
# 06 getLast             >>>  (28-2A,2)
# 07 getAddressBlockMap  >>>  {0L: (0-10,5), 20L: (14-14,1), 22L: (16-16,1), 24L: (18-20,3), 36L: (24-26,2), 40L: (28-2A,2)}
# 08 getEndAddress       >>>  0x2cL
# 09 formatEdges         >>>    (EDGES: 0->14, 0->18, 14->16, 18->24, 18->28, 24->16, 28->16)
# Done.


# 方法指令
# .method public final volatile bridge synthetic compare(Object, Object)I
# .registers 5
# 00000000  check-cast          p1, b
# 00000004  check-cast          p2, b
# 00000008  iget                v0, p1, b->o:I
# 0000000C  iget                v1, p2, b->o:I
# 00000010  if-ge               v0, v1, :18
# :14
# 00000014  const/4             v0, 1
# :16
# 00000016  return              v0
# :18
# 00000018  iget                v0, p1, b->o:I
# 0000001C  iget                v1, p2, b->o:I
# 00000020  if-le               v0, v1, :28  # 1111111111
# :24
# 00000024  const/4             v0, -1
# 00000026  goto                :16
# :28
# 00000028  const/4             v0, 0
# 0000002A  goto                :16
# .end method