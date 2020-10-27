# -*- coding: utf-8 -*-
from com.pnfsoftware.jeb.client.api import IClientContext
from com.pnfsoftware.jeb.core import IRuntimeProject
from com.pnfsoftware.jeb.core.units import IUnit
from com.pnfsoftware.jeb.core.units.code.android import IDexUnit


# 访问某个Method
def Test(ctx):
    assert isinstance(ctx,IClientContext)
    input_path = r"D:\tmp\2\project\about_dex_diff\code\jsq\jsq.apk"
    method_sign = "Lnet/cavas/show/af;->a(Lorg/apache/http/client/HttpClient;Ljava/util/Queue;)V"

    unit = ctx.open(input_path);                                    assert isinstance(unit,IUnit)
    prj = ctx.getMainProject();                                     assert isinstance(prj,IRuntimeProject)
    dexUnit = prj.findUnit(IDexUnit);                               assert isinstance(dexUnit,IDexUnit)

    # 某方法内容
    method = dexUnit.getMethod(method_sign)
    print "-----------------------------------------------"
    print "1 ClassType         >>> ",method.getClassType()
    print "2 ReturnType        >>> ",method.getReturnType()
    print "3 getName           >>> ",method.getName()
    print "4 getSignature      >>> ",method.getSignature()
    print "5 getParameterTypes >>> "
    for parm in method.getParameterTypes():
        print ">>> ",parm
    print "6 isInternal        >>> ",method.isInternal()
    print "7 isArtificial      >>> ",method.isArtificial()
    print "-----------------------------------------------"

# 输出
# -----------------------------------------------
# 1 ClassType         >>>  Type:#237,name=af,address=Lnet/cavas/show/af;
# 2 ReturnType        >>>  Type:#341,name=V,address=V
# 3 getName           >>>  a
# 4 getSignature      >>>  Lnet/cavas/show/af;->a(Lorg/apache/http/client/HttpClient;Ljava/util/Queue;)V
# 5 getParameterTypes >>>
# >>>  Type:#325,name=HttpClient,address=Lorg/apache/http/client/HttpClient;
# >>>  Type:#216,name=Queue,address=Ljava/util/Queue;
# 6 isInternal        >>>  True
# 7 isArtificial      >>>  False
# -----------------------------------------------