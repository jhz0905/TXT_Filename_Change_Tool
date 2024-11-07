### Module 경로 지정 ###
import sys
sys.path.append(r"C:\Users\USER\Desktop\조현준 백업\Coding\Module")

### Filename Change Tool 실행 ###
import Module, os
Module.Filename_Change("nowdir", os.path.basename(__file__))

input("Press enter to exit ;)")