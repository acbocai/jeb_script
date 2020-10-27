# -*- coding: utf-8 -*-
from com.pnfsoftware.jeb.client.api import IClientContext
from com.pnfsoftware.jeb.core import IRuntimeProject
from com.pnfsoftware.jeb.core.actions import ActionXrefsData, Actions, ActionContext
from com.pnfsoftware.jeb.core.units import IUnit
from com.pnfsoftware.jeb.core.units.code.android import IDexUnit
from com.pnfsoftware.jeb.core.units.code.android.dex import IDexMethod, IDexClass

def Test(ctx):
    assert isinstance(ctx,IClientContext)
    input_path = r"D:\tmp\2\project\about_dex_diff\code\jsq\jsq.dex"
    class_sign  = "Lcom/BestCalculatorCN/MyCalculator;"
    method_sign = "Lcom/BestCalculatorCN/MyCalculator;->b(Lcom/BestCalculatorCN/MyCalculator;Ljava/lang/String;)V"
    unit = ctx.open(input_path);                                    assert isinstance(unit,IUnit)
    prj = ctx.getMainProject();                                     assert isinstance(prj,IRuntimeProject)
    dexUnit = prj.findUnit(IDexUnit);                               assert isinstance(dexUnit,IDexUnit)
    clz = dexUnit.getClass(class_sign);                             assert isinstance(clz,IDexClass)
    method = dexUnit.getMethod(method_sign);                        assert isinstance(method,IDexMethod)

    # 1 查询某method交叉引用列表
    # 使用(unit,操作,地址,itemid)来创建一个context对象,提供给JEB引擎,用于后续执行
    print "------------------------------------------------"
    actionXrefsData = ActionXrefsData()
    actionContext = ActionContext(dexUnit, Actions.QUERY_XREFS, method.getItemId(), None)
    if unit.prepareExecution(actionContext,actionXrefsData):
        for xref_addr in actionXrefsData.getAddresses():
            print xref_addr

    # 2 查询整个class的交叉引用列表
    print "------------------------------------------------"
    actionXrefsData = ActionXrefsData()
    actionContext = ActionContext(dexUnit, Actions.QUERY_XREFS, clz.getItemId(), None)
    if unit.prepareExecution(actionContext,actionXrefsData):
        for idx,xref_addr in enumerate(actionXrefsData.getAddresses()):
            print idx,xref_addr