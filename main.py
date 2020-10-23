from Test.HDtest import HDTest
from Test.OBMtest import OBMTest
from Test.RDtest import RDTest
from Test.Comparetest import CompareTest
from Test.ICMTest import ICMTest
from Test.LTMtest2 import LTMTest2
from DiffusionModels.Models.HD import HDGraph
import DiffusionModels.Constants.constants as ct
import DiffusionModels.imp.Kstep1 as kStep

if __name__ == '__main__':
    #RD = RDTest(ct.FILE_PATH_2000)
    CompareTest = CompareTest(71, ct.FILE_PATH_2000)
    #RD.draw("E:/project/Experiment/TestResult/RD2000umt.png")
    CompareTest.draw_RH_DH_OBM_MsgAndTime("/Users/ChentingJIANG/Desktop/the university of tasmania/2020-2021 Research/project/MJ Project/Experiment2/TestResult/M_u.png")
