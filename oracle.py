import json, random
def dec(n, p=2):
    b = 10**p
    w, f = divmod(n, b)
    fs = str(f).zfill(p).rstrip("0")
    return str(w) + "." + fs if fs else str(w)
def m(n): return f"{n//100}.{str(n%100).zfill(2)}"
def pl(n, one, many): return f"{n}" + (one if n == 1 else many)
def v(n, one, many): return one if n == 1 else many
def boxes(n, b):
    k = -(-n//b)
    return f"The {pl(n,' mug',' mugs')} at {pl(b,' mug',' mugs')} a box {v(n,'takes','take')} {pl(k,' box',' boxes')}, the last box holding {pl(n-(k-1)*b,' mug',' mugs')}."
def weeks(n, w):
    k = n//w
    return f"The {pl(n,' mug',' mugs')} at {pl(w,' mug',' mugs')} a week {v(n,'lasts','last')} {pl(k,' full week',' full weeks')} with {pl(n-k*w,' mug',' mugs')} left for the next week."
def cost(b, pc, n):
    cc = b*pc
    pm = (2*cc + n)//(2*n)
    return f"The {pl(b,' box',' boxes')} at ${m(pc)} a box {v(b,'comes','come')} to ${m(cc)}, ${m(pm)} a mug."
def time_(n, pm):
    t = -(-n//pm); h, r = t//60, t%60
    return f"The {pl(n,' mug',' mugs')} at {pl(pm,' mug',' mugs')} a minute {v(n,'takes','take')} {pl(t,' minute',' minutes')}, {pl(h,' hour',' hours')} {pl(r,' minute',' minutes')}."
random.seed(778)
R = random.randint
cases = [
 dict(fn="boxes", args=["350","24"], expect=boxes(350,24)),
 dict(fn="weeks", args=["350","40"], expect=weeks(350,40)),
 dict(fn="cost", args=["15","38.50","350"], expect=cost(15,3850,350)),
 dict(fn="time", args=["350","6"], expect=time_(350,6)),
 dict(fn="boxes", args=["1","1"], expect=boxes(1,1)),
 dict(fn="boxes", args=["336","24"], expect=boxes(336,24)),
 dict(fn="boxes", args=["1000000","1000"], expect=boxes(1000000,1000)),
 dict(fn="weeks", args=["1","1"], expect=weeks(1,1)),
 dict(fn="weeks", args=["320","40"], expect=weeks(320,40)),
 dict(fn="weeks", args=["1000000","100000"], expect=weeks(1000000,100000)),
 dict(fn="cost", args=["1","0.01","1"], expect=cost(1,1,1)),
 dict(fn="cost", args=["100000","999.99","1000000"], expect=cost(100000,99999,1000000)),
 dict(fn="time", args=["1","1"], expect=time_(1,1)),
 dict(fn="time", args=["60","1"], expect=time_(60,1)),
 dict(fn="time", args=["1000000","100"], expect=time_(1000000,100)),
]
for _ in range(20):
    n,b=R(1,1000000),R(1,1000); cases.append(dict(fn="boxes", args=[str(n),str(b)], expect=boxes(n,b)))
for _ in range(20):
    n,w=R(1,1000000),R(1,100000); cases.append(dict(fn="weeks", args=[str(n),str(w)], expect=weeks(n,w)))
for _ in range(25):
    b,p,n=R(1,100000),R(1,99999),R(1,1000000); cases.append(dict(fn="cost", args=[str(b),dec(p),str(n)], expect=cost(b,p,n)))
for _ in range(19):
    n,m=R(1,1000000),R(1,100); cases.append(dict(fn="time", args=[str(n),str(m)], expect=time_(n,m)))
errs=[["boxes",["0","24"]],["boxes",["1000001","24"]],["boxes",["2.5","24"]],["boxes",["350","0"]],["boxes",["350","1001"]],
 ["weeks",["0","40"]],["weeks",["350","0"]],["weeks",["350","100001"]],["weeks",["350","1.5"]],["weeks",["1000001","40"]],
 ["cost",["0","38.50","350"]],["cost",["100001","38.50","350"]],["cost",["15","0","350"]],["cost",["15","38.505","350"]],["cost",["15","38.50","0"]],
 ["time",["0","6"]],["time",["350","0"]],["time",["350","101"]],["time",["350","6.5"]],["time",["1000001","6"]]]
json.dump(dict(cases=cases, errors=errs), open("expected.json","w"), indent=1)
print(len(cases),"cases,",len(errs),"errcases")
