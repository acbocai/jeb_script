# -*- coding: utf-8 -*-
from com.pnfsoftware.jeb.client.api import IClientContext
from com.pnfsoftware.jeb.core import IRuntimeProject
from com.pnfsoftware.jeb.core.units import IUnit, INativeCodeUnit
from com.pnfsoftware.jeb.core.units.code.asm.decompiler import INativeDecompilerUnit, INativeSourceUnit
from com.pnfsoftware.jeb.core.units.code.asm.decompiler.ast import ICMethod, ICIfStm
from com.pnfsoftware.jeb.core.util import DecompilerHelper

def displayTree(e, level=0):
    dispatch(e,level)
    if e:
        elts = e.getSubElements()
        for e in elts:
            displayTree(e, level+1)
pass

def dispatch(ele,level):
    if isinstance(ele,ICIfStm):
        # 分支代码序列(ICBlock)
        print "level:",level," ","BranchBody(0) >>> "
        print ele.getBranchBody(0)

        # if括号中的谓词
        print "BranchPredicate(0) >>> "
        print ele.getBranchPredicate(0)
        print "-----------------------"
pass

# 语法树元素ifelse
def Test(ctx):
    assert isinstance(ctx,IClientContext)
    input_path = r"D:\tmp\2\project\about_dex_diff\code\xmly\libFace3D.so"
    unit = ctx.open(input_path);                                    assert isinstance(unit,IUnit)
    prj = ctx.getMainProject();                                     assert isinstance(prj,IRuntimeProject)

    # 获取INativeCodeUnit并执行解析
    nativeCodeUnit = prj.findUnit(INativeCodeUnit);                 assert isinstance(nativeCodeUnit,INativeCodeUnit)
    bool = nativeCodeUnit.process()

    # 获取INativeDecompilerUnit并执行解析
    nativeDecompilerUnit = DecompilerHelper.getDecompiler(nativeCodeUnit);  assert isinstance(nativeDecompilerUnit,INativeDecompilerUnit)
    bool = nativeDecompilerUnit.process()

    # 获取函数对应顶层ICElement
    nativeSourceUnit = nativeDecompilerUnit.decompile("sub_11110"); assert isinstance(nativeSourceUnit,INativeSourceUnit)
    rootElement = nativeSourceUnit.getRootElement()

    # 输出全部(F5反编译效果)
    # print rootElement

    # 输出抽象语法树元素
    displayTree(rootElement,0)

'''
level: 2   BranchBody(0) >>>
{
    param0 += 12;
    DMB();
    v0 = *param0;
    *param0 = v0 - 1;
    DMB();
    if(v0 == 1) {
        _ptr_cv::Mat::deallocate();
    }
}
BranchPredicate(0) >>>
param0 != 0
-----------------------
level: 4   BranchBody(0) >>>
{
    _ptr_cv::Mat::deallocate();
}
BranchPredicate(0) >>>
v0 == 1
-----------------------
'''