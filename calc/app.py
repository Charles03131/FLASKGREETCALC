# Put your app in here.
from flask import Flask,request
from operations import add,subtract,mult,div

app=Flask(__name__)



@route('/add')
def use_add():
    """adds parameters a + b"""

    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    answer=add(a,b)

    return str(answer)





@route('/sub')
def use_sub():
    """subtracts peramaters b from a"""

    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    answer=sub(a,b)
    
    return str(answer)

@route('mult')
def use_mult():
    """multiplies parameters a * b"""

    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    answer=mult(a,b)

    return str(answer)


@route('div')
def use_div():

    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    answer=div(a,b)

    return str(answer)



operators={
    "add":add,
    "sub":sub,
    "mult":mult,
    "div":div,
}

@app.route("/math/<action>")
def use_math(action):
    """ use math ation on a and b"""

    a=int(request.args.get("a"))
    b=int(requst.args.get("b"))
    answer=operators[action](a,b)

    return str(answer)