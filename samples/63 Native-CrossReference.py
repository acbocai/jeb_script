# -*- coding: utf-8 -*-
from com.pnfsoftware.jeb.client.api import IClientContext
from com.pnfsoftware.jeb.core import IRuntimeProject
from com.pnfsoftware.jeb.core.units import IUnit, INativeCodeUnit
from com.pnfsoftware.jeb.core.units.code import EntryPointDescription
from com.pnfsoftware.jeb.core.units.code.asm.analyzer import INativeCodeAnalyzer, INativeCodeModel, IReferenceManager, ICallGraphManager, ICallGraph, CallGraphVertex
from com.pnfsoftware.jeb.core.units.code.asm.items import INativeMethodItem


# 原生库交叉引用信息
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

    # 获取一个函数入口指令地址的交叉引用列表
    funcName = "libunwind::LocalAddressSpace::findFunctionName"
    funcAddr = nativeCodeUnit.getMethod(funcName).getRoutineAddress()
    print ">>> funcAddr:",hex(funcAddr)
    referenceManager = nativeCodeModel.getReferenceManager()
    referenceList = referenceManager.getReferencesToTarget(funcAddr)
    print ">>> funcAddr referenceList:",referenceList

    # 获取一个基本块入口指令地址的交叉引用列表
    referenceList = referenceManager.getReferencesToTarget(0x19A5E)
    print ">>> block referenceList:",referenceList

# >>> funcAddr: 0x19a1cL
# >>> funcAddr referenceList: [196B2h]
# >>> block referenceList: [19A3Ch, 19A40h]    