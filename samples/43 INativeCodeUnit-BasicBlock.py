# -*- coding: utf-8 -*-
from com.pnfsoftware.jeb.client.api import IClientContext
from com.pnfsoftware.jeb.core import IRuntimeProject
from com.pnfsoftware.jeb.core.units import IUnit, INativeCodeUnit
from com.pnfsoftware.jeb.core.units.code.asm.cfg import BasicBlock
from com.pnfsoftware.jeb.core.units.code.asm.items import INativeMethodItem


# 基本块信息
def Test(ctx):
    assert isinstance(ctx,IClientContext)
    input_path = r"D:\tmp\2\project\about_dex_diff\code\xmly\libFace3D.so"
    unit = ctx.open(input_path);                                    assert isinstance(unit,IUnit)
    prj = ctx.getMainProject();                                     assert isinstance(prj,IRuntimeProject)
    nativeCodeUnit = prj.findUnit(INativeCodeUnit);                 assert isinstance(nativeCodeUnit,INativeCodeUnit)
    bool = nativeCodeUnit.process()

    # method
    method = nativeCodeUnit.getMethod("sub_11110");                 assert isinstance(method,INativeMethodItem)

    # block
    nativeMethodDataItem = method.getData()
    if nativeMethodDataItem is not None:
        cfg = nativeMethodDataItem.getCFG()
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

            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


'''
01 getFirstAddress           >>>  0x11110L
02 getEndAddress             >>>  0x1111aL
03 getLast                   >>>  (80B1) CBZ R0, 24h
04 getLastAddress            >>>  0x11118L
05 size                      >>>  5
06 getInstructions           >>>  [(D0B5) PUSH {R4, R6, R7, LR}, (02AF) ADD R7, SP, #8, (0446) MOV R4, R0, (406A) LDR R0, [R0, #24h], (80B1) CBZ R0, 24h]
07 allinsize                 >>>  0
08 insize                    >>>  0
09 irrinsize                 >>>  0
10 alloutsize                >>>  2
11 outsize                   >>>  2
12 irroutsize                >>>  0
13 getAllInputBlocks         >>>  []
14 getInputBlocks            >>>  []
15 getIrregularInputBlocks   >>>  []
16 getAllOutputBlocks        >>>  [1113Ch(6), 1111Ah(2)]
17 getOutputBlocks           >>>  [1113Ch(6), 1111Ah(2)]
18 getIrregularOutputBlocks  >>>  []
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
01 getFirstAddress           >>>  0x1111aL
02 getEndAddress             >>>  0x11120L
03 getLast                   >>>  (BFF35B8F) DMB ISH
04 getLastAddress            >>>  0x1111cL
05 size                      >>>  2
06 getInstructions           >>>  [(0C30) ADDS R0, #0Ch, (BFF35B8F) DMB ISH]
07 allinsize                 >>>  1
08 insize                    >>>  1
09 irrinsize                 >>>  0
10 alloutsize                >>>  1
11 outsize                   >>>  1
12 irroutsize                >>>  0
13 getAllInputBlocks         >>>  [11110h(5)]
14 getInputBlocks            >>>  [11110h(5)]
15 getIrregularInputBlocks   >>>  []
16 getAllOutputBlocks        >>>  [11120h(5)]
17 getOutputBlocks           >>>  [11120h(5)]
18 getIrregularOutputBlocks  >>>  []
......

'''