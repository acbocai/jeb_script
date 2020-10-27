# -*- coding: utf-8 -*-
from com.pnfsoftware.jeb.client.api import IClientContext
from com.pnfsoftware.jeb.core import IRuntimeProject
from com.pnfsoftware.jeb.core.units import IUnit
from com.pnfsoftware.jeb.core.units.code import IDecompilerUnit, DecompilationOptions, DecompilationContext
from com.pnfsoftware.jeb.core.units.code.android import IDexUnit, IDexDecompilerUnit
from com.pnfsoftware.jeb.core.units.code.java import IJavaMethod,IJavaFor
from com.pnfsoftware.jeb.core.util import DecompilerHelper

def displayTree(e, level=0):
    dispatch(e,level)
    if e:
        elts = e.getSubElements()
        for e in elts:
            displayTree(e, level+1)

def dispatch(ele,level):
    if isinstance(ele,IJavaFor):
        # 初始化语句
        print "1 Initializer     >>>  ",ele.getInitializer(),ele.getInitializer().getElementType()

        # 循环谓词
        print "2 Predicate       >>>  ",ele.getPredicate(),ele.getPredicate().getElementType()

        # 迭代后语句
        print "3 PostStatement   >>>  ",ele.getPostStatement(),ele.getPostStatement().getElementType()

        # 循环体
        print "4 Body            >>>  "
        print ele.getBody()
        pass
    else:
        pass


# IJavaFor
def Test(ctx):
    assert isinstance(ctx,IClientContext)
    input_path = r"D:\tmp\2\project\about_dex_diff\code\jsq\jsq.dex"
    sign = "Lcom/BestCalculatorCN/MyCalculator;->m(Lcom/BestCalculatorCN/MyCalculator;)Z"
    unit = ctx.open(input_path);                                    assert isinstance(unit,IUnit)
    prj = ctx.getMainProject();                                     assert isinstance(prj,IRuntimeProject)
    dexUnit = prj.findUnit(IDexUnit);                               assert isinstance(dexUnit,IDexUnit)
    dexDecompilerUnit = DecompilerHelper.getDecompiler(dexUnit);    assert isinstance(dexDecompilerUnit,IDexDecompilerUnit)
    opt = DecompilationOptions.Builder().newInstance().flags(IDecompilerUnit.FLAG_NO_DEFERRED_DECOMPILATION).build()
    bool = dexDecompilerUnit.decompileAllClasses(DecompilationContext(opt))
    print(bool)
    javaMethod = dexDecompilerUnit.getMethod(sign,False);           assert isinstance(javaMethod,IJavaMethod)
    print("---------------- tree ----------------")
    displayTree(javaMethod)


'''
目标代码:
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


'''
输出
True
---------------- tree ----------------
1 Initializer     >>>   v1 = 0(int) Assignment
2 Predicate       >>>   (true) Predicate
3 PostStatement   >>>   ++v1 Assignment
4 Body            >>>
If@496760551
If@1458799117
'''