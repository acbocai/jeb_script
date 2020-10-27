# -*- coding: utf-8 -*-
from com.pnfsoftware.jeb.client.api import IClientContext
from com.pnfsoftware.jeb.core import IRuntimeProject
from com.pnfsoftware.jeb.core.units import IUnit
from com.pnfsoftware.jeb.core.units.code.android import IDexUnit
from com.pnfsoftware.jeb.core.units.code.android.controlflow import BasicBlock
from com.pnfsoftware.jeb.core.units.code.android.dex import IDexMethodData, IDexCodeItem, IDalvikInstruction, IDexMethod


# 访问基本块
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

    # 指令序列
    print("-------------------------------------")
    for idx,insn in enumerate(dexCodeItem.getInstructions()):
        assert isinstance(insn,IDalvikInstruction)
        print(idx,hex(insn.getOffset()),insn.getMnemonic())

    # 控制流图
    print("-------------------------------------")
    cfg = dexCodeItem.getControlFlowGraph()
    print(cfg)

    # 基本块信息
    print("-------------------------------------")
    blockList = cfg.getBlocks()
    for block in blockList:
        assert isinstance(block,BasicBlock)
        print "01 getFirstAddress           >>> ", hex(block.getFirstAddress())      # 入口指令偏移
        print "02 getEndAddress             >>> ", hex(block.getEndAddress())        # 出口指令偏移
        print "03 getLast                   >>> ", block.getLast()                   # 最后一条指令
        print "04 getLastAddress            >>> ", hex(block.getLastAddress())       # 最后一条指令偏移
        print "05 size                      >>> ", block.size()                      # 指令条数
        print "06 getInstructions           >>> ", block.getInstructions()           # 指令序列

        print "07 allinsize                 >>> ", block.allinsize()                 # 前驱个数
        print "08 insize                    >>> ", block.insize()                    # 规则前驱个数
        print "09 irrinsize                 >>> ", block.irrinsize()                 # 不规则前驱个数

        print "10 alloutsize                >>> ", block.alloutsize()                # 后继个数
        print "11 outsize                   >>> ", block.outsize()                   # 规则后继个数
        print "12 irroutsize                >>> ", block.irroutsize()                # 不规则后继个数

        print "13 getAllInputBlocks         >>> ", block.getAllInputBlocks()         # 所有前驱块
        print "14 getInputBlocks            >>> ", block.getInputBlocks()            # 常规前驱块
        print "15 getIrregularInputBlocks   >>> ", block.getIrregularInputBlocks()   # 不规则前驱块

        print "16 getAllOutputBlocks        >>> ", block.getAllOutputBlocks()        # 所有后继块
        print "17 getOutputBlocks           >>> ", block.getOutputBlocks()           # 常规后继块
        print "18 getIrregularOutputBlocks  >>> ", block.getIrregularOutputBlocks()  # 不规则后继块

        print block.getAddress()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# 输出
# -------------------------------------
# (0, '0x0L', u'check-cast')
# (1, '0x4L', u'check-cast')
# (2, '0x8L', u'iget')
# (3, '0xcL', u'iget')
# (4, '0x10L', u'if-ge')
# (5, '0x14L', u'const/4')
# (6, '0x16L', u'return')
# (7, '0x18L', u'iget')
# (8, '0x1cL', u'iget')
# (9, '0x20L', u'if-le')
# (10, '0x24L', u'const/4')
# (11, '0x26L', u'goto')
# (12, '0x28L', u'const/4')
# (13, '0x2aL', u'goto')
# -------------------------------------
# CFG(6): (0-10,5), (14-14,1), (16-16,1), (18-20,3), (24-26,2), (28-2A,2)
# -------------------------------------
# 01 getFirstAddress           >>>  0x0L
# 02 getEndAddress             >>>  0x14L
# 03 getLast                   >>>  if-ge
# 04 getLastAddress            >>>  0x10L
# 05 size                      >>>  5
# 06 getInstructions           >>>  [check-cast, check-cast, iget, iget, if-ge]
# 07 allinsize                 >>>  0
# 08 insize                    >>>  0
# 09 irrinsize                 >>>  0
# 10 alloutsize                >>>  2
# 11 outsize                   >>>  2
# 12 irroutsize                >>>  0
# 13 getAllInputBlocks         >>>  []
# 14 getInputBlocks            >>>  []
# 15 getIrregularInputBlocks   >>>  []
# 16 getAllOutputBlocks        >>>  [(14-14,1), (18-20,3)]
# 17 getOutputBlocks           >>>  [(14-14,1), (18-20,3)]
# 18 getIrregularOutputBlocks  >>>  []
# 0
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 01 getFirstAddress           >>>  0x14L
# 02 getEndAddress             >>>  0x16L
# 03 getLast                   >>>  const/4
# 04 getLastAddress            >>>  0x14L
# 05 size                      >>>  1
# 06 getInstructions           >>>  [const/4]
# 07 allinsize                 >>>  1
# 08 insize                    >>>  1
# 09 irrinsize                 >>>  0
# 10 alloutsize                >>>  1
# 11 outsize                   >>>  1
# 12 irroutsize                >>>  0
# 13 getAllInputBlocks         >>>  [(0-10,5)]
# 14 getInputBlocks            >>>  [(0-10,5)]
# 15 getIrregularInputBlocks   >>>  []
# 16 getAllOutputBlocks        >>>  [(16-16,1)]
# 17 getOutputBlocks           >>>  [(16-16,1)]
# 18 getIrregularOutputBlocks  >>>  []
# 20
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 01 getFirstAddress           >>>  0x16L
# 02 getEndAddress             >>>  0x18L
# 03 getLast                   >>>  return
# 04 getLastAddress            >>>  0x16L
# 05 size                      >>>  1
# 06 getInstructions           >>>  [return]
# 07 allinsize                 >>>  3
# 08 insize                    >>>  3
# 09 irrinsize                 >>>  0
# 10 alloutsize                >>>  0
# 11 outsize                   >>>  0
# 12 irroutsize                >>>  0
# 13 getAllInputBlocks         >>>  [(28-2A,2), (24-26,2), (14-14,1)]
# 14 getInputBlocks            >>>  [(28-2A,2), (24-26,2), (14-14,1)]
# 15 getIrregularInputBlocks   >>>  []
# 16 getAllOutputBlocks        >>>  []
# 17 getOutputBlocks           >>>  []
# 18 getIrregularOutputBlocks  >>>  []
# 22
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 01 getFirstAddress           >>>  0x18L
# 02 getEndAddress             >>>  0x24L
# 03 getLast                   >>>  if-le
# 04 getLastAddress            >>>  0x20L
# 05 size                      >>>  3
# 06 getInstructions           >>>  [iget, iget, if-le]
# 07 allinsize                 >>>  1
# 08 insize                    >>>  1
# 09 irrinsize                 >>>  0
# 10 alloutsize                >>>  2
# 11 outsize                   >>>  2
# 12 irroutsize                >>>  0
# 13 getAllInputBlocks         >>>  [(0-10,5)]
# 14 getInputBlocks            >>>  [(0-10,5)]
# 15 getIrregularInputBlocks   >>>  []
# 16 getAllOutputBlocks        >>>  [(24-26,2), (28-2A,2)]
# 17 getOutputBlocks           >>>  [(24-26,2), (28-2A,2)]
# 18 getIrregularOutputBlocks  >>>  []
# 24
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 01 getFirstAddress           >>>  0x24L
# 02 getEndAddress             >>>  0x28L
# 03 getLast                   >>>  goto
# 04 getLastAddress            >>>  0x26L
# 05 size                      >>>  2
# 06 getInstructions           >>>  [const/4, goto]
# 07 allinsize                 >>>  1
# 08 insize                    >>>  1
# 09 irrinsize                 >>>  0
# 10 alloutsize                >>>  1
# 11 outsize                   >>>  1
# 12 irroutsize                >>>  0
# 13 getAllInputBlocks         >>>  [(18-20,3)]
# 14 getInputBlocks            >>>  [(18-20,3)]
# 15 getIrregularInputBlocks   >>>  []
# 16 getAllOutputBlocks        >>>  [(16-16,1)]
# 17 getOutputBlocks           >>>  [(16-16,1)]
# 18 getIrregularOutputBlocks  >>>  []
# 36
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 01 getFirstAddress           >>>  0x28L
# 02 getEndAddress             >>>  0x2cL
# 03 getLast                   >>>  goto
# 04 getLastAddress            >>>  0x2aL
# 05 size                      >>>  2
# 06 getInstructions           >>>  [const/4, goto]
# 07 allinsize                 >>>  1
# 08 insize                    >>>  1
# 09 irrinsize                 >>>  0
# 10 alloutsize                >>>  1
# 11 outsize                   >>>  1
# 12 irroutsize                >>>  0
# 13 getAllInputBlocks         >>>  [(18-20,3)]
# 14 getInputBlocks            >>>  [(18-20,3)]
# 15 getIrregularInputBlocks   >>>  []
# 16 getAllOutputBlocks        >>>  [(16-16,1)]
# 17 getOutputBlocks           >>>  [(16-16,1)]
# 18 getIrregularOutputBlocks  >>>  []
# 40
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Done.        



# 方法指令
# .method public final volatile bridge synthetic compare(Object, Object)I
#           .registers 5
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