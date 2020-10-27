# -*- coding: utf-8 -*-
from com.pnfsoftware.jeb.client.api import IClientContext
from com.pnfsoftware.jeb.core import IRuntimeProject
from com.pnfsoftware.jeb.core.units import IUnit, INativeCodeUnit
from com.pnfsoftware.jeb.core.units.code.asm.analyzer import INativeCodeAnalyzer, INativeCodeModel, IReferenceManager, ICallGraphManager, ICallGraph, CallGraphVertex
from com.pnfsoftware.jeb.core.units.code.asm.items import INativeMethodItem


# callees/callers 调用与被调用信息
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

    # 获取ICallGraph
    callGraph = nativeCodeModel.getCallGraphManager().getGlobalCallGraph(); assert isinstance(callGraph,ICallGraph)

    # 函数
    funcName = "libunwind::LocalAddressSpace::findFunctionName"
    nativeMethodItem = nativeCodeUnit.getMethod(funcName);                  assert isinstance(nativeMethodItem,INativeMethodItem)
    print ">>> funcAddr:",hex(nativeMethodItem.getRoutineAddress())

    # callees 目标函数调用了谁
    callGraphVertexList = callGraph.getCallees(nativeMethodItem,False)
    for callGraphVertex in callGraphVertexList:
        assert isinstance(callGraphVertex,CallGraphVertex)
        print ">>> Callee:",hex(callGraphVertex.getInternalAddress().getAddress())

    # callers 目标函数被谁调用
    callerList = callGraph.getCallers(nativeMethodItem,False)
    for caller in callerList:
        print ">>> Callers:",hex(caller)

# >>> funcAddr: 0x19a1cL
# >>> Callee: 0xabfcL
# >>> Callee: 0xac08L
# >>> Callee: 0x9cc0L
# >>> Callers: 0x196b2L        