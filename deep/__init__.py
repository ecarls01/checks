import check50
import check50.py


@check50.check()
def exists():
    """Carlson - Check that deep.py exists """
    check50.exists("deep.py")


@check50.check(exists)
def run():
    """ File runs without syntax errors"""
    check50.py.compile("deep.py")


@check50.check(run)
def importlater():
    """ No import statements allowed in this program """

    # Read in the file
    with open('deep.py', 'r') as file:
        filedata = file.read()

    import_pos = filedata.count("import")

    if import_pos > 0:
        raise check50.Failure("Your program imports packages when it should not", \
                              help="Remove any import statements and resubmit")


@check50.check(importlater)
def deep1():
    """ input of 42 yields output of Yes"""
    out = check50.run("python deep.py").stdin("42").stdout(timeout=50)
    if out.strip() != "Yes":
        raise check50.Mismatch("Yes", out.strip())

def deep2():
    """ input of forty-two yields output of Yes"""
    out = check50.run("python deep.py").stdin("forty-two").stdout(timeout=50)
    if out.strip() != "Yes":
        raise check50.Mismatch("Yes", out.strip())

def deep3():
    """ input of forty two yields output of Yes"""
    out = check50.run("python deep.py").stdin("forty two").stdout(timeout=50)
    if out.strip() != "Yes":
        raise check50.Mismatch("Yes", out.strip())
    
def deep3():
    """ input of FoRty TwO yields output of Yes"""
    out = check50.run("python deep.py").stdin("FoRty TwO").stdout(timeout=50)
    if out.strip() != "Yes":
        raise check50.Mismatch("Yes", out.strip())
    

def deep4():
    """ input of 42 (with spaces on either side) yields output of Yes"""
    out = check50.run("python deep.py").stdin("    42    ").stdout(timeout=50)
    if out.strip() != "Yes":
        raise check50.Mismatch("Yes", out.strip())
    
def deep5():
    """ input of 50 yields output of No"""
    out = check50.run("python deep.py").stdin("No").stdout(timeout=50)
    if out.strip() != "No":
        raise check50.Mismatch("No", out.strip())

    
def deep6():
    """ input of fifty yields output of No"""
    out = check50.run("python deep.py").stdin("No").stdout(timeout=50)
    if out.strip() != "No":
        raise check50.Mismatch("No", out.strip())
