# -*- coding: utf-8 -*-
from com.pnfsoftware.jeb.client.api import IClientContext
from com.pnfsoftware.jeb.core import IRuntimeProject
from com.pnfsoftware.jeb.core.units import IUnit
from com.pnfsoftware.jeb.core.units.code import IFlowInformation, IEntryPointDescription
from com.pnfsoftware.jeb.core.units.code.android import IDexUnit
from com.pnfsoftware.jeb.core.units.code.android.dex import IDexMethod, IDexClass, IDexMethodData, IDexCodeItem, \
    IDalvikInstruction

# 访问指令
def Test(ctx):
    assert isinstance(ctx,IClientContext)
    input_path = r"D:\tmp\2\project\about_dex_diff\code\jsq\jsq.dex"
    unit = ctx.open(input_path);                                    assert isinstance(unit,IUnit)
    prj = ctx.getMainProject();                                     assert isinstance(prj,IRuntimeProject)
    sign = "Lcom/BestCalculatorCN/MyCalculator;"
    sign2 = "Lnet/cavas/show/af;->a(Lorg/apache/http/client/HttpClient;Ljava/util/Queue;)V"

    dexUnit = prj.findUnit(IDexUnit);                               assert isinstance(dexUnit,IDexUnit);
    clz = dexUnit.getClass(sign);                                   assert isinstance(clz,IDexClass);
    method = dexUnit.getMethod(sign2);                              assert isinstance(method,IDexMethod)
    dexMethodData = method.getData();                               assert isinstance(dexMethodData,IDexMethodData)
    dexCodeItem= dexMethodData.getCodeItem();                       assert isinstance(dexCodeItem,IDexCodeItem)

    # 方法的指令序列信息
    print "1 RegisterCount                    >>> ", dexCodeItem.getRegisterCount()
    print "2 InputArgumentCount               >>> ", dexCodeItem.getInputArgumentCount()
    print "3 OutputArgumentCount              >>> ", dexCodeItem.getOutputArgumentCount()
    print "4 ExceptionItems                   >>> ", dexCodeItem.getExceptionItems()
    print "5 InstructionsOffset               >>> ", dexCodeItem.getInstructionsOffset()
    print "6 InstructionsSize                 >>> ", dexCodeItem.getInstructionsSize()
    print "7 isCompleteBytecode               >>> ", dexCodeItem.isCompleteBytecode()

    # DVM单个指令信息
    print "8 Instructions:",
    print
    for idx,insn in enumerate(dexCodeItem.getInstructions()):
        assert isinstance(insn,IDalvikInstruction)
        print insn
        print idx,"(01) getCode                      >>> ",insn.getCode()               # 二进制
        print idx,"(02) getOpcode                    >>> ",insn.getOpcode()             # 操作码
        print idx,"(03) getParameters:"                                                 # 指令操作数
        for a,b in enumerate(insn.getParameters()):
            print "<",a,">",b.getType(),b.getValue()
        print idx,"(04) getParameterFirstIndexType   >>> ",insn.getParameterFirstIndexType()# 指令索引参数 池类型
        print idx,"(05) getParameterSecondIndexType  >>> ",insn.getParameterSecondIndexType()
        print idx,"(06) isPseudoInstruction          >>> ",insn.isPseudoInstruction()   # 伪指令
        print idx,"(07) isSwitch                     >>> ",insn.isSwitch()
        print idx,"(08) isArray                      >>> ",insn.isArray()
        print idx,"(99) getSwitchData                >>> ",insn.getSwitchData()
        print idx,"(10) getArrayData                 >>> ",insn.getArrayData()

        print idx,"(11) getProcessorMode             >>> ",insn.getProcessorMode()          # 处理模式
        print idx,"(12) getSize                      >>> ",insn.getSize()                   # 指令size
        print idx,"(13) getPrefix                    >>> ",insn.getPrefix()                 # 指令可选前缀
        print idx,"(14) getMnemonic                  >>> ",insn.getMnemonic()               # 助记符
        print idx,"(15) getOperands                  >>> ",insn.getOperands()               # 操作数列表
        print idx,"(16) canThrow                     >>> ",insn.canThrow()                  # 指令是否可以引发异常
        print idx,"(17) isConditional                >>> ",insn.isConditional()             # 条件执行
        print("")

        # 指令是否中断了执行流
        print idx,"(18) getBreakingFlow:"
        iflowInformation = insn.getBreakingFlow();  assert isinstance(iflowInformation,IFlowInformation)
        print "BreakingFlow.isBroken                >>> ",iflowInformation.isBroken()                       # 确定此对象是否包含流信息
        print "BreakingFlow.isBrokenUnknown         >>> ",iflowInformation.isBrokenUnknown()                # 确定此对象是否包含流信息，但没有已知的目标
        print "BreakingFlow.isBrokenKnown           >>> ",iflowInformation.isBrokenKnown()                  # 确定此对象是否包含流信息，目标已知
        print "BreakingFlow.mustComputeFallThrough  >>> ",iflowInformation.mustComputeFallThrough()         # 指示流信息是否包含一个直达地址
        print "BreakingFlow.getDelaySlotCount       >>> ",iflowInformation.getDelaySlotCount()              # 获取延迟槽中的指令数
        print "BreakingFlow.getTargets:"
        if iflowInformation.getTargets() is not None:
            for a,b in enumerate(iflowInformation.getTargets()):
                assert isinstance(b,IEntryPointDescription)
                print "<",a,">","BreakingFlow.getMode             >>> ",b.getMode()
                print "<",a,">","BreakingFlow.isUnknownAddress    >>> ",b.isUnknownAddress()
                print "<",a,">","BreakingFlow.getAddress          >>> ",b.getAddress()
        print("")

        # 指令是否分支(或调用)到子例程(和18一样的代码)
        print idx,"(19) getRoutineCall:"
        iflowInformation = insn.getRoutineCall();  assert isinstance(iflowInformation,IFlowInformation)
        print "RoutineCall.isBroken                >>> ",iflowInformation.isBroken()
        print "RoutineCall.isBrokenUnknown         >>> ",iflowInformation.isBrokenUnknown()
        print "RoutineCall.isBrokenKnown           >>> ",iflowInformation.isBrokenKnown()
        print "RoutineCall.mustComputeFallThrough  >>> ",iflowInformation.mustComputeFallThrough()
        print "RoutineCall.getDelaySlotCount       >>> ",iflowInformation.getDelaySlotCount()
        print "RoutineCall.getTargets:"
        if iflowInformation.getTargets() is not None:
            for a,b in enumerate(iflowInformation.getTargets()):
                assert isinstance(b,IEntryPointDescription)
                print "<",a,">","RoutineCall.getMode             >>> ",b.getMode()
                print "<",a,">","RoutineCall.isUnknownAddress    >>> ",b.isUnknownAddress()
                print "<",a,">","RoutineCall.getAddress          >>> ",b.getAddress()
        print("")

        # 确定一条指令,是否间接分支(调用)子例程(和18一样的代码)
        print idx,"(20) getIndirectRoutineCall:"
        iflowInformation = insn.getIndirectRoutineCall();  assert isinstance(iflowInformation,IFlowInformation)
        print "IndirectRoutineCall.isBroken                >>> ",iflowInformation.isBroken()
        print "IndirectRoutineCall.isBrokenUnknown         >>> ",iflowInformation.isBrokenUnknown()
        print "IndirectRoutineCall.isBrokenKnown           >>> ",iflowInformation.isBrokenKnown()
        print "IndirectRoutineCall.mustComputeFallThrough  >>> ",iflowInformation.mustComputeFallThrough()
        print "IndirectRoutineCall.getDelaySlotCount       >>> ",iflowInformation.getDelaySlotCount()
        print "IndirectRoutineCall.getTargets:"
        if iflowInformation.getTargets() is not None:
            for a,b in enumerate(iflowInformation.getTargets()):
                assert isinstance(b,IEntryPointDescription)
                print "<",a,">","IndirectRoutineCall.getMode             >>> ",b.getMode()
                print "<",a,">","IndirectRoutineCall.isUnknownAddress    >>> ",b.isUnknownAddress()
                print "<",a,">","IndirectRoutineCall.getAddress          >>> ",b.getAddress()
        print("")
        print("----------------------------------------------------------------------------")
        break
# 输出
# 1 RegisterCount                    >>>  8
# 2 InputArgumentCount               >>>  3
# 3 OutputArgumentCount              >>>  3
# 4 ExceptionItems                   >>>  [try=[52h-9Ah[ handlers=[9Ch:324, B2h:165, AEh:X], try=[9Eh-ACh[ handlers=[AEh:X], try=[B4h-C2h[ handlers=[AEh:X]]
# 5 InstructionsOffset               >>>  66644
# 6 InstructionsSize                 >>>  196
# 7 isCompleteBytecode               >>>  True
# 8 Instructions:
# invoke-interface
# 0 (01) getCode                      >>>  array('b', [114, 16, 116, 2, 7, 0])
# 0 (02) getOpcode                    >>>  114
# 0 (03) getParameters:
# < 0 > 2 628
# < 1 > 0 7
# 0 (04) getParameterFirstIndexType   >>>  19
# 0 (05) getParameterSecondIndexType  >>>  0
# 0 (06) isPseudoInstruction          >>>  False
# 0 (07) isSwitch                     >>>  False
# 0 (08) isArray                      >>>  False
# 0 (99) getSwitchData                >>>  None
# 0 (10) getArrayData                 >>>  None
# 0 (11) getProcessorMode             >>>  0
# 0 (12) getSize                      >>>  6
# 0 (13) getPrefix                    >>>  None
# 0 (14) getMnemonic                  >>>  invoke-interface
# 0 (15) getOperands                  >>>  array(com.pnfsoftware.jebglobal.hy, [t=2,v=628, t=0,v=7])
# 0 (16) canThrow                     >>>  True
# 0 (17) isConditional                >>>  False

# 0 (18) getBreakingFlow:
# BreakingFlow.isBroken                >>>  False
# BreakingFlow.isBrokenUnknown         >>>  False
# BreakingFlow.isBrokenKnown           >>>  False
# BreakingFlow.mustComputeFallThrough  >>>  False
# BreakingFlow.getDelaySlotCount       >>>  0
# BreakingFlow.getTargets:

# 0 (19) getRoutineCall:
# RoutineCall.isBroken                >>>  False
# RoutineCall.isBrokenUnknown         >>>  False
# RoutineCall.isBrokenKnown           >>>  False
# RoutineCall.mustComputeFallThrough  >>>  False
# RoutineCall.getDelaySlotCount       >>>  0
# RoutineCall.getTargets:

# 0 (20) getIndirectRoutineCall:
# IndirectRoutineCall.isBroken                >>>  False
# IndirectRoutineCall.isBrokenUnknown         >>>  False
# IndirectRoutineCall.isBrokenKnown           >>>  False
# IndirectRoutineCall.mustComputeFallThrough  >>>  False
# IndirectRoutineCall.getDelaySlotCount       >>>  0
# IndirectRoutineCall.getTargets:
# ----------------------------------------------------------------------------