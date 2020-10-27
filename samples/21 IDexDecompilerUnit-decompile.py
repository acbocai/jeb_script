# -*- coding: utf-8 -*-
from com.pnfsoftware.jeb.client.api import IClientContext
from com.pnfsoftware.jeb.core import IRuntimeProject
from com.pnfsoftware.jeb.core.units import IUnit
from com.pnfsoftware.jeb.core.units.code import DecompilationOptions, IDecompilerUnit, DecompilationContext
from com.pnfsoftware.jeb.core.units.code.android import IDexUnit, IDexDecompilerUnit
from com.pnfsoftware.jeb.core.util import DecompilerHelper

# F5反编译Class
def Test(ctx):
    assert isinstance(ctx,IClientContext)
    input_path = r"D:\tmp\2\project\about_dex_diff\code\jsq\jsq.dex"
    sign = "Lnet/cavas/show/aa;"
    unit = ctx.open(input_path);                                    assert isinstance(unit,IUnit)
    prj = ctx.getMainProject();                                     assert isinstance(prj,IRuntimeProject)
    dexUnit = prj.findUnit(IDexUnit);                               assert isinstance(dexUnit,IDexUnit)

    dexDecompilerUnit = DecompilerHelper.getDecompiler(dexUnit);    assert isinstance(dexDecompilerUnit,IDexDecompilerUnit)
    opt = DecompilationOptions.Builder().newInstance().flags(IDecompilerUnit.FLAG_NO_DEFERRED_DECOMPILATION).build()
    bool = dexDecompilerUnit.decompileAllClasses(DecompilationContext(opt))
    text = dexDecompilerUnit.getDecompiledClassText(sign)
    print("-------------------------------------")
    print text
    print("-------------------------------------")

# 输出
'''
package net.cavas.show;

import java.util.Comparator;
import net.cavas.show.a.b;

final class aa implements Comparator {
    final x a;

    aa(x arg1) {
        this.a = arg1;
        super();
    }

    @Override
    public final int compare(Object arg3, Object arg4) {
        b v3 = (b)arg3;
        b v4 = (b)arg4;
        if(v3.o < v4.o) {
            return 1;
        }
        return v3.o <= v4.o ? 0 : -1;
    }
}
'''