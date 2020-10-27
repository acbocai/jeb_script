# -*- coding: utf-8 -*-
from com.pnfsoftware.jeb.client.api import IScript, IClientContext
from com.pnfsoftware.jeb.core import IRuntimeProject, ILiveArtifact, IEnginesContext
from com.pnfsoftware.jeb.core.units import IUnit
from com.pnfsoftware.jeb.core.units.code.android import IDexUnit, IDexDecompilerUnit
from com.pnfsoftware.jeb.core.units.code.android.dex import IDexClass, IDexField, IDexMethod


# 遍历Field / Method
def Test(ctx):
    assert isinstance(ctx,IClientContext)
    input_path = r"D:\tmp\2\project\about_dex_diff\code\jsq\jsq.apk"
    sign = "Lcom/BestCalculatorCN/MyCalculator;"
    unit = ctx.open(input_path);                                    assert isinstance(unit,IUnit)
    prj = ctx.getMainProject();                                     assert isinstance(prj,IRuntimeProject)
    dexUnit = prj.findUnit(IDexUnit);                               assert isinstance(dexUnit,IDexUnit)
    dexClass = dexUnit.getClass(sign);                              assert isinstance(dexClass,IDexClass)

    # 遍历属性
    for field in dexClass.getFields():
        assert isinstance(field,IDexField)
        print ">>> ",field.getSignature()
    print "----"

    # 遍历方法
    for method in dexClass.getMethods():
        assert isinstance(method,IDexMethod)
        print ">>> ",method.getSignature()

# 输出
# >>>  Lcom/BestCalculatorCN/MyCalculator;-><init>()V
# >>>  Lcom/BestCalculatorCN/MyCalculator;->a(Ljava/lang/String;)D
# >>>  Lcom/BestCalculatorCN/MyCalculator;->a(Lcom/BestCalculatorCN/MyCalculator;)Ljava/lang/String;
# >>>  Lcom/BestCalculatorCN/MyCalculator;->a(Lcom/BestCalculatorCN/MyCalculator;D)V
# >>>  Lcom/BestCalculatorCN/MyCalculator;->a(Lcom/BestCalculatorCN/MyCalculator;Lcom/BestCalculatorCN/ar;)V