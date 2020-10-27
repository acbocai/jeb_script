# -*- coding: utf-8 -*-
from com.pnfsoftware.jeb.client.api import IClientContext
from com.pnfsoftware.jeb.core import IRuntimeProject
from com.pnfsoftware.jeb.core.units import IUnit
from com.pnfsoftware.jeb.core.units.code import IDecompilerUnit, DecompilationOptions, DecompilationContext
from com.pnfsoftware.jeb.core.units.code.android import IDexUnit, IDexDecompilerUnit
from com.pnfsoftware.jeb.core.units.code.java import IJavaMethod,IJavaCall
from com.pnfsoftware.jeb.core.util import DecompilerHelper

def displayTree(e, level=0):
    dispatch(e,level)
    if e:
        elts = e.getSubElements()
        for e in elts:
            displayTree(e, level+1)

def dispatch(ele,level):
    if isinstance(ele,IJavaCall):
        if ele.getMethodName() == "equalsIgnoreCase":
            print "1 getPhysicalOffset()   >>> ",ele.getPhysicalOffset()
            print "2 getCallType()         >>> ",ele.getCallType() # REGULAR 0;SUPER 1;LAMBDA 2;STATIC 3;
            print "3 isSuperCall()         >>> ",ele.isSuperCall()
            print "4 isCustomCall()        >>> ",ele.isCustomCall()
            print "5 isStaticCall()        >>> ",ele.isStaticCall()
            print "6 getMethod()           >>> ",ele.getMethod()
            print "7 getMethodName()       >>> ",ele.getMethodName()
            print "8 getMethodSignature()  >>> ",ele.getMethodSignature()
            print "9 getArguments()        >>> ",ele.getArguments()
            print "10 getArguments()[0]     >>> ",ele.getArguments()[0].getElementType()
            print "11 getArguments()[1]     >>> ",ele.getArguments()[1].getElementType()
            exit(0)
        pass
    else:
        pass


# IJavaCall
def Test(ctx):
    assert isinstance(ctx,IClientContext)
    input_path = r"D:\tmp\2\project\about_dex_diff\code\jsq\jsq.dex"
    sign = "Lnet/cavas/show/bl;->handleMessage(Landroid/os/Message;)V"
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


# 目标代码
# "null".equalsIgnoreCase(v0.b.trim())


'''
输出
---------------- tree ----------------
1 getPhysicalOffset()   >>>  130
2 getCallType()         >>>  0
3 isSuperCall()         >>>  False
4 isCustomCall()        >>>  False
5 isStaticCall()        >>>  False
6 getMethod()           >>>  method:java.lang.String.equalsIgnoreCase
7 getMethodName()       >>>  equalsIgnoreCase
8 getMethodSignature()  >>>  Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z
9 getArguments()        >>>  ["null", trim(v0.b)]
10 getArguments()[0]     >>>  Constant
11 getArguments()[1]     >>>  Call
'''