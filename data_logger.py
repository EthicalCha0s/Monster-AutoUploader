from datetime import datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\u001b[0m'


GREETING = bcolors.OKCYAN + '''
 
`7MMM.     ,MMF'                             mm                   
  MMMb    dPMM                               MM                   
  M YM   ,M MM  ,pW"Wq.`7MMpMMMb.  ,pP"Ybd mmMMmm .gP"Ya `7Mb,od8 
  M  Mb  M' MM 6W'   `Wb MM    MM  8I   `"   MM  ,M'   Yb  MM' "' 
  M  YM.P'  MM 8M     M8 MM    MM  `YMMMa.   MM  8M""""""  MM     
  M  `YM'   MM YA.   ,A9 MM    MM  L.   I8   MM  YM.    ,  MM     
.JML. `'  .JMML.`Ybmd9'.JMML  JMML.M9mmmP'   `Mbmo`Mbmmd'.JMML.   
                                                                                                                                                                                                                                                                                           
''' + bcolors.RESET


class DataLogger:
    def greeting():
        print(GREETING, "\n")

    def log_error(err):
        print(DataLogger.get_date_time_string(),
              bcolors.FAIL + "[Error]:" + bcolors.RESET, err)

    def log_warning(warn):
        print(DataLogger.get_date_time_string(),
              bcolors.WARNING + "[Warning]:" + bcolors.RESET, warn)

    def log_information(msg):
        print(DataLogger.get_date_time_string(),
              bcolors.OKCYAN + "[Information]:" + bcolors.RESET, msg)

    def log_debug(msg):
        print("[Debug]:", msg)

    def get_date_time_string():
        return "[" + datetime.today().strftime('%Y-%m-%d %H:%M:%S') + "]"