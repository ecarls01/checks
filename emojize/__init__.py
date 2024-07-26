import check50
import check50.py
import emoji

@check50.check()
def exists():
    """Check that emojize.py exists """
    check50.exists("emojize.py")


@check50.check(exists)
def run():
    """ File runs without syntax errors"""
    check50.py.compile("emojize.py")


@check50.check(run)

def index1():
    """ input of :1st_place_medal yields correct output""""
    out = check50.run("python emojize.py").stdin(":1st_place_medal").stdout(timeout=50)
    if out.strip() != emoji.emojize(":1st_place_medal:"):
        raise check50.Mismatch(emoji.emojize(":1st_place_medal:"), out.strip())

@check50.check(index1)

# def index2():
#     """ input of 0 yields output of 5"""
#     out = check50.run("python emojize.py").stdin("0").stdout(timeout=50)
#     if out.strip() != "5":
#         raise check50.Mismatch("5", out.strip())


# @check50.check(index2)
# def index3():
#     """ input of 4 yields output of pizza"""
#     out = check50.run("python emojize.py").stdin("4").stdout(timeout=50)
#     if out.strip() != "pizza":
#         raise check50.Mismatch("pizza", out.strip())

# @check50.check(index3)
# def index4():
#     """ input of 25 yields output of Index not valid for this list"""
#     out = check50.run("python emojize.py").stdin("25").stdout(timeout=50)
#     if out.strip() != "Index not valid for this list":
#         raise check50.Mismatch("Index not valid for this list", out.strip())
