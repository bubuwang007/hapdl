import enum

class Processor(enum.Enum):
    begin = "FINISH"
    prep7 = "/PREP7"
    post26 = "/POST26"
    post1 = "/POST1"
    solu = "/SOLU"
    opt = "/OPT"
    pds = "/PDS"
    aux2 = "/AUX2"
    aux12 = "/AUX12"
    aux15 = "/AUX15"
    runstat = "/RUNSTAT"