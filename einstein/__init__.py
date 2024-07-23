import check50
import check50.py


@check50.check()
def exists():
    """Carlson - Check that einstein.py exists """
    check50.exists("einstein.py")


@check50.check(exists)
def run():
    """ File runs without syntax errors"""
    check50.py.compile("einstein.py")


@check50.check(run)
def importlater():
    """ No import statements allowed in this program """

    # Read in the file
    with open('einstein.py', 'r') as file:
        filedata = file.read()

    import_pos = filedata.count("import")

    if import_pos > 0:
        raise check50.Failure("Your program imports packages when it should not", \
                              help="Remove any import statements and resubmit")


@check50.check(importlater)
def einstein1():
    """ The energy is correct for 1 kg """
    out = check50.run("python einstein.py").stdin("1").stdout(timeout=50)
    if out.strip() != "90000000000000000":
        raise check50.Mismatch("90000000000000000", out.strip())


@check50.check(importlater)
def einstein2():
    """ The energy is correct for 14 kg """
    out = check50.run("python einstein.py").stdin("14").stdout(timeout=50)
    if out.strip() != "1260000000000000000":
        raise check50.Mismatch("1260000000000000000", out.strip())


@check50.check(importlater)
def einstein3():
    """ The energy is correct for 50 kg """
    out = check50.run("python einstein.py").stdin("50").stdout(timeout=50)
    if out.strip() != "4500000000000000000":
        raise check50.Mismatch("4500000000000000000", out.strip())