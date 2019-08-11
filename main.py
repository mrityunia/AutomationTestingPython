# Created by ********  chomri01 at 8/10/2019

# Feature Name :: --

# To Do ::-

from behave.__main__ import main as behave_main
from sys import exit

if __name__ == '__main__':
    exit(behave_main('--tags=@login --no-capture'))

#behave_main('path/to/feature_file.feature -f json -o /path/to/logs/here')
# to print behave_main('--no-capture')
# to pass tag in behave :: exit(behave_main('--tags=@login,--no-capture'))