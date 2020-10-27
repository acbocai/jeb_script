# -*- coding: utf-8 -*-
from com.pnfsoftware.jeb.client.api import IClientContext
from com.pnfsoftware.jeb.core import IRuntimeProject
from com.pnfsoftware.jeb.core.units import IUnit
from com.pnfsoftware.jeb.core.units.code import IDecompilerUnit, DecompilationOptions, DecompilationContext
from com.pnfsoftware.jeb.core.units.code.android import IDexUnit, IDexDecompilerUnit
from com.pnfsoftware.jeb.core.units.code.java import IJavaMethod
from com.pnfsoftware.jeb.core.util import DecompilerHelper

def displayTree(e, level=0):
    dispatch(e,level)
    if e:
        elts = e.getSubElements()
        for e in elts:
            displayTree(e, level+1)

def dispatch(ele,level):
    print(level,"<",ele.getElementType(),"> >>>",ele)

# 输出语法树内容
def Test(ctx):
    assert isinstance(ctx,IClientContext)
    input_path = r"D:\tmp\2\project\about_dex_diff\code\jsq\jsq.dex"
    sign = "Lcom/BestCalculatorCN/MyCalculator;->m(Lcom/BestCalculatorCN/MyCalculator;)Z"
    unit = ctx.open(input_path);                                    assert isinstance(unit,IUnit)
    prj = ctx.getMainProject();                                     assert isinstance(prj,IRuntimeProject)
    dexUnit = prj.findUnit(IDexUnit);                               assert isinstance(dexUnit,IDexUnit)

    # 发现使用DecompilationContext时,才能出现javablock,不然block为0,没有进行解析
    dexDecompilerUnit = DecompilerHelper.getDecompiler(dexUnit);    assert isinstance(dexDecompilerUnit,IDexDecompilerUnit)
    opt = DecompilationOptions.Builder().newInstance().flags(IDecompilerUnit.FLAG_NO_DEFERRED_DECOMPILATION).build()
    bool = dexDecompilerUnit.decompileAllClasses(DecompilationContext(opt))
    print(bool)
    javaMethod = dexDecompilerUnit.getMethod(sign,False);           assert isinstance(javaMethod,IJavaMethod)
    displayTree(javaMethod)


# 方法原型
'''
static boolean m(MyCalculator arg5) {
    int v2 = arg5.S.length();
    int v1;
    for(v1 = 0; true; ++v1) {
        if(v1 >= v2) {
            return false;
        }

        if(arg5.S.charAt(v1) == 120) {
            return true;
        }
    }
}
'''

# 输出
# True
# (0, '<', Method, '> >>>', method:com.BestCalculatorCN.MyCalculator.m)
# (1, '<', Definition, '> >>>', com.BestCalculatorCN.MyCalculator arg5)
# (2, '<', Identifier, '> >>>', arg5)
# (1, '<', Block, '> >>>', int v2 = length(arg5.S)
# int v1
# For@665729435
# )
# (2, '<', Assignment, '> >>>', int v2 = length(arg5.S))
# (3, '<', Definition, '> >>>', int v2)
# (4, '<', Identifier, '> >>>', v2)
# (3, '<', Call, '> >>>', length(arg5.S))
# (4, '<', InstanceField, '> >>>', arg5.S)
# (5, '<', Identifier, '> >>>', arg5)
# (2, '<', Definition, '> >>>', int v1)
# (3, '<', Identifier, '> >>>', v1)
# (2, '<', For, '> >>>', For@665729435)
# (3, '<', Assignment, '> >>>', v1 = 0(int))
# (4, '<', Identifier, '> >>>', v1)
# (4, '<', Constant, '> >>>', 0(int))
# (3, '<', Predicate, '> >>>', (true))
# (4, '<', Constant, '> >>>', true)
# (3, '<', Assignment, '> >>>', ++v1)
# (4, '<', Identifier, '> >>>', v1)
# (3, '<', Block, '> >>>', If@549618061
# If@-1864570085
# )
# (4, '<', If, '> >>>', If@549618061)
# (5, '<', Predicate, '> >>>', (v1, >=, v2))
# (6, '<', Identifier, '> >>>', v1)
# (6, '<', Identifier, '> >>>', v2)
# (5, '<', Block, '> >>>', return false
# )
# (6, '<', Return, '> >>>', return false)
# (7, '<', Constant, '> >>>', false)
# (4, '<', If, '> >>>', If@-1864570085)
# (5, '<', Predicate, '> >>>', (charAt(arg5.S, v1), ==, 0x78(int)))
# (6, '<', Call, '> >>>', charAt(arg5.S, v1))
# (7, '<', InstanceField, '> >>>', arg5.S)
# (8, '<', Identifier, '> >>>', arg5)
# (7, '<', Identifier, '> >>>', v1)
# (6, '<', Constant, '> >>>', 0x78(int))
# (5, '<', Block, '> >>>', return true
# )
# (6, '<', Return, '> >>>', return true)
# (7, '<', Constant, '> >>>', true)