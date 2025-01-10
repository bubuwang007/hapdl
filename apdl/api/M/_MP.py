from .._api import _api, Processor

class MP(_api):
    '''Defines a linear material property as a constant or a function of temperature.'''
    processor = Processor.prep7

    @classmethod
    def _check(cls, command):
        raise NotImplementedError
    
    @staticmethod
    def alpd(mat_id, *value):
        '''Mass matrix multiplier for damping.'''
        return f"MP,ALPD,{mat_id},{','.join([str(i) for i in value])}"

    @staticmethod
    def alpx(mat_id, *value):
        '''Secant coefficients of thermal expansion (also ALPY, ALPZ).'''
        return f"MP,ALPX,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def alpy(mat_id, *value):
        '''Secant coefficients of thermal expansion (also ALPX, ALPZ).'''
        return f"MP,ALPY,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def alpz(mat_id, *value):
        '''Secant coefficients of thermal expansion (also ALPX, ALPY).'''
        return f"MP,ALPZ,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def betd(mat_id, *value):
        '''Stiffness matrix multiplier for damping.'''
        return f"MP,BETD,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def betx(mat_id, *value):
        '''Coefficient of diffusion expansion (also BETY, BETZ)'''
        return f"MP,BETX,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def bety(mat_id, *value):
        '''Coefficient of diffusion expansion (also BETX, BETZ)'''
        return f"MP,BETY,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def betz(mat_id, *value):
        '''Coefficient of diffusion expansion (also BETX, BETY)'''
        return f"MP,BETZ,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def bvis(mat_id, *value):
        '''Bulk viscosity.'''
        return f"MP,BVIS,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def c(mat_id, *value):
        '''Specific heat.'''
        return f"MP,C,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def cref(mat_id, *value):
        '''Reference concentration (may not be temperature dependent)'''
        return f"MP,CREF,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def csat(mat_id, *value):
        '''Saturated concentration'''
        return f"MP,CSAT,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def ctex(mat_id, *value):
        '''Instantaneous coefficients of thermal expansion (also CTEY, CTEZ)'''
        return f"MP,CTEX,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def ctey(mat_id, *value):
        '''Instantaneous coefficients of thermal expansion (also CTEX, CTEZ)'''
        return f"MP,CTEY,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def ctez(mat_id, *value):
        '''Instantaneous coefficients of thermal expansion (also CTEX, CTEY)'''
        return f"MP,CTEZ,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def dens(mat_id, *value):
        '''Density.'''
        return f"MP,DENS,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def dmpr(mat_id, *value):
        '''Constant structural damping coefficient in harmonic analysis (full and QRDAMP mode-superposition). Damping ratio in non-QRDAMP mode-superposition analysis. As a constant structural damping coefficient, it is also supported in transient analyses (full and QRDAMP mode-superposition) when an average excitation frequency is specified (DMPSFreq on TRNOPT).'''
        return f"MP,DMPR,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def dxx(mat_id, *value):
        '''Diffusion coefficient (also DYY, DZZ)'''
        return f"MP,DXX,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def dyy(mat_id, *value):
        '''Diffusion coefficient (also DXX, DZZ)'''
        return f"MP,DYY,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def dzz(mat_id, *value):
        '''Diffusion coefficient (also DXX, DYY)'''
        return f"MP,DZZ,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def emis(mat_id, *value):
        '''Emissivity.'''
        return f"MP,EMIS,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def enth(mat_id, *value):
        '''Enthalpy.'''
        return f"MP,ENTH,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def ex(mat_id, *value):
        '''Elastic moduli (also EY, EZ)'''
        return f"MP,EX,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def ey(mat_id, *value):
        '''Elastic moduli (also EX, EZ)'''
        return f"MP,EY,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def ez(mat_id, *value):
        '''Elastic moduli (also EX, EY)'''
        return f"MP,EZ,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def gxy(mat_id, *value):
        '''Shear moduli (also GYZ, GXZ)'''
        return f"MP,GXY,{mat_id},{','.join([str(i) for i in value])}"

    @staticmethod
    def gyz(mat_id, *value):
        '''Shear moduli (also GXY, GXZ)'''
        return f"MP,GYZ,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def gxz(mat_id, *value):
        '''Shear moduli (also GXY, GYZ)'''
        return f"MP,GXZ,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def hf(mat_id, *value):
        '''Convection or film coefficient'''
        return f"MP,HF,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def kxx(mat_id, *value):
        '''Thermal conductivity (also KYY, KZZ)'''
        return f"MP,KXX,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def kyy(mat_id, *value):
        '''Thermal conductivity (also KXX, KZZ)'''
        return f"MP,KYY,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def kzz(mat_id, *value):
        '''Thermal conductivity (also KXX, KYY)'''
        return f"MP,KZZ,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def lsst(mat_id, *value):
        '''Electric loss tangent'''
        return f"MP,LSST,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def lssm(mat_id, *value):
        '''Magnetic loss tangent'''
        return f"MP,LSSM,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def mgxx(mat_id, *value):
        '''Magnetic coercive forces (also MGYY, MGZZ)'''
        return f"MP,MGXX,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def mgyy(mat_id, *value):
        '''Magnetic coercive forces (also MGXX, MGZZ)'''
        return f"MP,MGYY,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def mgzz(mat_id, *value):
        '''Magnetic coercive forces (also MGXX, MGYY)'''
        return f"MP,MGZZ,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def murx(mat_id, *value):
        '''Magnetic coercive forces (also MGYY, MGZZ)'''
        return f"MP,MURX,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def mury(mat_id, *value):
        '''Magnetic coercive forces (also MGXX, MGZZ)'''
        return f"MP,MURY,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def murz(mat_id, *value):
        '''Magnetic coercive forces (also MGXX, MGYY)'''
        return f"MP,MURZ,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def mu(mat_id, *value):
        '''Coefficient of friction'''
        return f"MP,MU,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def nuxy(mat_id, *value):
        '''Minor Poisson's ratios (also NUYZ, NUXZ) '''
        return f"MP,NUXY,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def nuyz(mat_id, *value):
        '''Minor Poisson's ratios (also NUXY, NUXZ) '''
        return f"MP,NUYZ,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def nuxz(mat_id, *value):
        '''Minor Poisson's ratios (also NUXY, NUYZ) '''
        return f"MP,NUXZ,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def perx(mat_id, *value):
        '''Electric relative permittivities (also PERY, PERZ)'''
        return f"MP,PERX,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def pery(mat_id, *value):
        '''Electric relative permittivities (also PERX, PERZ)'''
        return f"MP,PERY,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def perz(mat_id, *value):
        '''Electric relative permittivities (also PERX, PERY)'''
        return f"MP,PERZ,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def prxy(mat_id, *value):
        '''Major Poisson's ratios (also PRYZ, PRXZ)'''
        return f"MP,PRXY,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def pryz(mat_id, *value):
        '''Major Poisson's ratios (also PRXY, PRXZ)'''
        return f"MP,PRYZ,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def prxz(mat_id, *value):
        '''Major Poisson's ratios (also PRXY, PRYZ)'''
        return f"MP,PRXZ,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def qrate(mat_id, *value):
        '''Heat generation rate for thermal mass element MASS71. Fraction of plastic work converted to heat (Taylor-Quinney coefficient) for coupled-field elements PLANE222, PLANE223, SOLID226, and SOLID227.'''
        return f"MP,QRATE,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def reft(mat_id, *value):
        '''Reference temperature. Must be defined as a constant; C1 through C4 are ignored.'''
        return f"MP,REFT,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def rh(mat_id, *value):
        '''Hall Coefficient.'''
        return f"MP,RH,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def rsvx(mat_id, *value):
        '''Electrical resistivities (also RSVY, RSVZ).'''
        return f"MP,RSVX,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def rsvy(mat_id, *value):
        '''Electrical resistivities (also RSVX, RSVZ).'''
        return f"MP,RSVY,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def rsvz(mat_id, *value):
        '''Electrical resistivities (also RSVX, RSVY).'''
        return f"MP,RSVZ,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def sbkx(mat_id, *value):
        '''Seebeck coefficients (also SBKY, SBKZ).'''
        return f"MP,SBKX,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def sbky(mat_id, *value):
        '''Seebeck coefficients (also SBKX, SBKZ).'''
        return f"MP,SBKY,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def sbkz(mat_id, *value):
        '''Seebeck coefficients (also SBKX, SBKY).'''
        return f"MP,SBKZ,{mat_id},{','.join([str(i) for i in value])}"

    @staticmethod
    def sonc(mat_id, *value):
        '''Sonic velocity.'''
        return f"MP,SONC,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def thsx(mat_id, *value):
        '''Thermal strain (also THSY, THSZ).'''
        return f"MP,THSX,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def thsy(mat_id, *value):
        '''Thermal strain (also THSX, THSZ).'''
        return f"MP,THSY,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def thsz(mat_id, *value):
        '''Thermal strain (also THSX, THSY).'''
        return f"MP,THSZ,{mat_id},{','.join([str(i) for i in value])}"
    
    @staticmethod
    def visc(mat_id, *value):
        '''Viscosity.'''
        return f"MP,VISC,{mat_id},{','.join([str(i) for i in value])}"