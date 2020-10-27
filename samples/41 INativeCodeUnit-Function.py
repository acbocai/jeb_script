# -*- coding: utf-8 -*-
from com.pnfsoftware.jeb.client.api import IClientContext
from com.pnfsoftware.jeb.core import IRuntimeProject
from com.pnfsoftware.jeb.core.units import IUnit, INativeCodeUnit
from com.pnfsoftware.jeb.core.units.code.asm.items import INativeMethodItem


# 遍历函数
def Test(ctx):
    assert isinstance(ctx,IClientContext)
    input_path = r"D:\tmp\2\project\about_dex_diff\code\xmly\libFace3D.so"
    unit = ctx.open(input_path);                                    assert isinstance(unit,IUnit)
    prj = ctx.getMainProject();                                     assert isinstance(prj,IRuntimeProject)
    nativeCodeUnit = prj.findUnit(INativeCodeUnit);                 assert isinstance(nativeCodeUnit,INativeCodeUnit)
    bool = nativeCodeUnit.process()

    # Methods
    methodList = nativeCodeUnit.getMethods()
    for idx,method in enumerate(methodList):
        assert isinstance(method,INativeMethodItem)
        print "-------------------------------"
        print " >>> ",idx,method.getItemId()
        print " >>> ",idx,method.getSignature()

    # InternalMethods
    internalMethodlist = nativeCodeUnit.getInternalMethods()
    for idx,method in enumerate(internalMethodlist):
        assert isinstance(method,INativeMethodItem)
        print "-------------------------------"
        print " >>> ",idx,method.getItemId()
        print " >>> ",idx,method.getSignature()

'''
输出:

......
-------------------------------
 >>>  718 -8718968878589278991
 >>>  718 libunwind::UnwindCursor<libunwind::LocalAddressSpace, libunwind::Registers_arm>::getInfoFromEHABISection
-------------------------------
 >>>  719 -8718968878589279141
 >>>  719 std::__ndk1::__upper_bound<std::__ndk1::__less<unsigned int, unsigned int>&, libunwind::EHABISectionIterator<libunwind::LocalAddressSpace>, unsigned int>
-------------------------------
 >>>  720 -8718968878589279140
 >>>  720 sub_1A124
 ......
 
'''