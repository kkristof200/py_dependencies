# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
import sys, subprocess

# Pip


# Local



# ---------------------------------------------------------------------------------------------------------------------------------------- #




# ------------------------------------------------------------- class: Utils ------------------------------------------------------------- #

class Utils:

    # ------------------------------------------------------ Public properties ------------------------------------------------------- #



    # -------------------------------------------------------- Public methods -------------------------------------------------------- #

    @classmethod
    def get_pip_info_str(cls, package_name: str) -> str:
        return cls.sh('{} -m pip show {}'.format(sys.executable, package_name))

    @staticmethod
    def sh(
        cmd: str,
        debug: bool = False
    ) -> str:
        if debug:
            print(cmd)

        return subprocess.getoutput(cmd)

    # ------------------------------------------------------ Private properties ------------------------------------------------------ #



    # ------------------------------------------------------- Private methods -------------------------------------------------------- #




# ---------------------------------------------------------------------------------------------------------------------------------------- #