# -*- coding: utf-8 -*-
from com.pnfsoftware.jeb.client.api import IClientContext
from com.pnfsoftware.jeb.core import IRuntimeProject
from com.pnfsoftware.jeb.core.units import IUnit, INativeCodeUnit
from com.pnfsoftware.jeb.core.units.code import IInstruction
from com.pnfsoftware.jeb.core.units.code.asm.items import INativeMethodItem

# 指令信息
def Test(ctx):
    assert isinstance(ctx,IClientContext)
    input_path = r"D:\tmp\2\project\about_dex_diff\code\xmly\libFace3D.so"
    unit = ctx.open(input_path);                                    assert isinstance(unit,IUnit)
    prj = ctx.getMainProject();                                     assert isinstance(prj,IRuntimeProject)
    nativeCodeUnit = prj.findUnit(INativeCodeUnit);                 assert isinstance(nativeCodeUnit,INativeCodeUnit)
    bool = nativeCodeUnit.process()

    # method
    method = nativeCodeUnit.getMethod("sub_11110");                 assert isinstance(method,INativeMethodItem)

    # insn
    insnlist = method.getInstructions()
    for insn in insnlist:
        assert isinstance(insn,IInstruction)
        print " >>> ",insn.getMnemonic()
        print " >>> ",insn.getProcessorMode()
        print " >>> ",insn.getSize()
        print " >>> ",insn.getCode()
        print " >>> ",insn.getPrefix()
        print " >>> ",insn.getMnemonic()
        print " >>> ",insn.getOperands()
        print " >>> ",insn.canThrow()
        print " >>> ",insn.isConditional()
        print "-------------------------"


'''
输出:
 >>>  PUSH
 >>>  16
 >>>  2
 >>>  array('b', [-48, -75])
 >>>  None
 >>>  PUSH
 >>>  array(com.pnfsoftware.jebglobal.WX, [{R4, R6, R7, LR}])
 >>>  False
 >>>  False
-------------------------
 >>>  ADD
 >>>  16
 >>>  2
 >>>  array('b', [2, -81])
 >>>  None
 >>>  ADD
 >>>  array(com.pnfsoftware.jebglobal.WX, [R7, SP, #8])
 >>>  False
 >>>  False
-------------------------
 >>>  MOV
 >>>  16
 >>>  2
 >>>  array('b', [4, 70])
 >>>  None
 >>>  MOV
 >>>  array(com.pnfsoftware.jebglobal.WX, [R4, R0])
 >>>  False
 >>>  False
-------------------------
 >>>  LDR
 >>>  16
 >>>  2
 >>>  array('b', [64, 106])
 >>>  None
 >>>  LDR
 >>>  array(com.pnfsoftware.jebglobal.WX, [R0, [R0, #24h]])
 >>>  False
 >>>  False
-------------------------
......

'''