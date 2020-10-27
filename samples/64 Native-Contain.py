# -*- coding: utf-8 -*-
from com.pnfsoftware.jeb.client.api import IClientContext
from com.pnfsoftware.jeb.core import IRuntimeProject
from com.pnfsoftware.jeb.core.units import IUnit, INativeCodeUnit
from com.pnfsoftware.jeb.core.units.code import EntryPointDescription
from com.pnfsoftware.jeb.core.units.code.asm.analyzer import INativeCodeAnalyzer, INativeCodeModel, IReferenceManager, ICallGraphManager, ICallGraph, CallGraphVertex
from com.pnfsoftware.jeb.core.units.code.asm.items import INativeMethodItem


def Test(ctx):
    assert isinstance(ctx,IClientContext)
    input_path = r"D:\tmp\2\project\about_dex_diff\code\xmly\libFace3D.so"
    unit = ctx.open(input_path);                                            assert isinstance(unit,IUnit)
    prj = ctx.getMainProject();                                             assert isinstance(prj,IRuntimeProject)

    # 获取INativeCodeUnit并执行解析
    nativeCodeUnit = prj.findUnit(INativeCodeUnit);                         assert isinstance(nativeCodeUnit,INativeCodeUnit)
    bool = nativeCodeUnit.process()

    # 获取INativeCodeAnalyzer,获取INativeCodeModel
    nativeCodeAnalyzer = nativeCodeUnit.getCodeAnalyzer();                  assert isinstance(nativeCodeAnalyzer,INativeCodeAnalyzer)
    nativeCodeAnalyzer.analyze()
    nativeCodeModel = nativeCodeAnalyzer.getModel();                        assert isinstance(nativeCodeModel,INativeCodeModel)

    # 返回该地址所在函数的首地址
    print "-------------------"
    r = nativeCodeModel.getContainedRoutineAddresses(0x19A60)
    print ">>> ",hex(r[0])

    # 返回该地址所在基本块
    print "-------------------"
    r = nativeCodeModel.getBasicBlockHeader(0x19A60)
    for insn in r.getInstructions():
        print ">>> ",insn.getMnemonic()

# -------------------
# >>>  0x19a1cL
# -------------------
# >>>  LDR
# >>>  LDR
# >>>  SUBS
# >>>  ITTT
# >>>  ADDEQ
# >>>  POPEQ
# >>>  POPEQ