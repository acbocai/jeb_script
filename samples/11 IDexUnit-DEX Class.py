# -*- coding: utf-8 -*-
from com.pnfsoftware.jeb.client.api import IScript, IClientContext
from com.pnfsoftware.jeb.core import IRuntimeProject, ILiveArtifact, IEnginesContext
from com.pnfsoftware.jeb.core.units import IUnit
from com.pnfsoftware.jeb.core.units.code.android import IDexUnit, IDexDecompilerUnit

# 访问DEX与Class
def Test(ctx):
    assert isinstance(ctx,IClientContext)
    input_path = r"D:\tmp\2\project\about_dex_diff\code\taobao\taobao.apk"
    sign = "Lcom/taobao/android/diva/core/BitmapProvider;"

    # JEB打开APK
    unit = ctx.open(input_path);                                    assert isinstance(unit,IUnit)

    # 获取JEB加载的项目实例
    prj = ctx.getMainProject();                                     assert isinstance(prj,IRuntimeProject)

    # 访问DEX(DEX被合并,产生了一个虚拟DEX单元)
    dexUnit = prj.findUnit(IDexUnit);                               assert isinstance(dexUnit,IDexUnit)

    # 访问DEX中Class
    cls = dexUnit.getClass(sign)
    print ">>> ",cls.getSignature()

# 输出
# >>>  Lcom/taobao/android/diva/core/BitmapProvider;