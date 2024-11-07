### Module 경로 지정 ###
import sys
sys.path.append(r"C:\Users\USER\Desktop\조현준 백업\Coding\Test")

### Filename Change Tool 실행 ###
import Second, os
Second.Filename_Change("nowdir", os.path.basename(__file__))

input("Press enter to exit ;)")