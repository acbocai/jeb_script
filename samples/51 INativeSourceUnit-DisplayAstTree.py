# -*- coding: utf-8 -*-
from com.pnfsoftware.jeb.client.api import IClientContext
from com.pnfsoftware.jeb.core import IRuntimeProject
from com.pnfsoftware.jeb.core.units import IUnit, INativeCodeUnit
from com.pnfsoftware.jeb.core.units.code.asm.decompiler import INativeDecompilerUnit, INativeSourceUnit
from com.pnfsoftware.jeb.core.util import DecompilerHelper

def displayTree(e, level=0):
    dispatch(e,level)
    if e:
        elts = e.getSubElements()
        for e in elts:
            displayTree(e, level+1)

def dispatch(ele,level):
    print(level,"<",ele.getElementType(),"> >>>")
    print(ele)
    print("----------------------------------------")

# 输出语法树
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
    # print rootElement

    # 输出
    displayTree(rootElement,0)

'''
输出
----------------------------------------
(1, '<', Definition, '> >>>')
unsigned int param0
----------------------------------------
(1, '<', Block, '> >>>')
{
    unsigned int v0;
    unsigned int v1 = param0;
    param0 = *(param0 + 36);
    if(param0 != 0) {
        param0 += 12;
        DMB();
        v0 = *param0;
        *param0 = v0 - 1;
        DMB();
        if(v0 == 1) {
            _ptr_cv::Mat::deallocate();
        }
    }
    v0 = 0;
    *(v1 + 16) = 0;
    *(v1 + 20) = 0;
    *(v1 + 24) = 0;
    *(v1 + 28) = 0;
    *(v1 + 36) = 0;
    while(*(v1 + 4) > ((int)v0)) {
        *(v0 * 4 + *(v1 + 40)) = 0;
        ++v0;
    }
    return 0;
}
----------------------------------------
(2, '<', Definition, '> >>>')
unsigned int v0
----------------------------------------
(2, '<', Assignment, '> >>>')
unsigned int v1 = param0
----------------------------------------
(3, '<', Definition, '> >>>')
unsigned int v1
----------------------------------------
(3, '<', Identifier, '> >>>')
param0
----------------------------------------
(2, '<', Assignment, '> >>>')
param0 = *(param0 + 36)
----------------------------------------
(3, '<', Identifier, '> >>>')
param0
----------------------------------------
(3, '<', Operation, '> >>>')
* param0 + 36
----------------------------------------
(4, '<', Operation, '> >>>')
param0 + 36
......

'''