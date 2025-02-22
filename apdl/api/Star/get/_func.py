
def get(par: str, entity: str, entnum: int, item1: str, it1num: int, item2: str, it2num: int) -> str:
    return f"*GET,{par},{entity},{entnum},{item1},{it1num},{item2},{it2num}"

def get_active(par: str, item1: str, it1num: str="") -> str:
    return get(par, "ACTIVE", 0, item1, it1num, "", "")

def get_cmd(par: str, item1: str, it1num: str="") -> str:
    return get(par, "CMD", 0, item1, it1num, "", "")

def get_comp(par: str, entnum: int, item1: str, it1num: int="") -> str:
    return get(par, "COMP", entnum, item1, it1num, "", "")