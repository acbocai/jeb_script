# -*- coding: utf-8 -*-
from com.pnfsoftware.jeb.client.api import IClientContext
from com.pnfsoftware.jeb.core import IRuntimeProject
from com.pnfsoftware.jeb.core.units import IUnit
from com.pnfsoftware.jeb.core.units.code import IDecompilerUnit, DecompilationOptions, DecompilationContext
from com.pnfsoftware.jeb.core.units.code.android import IDexUnit, IDexDecompilerUnit
from com.pnfsoftware.jeb.core.units.code.java import IJavaMethod, IJavaDefinition, IJavaIdentifier, \
    IJavaBlock, IJavaIf
from com.pnfsoftware.jeb.core.util import DecompilerHelper

def displayTree(e, level=0):
    dispatch(e,level)
    if e:
        elts = e.getSubElements()
        for e in elts:
            displayTree(e, level+1)

def dispatch(ele,level):
    if isinstance(ele,IJavaIf):
        # if分支个数
        if ele.size()>1:
            print ele.getPhysicalOffset()

            # if第1个分支的语句序列(类型为IJavaBlock)
            print "01 getBranchBody(0)     >>>",ele.getBranchBody(0)

            # if第2个分支的语句序列
            print "02 getBranchBody(1)     >>>",ele.getBranchBody(1)

            # 获取if第1个分支的谓词(类型为IJavaPredicate,继承接口IJavaArithmeticExpression)
            print "03 getBranchPredicate(0) >>>",ele.getBranchPredicate(0)

            # 获取if第2个分支的谓词(类型为IJavaPredicate,继承接口IJavaArithmeticExpression)
            print "04 getBranchPredicate(1) >>>",ele.getBranchPredicate(1)

            # 谓词的右值/左值/运算符
            print "05 getRight()            >>>",ele.getBranchPredicate(1).getRight()
            print "06 getLeft()             >>>",ele.getBranchPredicate(1).getLeft()
            print "07 getOperator()         >>>",ele.getBranchPredicate(1).getOperator()

            # 谓词的右值/左值的类型
            print "08 Right Element Type    >>> ",ele.getBranchPredicate(1).getRight().getElementType()
            print "09 Left  Element Type    >>> ",ele.getBranchPredicate(1).getLeft().getElementType()

            # 谓词的左值是一个类属性,看一下他的完整签名
            print "10 field sign            >>> ",ele.getBranchPredicate(1).getLeft().getFieldSignature()

            # 谓词的运算符提供的一些方法
            print "11 getOperatorType       >>> ",ele.getBranchPredicate(1).getOperator().getOperatorType()
            print "12 isArithmetic          >>> ",ele.getBranchPredicate(1).getOperator().isArithmetic()
            print "13 isBinary              >>> ",ele.getBranchPredicate(1).getOperator().isBinary()
            print "14 isCast                >>> ",ele.getBranchPredicate(1).getOperator().isCast()
            print "15 isLogical             >>> ",ele.getBranchPredicate(1).getOperator().isLogical()
            print "16 isUnary               >>> ",ele.getBranchPredicate(1).getOperator().isUnary()
            print "17 toString              >>> ",ele.getBranchPredicate(1).getOperator().toString()
            print("--------------")
        pass
    else:
        pass


# IJavaIf
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


# 被解析的目标代码:
'''
if(this.a.f.o == 0) {
    this.a.b.a(0, v0.d);
}
else if(this.a.f.o == 2) {
    this.a.b.a(1, v0.d);
}
'''


# 输出
# 01 getBranchBody(0)     >>> a(this.a.b, 0(int), v0.d)
# 02 getBranchBody(1)     >>> a(this.a.b, 1(int), v0.d)
# 03 getBranchPredicate(0) >>> (this.a.f.o, ==, 0(int))
# 04 getBranchPredicate(1) >>> (this.a.f.o, ==, 2(int))
# 05 getRight()            >>> 2(int)
# 06 getLeft()             >>> this.a.f.o
# 07 getOperator()         >>> ==
# 08 Right Element Type    >>>  Constant
# 09 Left  Element Type    >>>  InstanceField
# 10 field sign            >>>  Lnet/cavas/show/a/b;->o:I
# 11 getOperatorType       >>>  EQ
# 12 isArithmetic          >>>  False
# 13 isBinary              >>>  True
# 14 isCast                >>>  False
# 15 isLogical             >>>  True
# 16 isUnary               >>>  False
# 17 toString              >>>  ==