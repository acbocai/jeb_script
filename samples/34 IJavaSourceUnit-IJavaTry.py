# -*- coding: utf-8 -*-
from com.pnfsoftware.jeb.client.api import IClientContext
from com.pnfsoftware.jeb.core import IRuntimeProject
from com.pnfsoftware.jeb.core.units import IUnit
from com.pnfsoftware.jeb.core.units.code import IDecompilerUnit, DecompilationOptions, DecompilationContext
from com.pnfsoftware.jeb.core.units.code.android import IDexUnit, IDexDecompilerUnit
from com.pnfsoftware.jeb.core.units.code.java import IJavaMethod, IJavaTry
from com.pnfsoftware.jeb.core.util import DecompilerHelper

def displayTree(e, level=0):
    dispatch(e,level)
    if e:
        elts = e.getSubElements()
        for e in elts:
            displayTree(e, level+1)

def dispatch(ele,level):
    if isinstance(ele,IJavaTry):
        print "---------- try body start -----------"
        print ele.getTryBody()                                          # try块语句序列
        print "---------- try body end -------------"
        print "CatchCount          >>> " , ele.getCatchCount()          # catch块个数
        for idx in range(ele.getCatchCount()):
            print ""
            print ""
            print "---------- catch body start -----------",idx
            print "Type            >>> ",ele.getCatchType(idx)          # catch块括号内异常类型
            print "Identifier      >>> ",ele.getCatchIdentifier(idx)    # catch块括号内标识符
            print "catch body      >>> "
            print ele.getCatchBody(idx)                                 # catch块语句序列
            print "---------- catch body end -------------",idx
            print ""
            print ""
        print "finally body    >>>",ele.getFinallyBody()            # final块语句序列
        exit(0)
        pass
    else:
        pass

# IJavaTry
def Test(ctx):
    assert isinstance(ctx,IClientContext)
    input_path = r"D:\tmp\2\project\about_dex_diff\code\jsq\jsq.dex"
    sign = "Lnet/cavas/show/af;->a(Lorg/apache/http/client/HttpClient;Ljava/util/Queue;)V"
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
final class af implements Runnable {
    private void a(HttpClient arg6, Queue arg7) {
        String v0 = (String)arg7.poll();
        if(this.b != null && v0 != null) {
            HttpPost v1 = new HttpPost(this.b.replace(" ", "%20"));
            v1.setEntity(new EntityTemplate(new ag(this, v0)));
            try {
                HttpResponse v0_4 = arg6.execute(((HttpUriRequest)v1));
                c.a("offer", Integer.valueOf(v0_4.getStatusLine().getStatusCode()));
                if(v0_4.getStatusLine().getStatusCode() == 200) {
                    this.a(arg6, arg7);
                    return;
                }
            }
            catch(ClientProtocolException v0_3) {
                try {
                    c.c(d.a, "Caught ClientProtocolException in PingUrlRunnable");
                    return;
                label_35:
                    c.c(d.a, "Caught IOException in PingUrlRunnable");
                    return;
                }
                catch(Throwable v0_1) {
                    throw v0_1;
                }
            }
            catch(IOException v0_2) {
                goto label_35;
                return;
            }
            catch(Throwable v0_1) {
                throw v0_1;
            }
        }
    }
}
'''



'''
输出:
True
---------------- tree ----------------

---------- try body start -----------
org.apache.http.HttpResponse v0_4 = execute(arg6, ((org.apache.http.client.methods.HttpUriRequest), v1))
a("offer", valueOf(getStatusCode(getStatusLine(v0_4))))
If@-2003461530
---------- try body end -------------


CatchCount          >>>  3
---------- catch body start ----------- 0
Type            >>>  org.apache.http.client.ClientProtocolException
Identifier      >>>  v0_3
catch body      >>>
Try@1198833152
---------- catch body end ------------- 0


---------- catch body start ----------- 1
Type            >>>  java.io.IOException
Identifier      >>>  v0_2
catch body      >>>
goto label_35
return
---------- catch body end ------------- 1


---------- catch body start ----------- 2
Type            >>>  java.lang.Throwable
Identifier      >>>  v0_1
catch body      >>>
throw v0_1
---------- catch body end ------------- 2
finally body    >>> None
'''