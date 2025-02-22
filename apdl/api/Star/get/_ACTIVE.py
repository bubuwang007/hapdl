from functools import partial
from ._func import get_active

class ACTIVE:

    @staticmethod
    def interactive_key(par:str):
        '''Current interactive key: 0=off, 2=on.'''
        return get_active(par, "INT")

    @staticmethod
    def immediate_key(par:str):
        '''Current immediate key: 0=off, 1=on.'''
        return get_active(par, "IMME")

    @staticmethod
    def menu_key(par:str):
        '''Current menu key: 0=off, 1=on.'''
        return get_active(par, "MENU")

    @staticmethod
    def printout_status(par:str):
        '''Printout suppression status: 0=/NOPR, 1=/GOPR or /GO'''
        return get_active(par, "PRKEY")

    @staticmethod
    def current_routine(par:str):
        '''Current routine: 0 = Begin level, 17 = PREP7, 21 = SOLUTION, 31 = POST1, 36 = POST26, 52 = AUX2, 53 = AUX3, 62 = AUX12, 65 = AUX15.'''
        return get_active(par, "ROUT")

    @staticmethod
    def cpu_time(par:str):
        '''CPU time.'''
        return get_active(par, "TIME", "CPU")

    @staticmethod
    def wall_time(par:str):
        '''Wall clock time.'''
        return get_active(par, "TIME", "WALL")

    @staticmethod
    def dbase_ldate(par:str):
        '''Date of first modification of any database quantity required for POST1 operation. The parameter returned is Par = YEAR*10000 + MONTH*100 + DAY.'''
        return get_active(par, "DBASE", "LDATE")
    
    @staticmethod
    def dbase_ltime(par:str):
        '''Time of last modification of any database quantity required for POST1 operation. The parameter returned is Par = HOURS*10000 + MINUTES*100 + SECONDS.'''
        return get_active(par, "DBASE", "LTIME")

    @staticmethod
    def release_version(par:str):
        '''Minor release revision number (5.6, 5.7, 6.0 etc.). Letter notation (e.g., 5.0A) is not included.'''
        return get_active(par, "RELEASE", "REV")
    
    @staticmethod
    def title(par:str, num:int=0):
        '''Current title string of the main title (IT1NUM=0 or blank) or subtitle 1, 2, 3, or 4 (IT1NUM=1,2,3, or 4). A character parameter of up to 8 characters'''
        return get_active(par, "TITLE", str(num))
    
    @staticmethod
    def jobname(par:str):
        '''Current Jobname. A character parameter of up to 8 characters.'''
        return get_active(par, "JOBNAM")

    @staticmethod
    def platform(par:str):
        '''The current platform.'''
        return get_active(par, "PLATFORM")

    @staticmethod
    def current_processors_number(par:str):
        '''The number of processors being used for the current session'''
        return get_active(par, "NPROC", "CURR")
    
    @staticmethod
    def max_processors_number(par:str):
        ''' The maximum total number of processors (physical and virtual) available on the machine'''
        return get_active(par, "NPROC", "MAX")

    @staticmethod
    def max_physical_processors_number(par:str):
        '''the maximum number of physical processors available on the machine.'''
        return get_active(par, "NPROC", "MAXP")

    @staticmethod
    def cpu_number(par:str):
        '''Number of Distributed ANSYS processes being used (distributed memory parallel).'''
        return get_active(par, "NUMCPU")

# print(ACTIVE.current_routine("par"))