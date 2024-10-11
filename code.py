
import matplotlib.pyplot as plt
import functools 
import numpy as np
import math



def cricle_height_np(x):
    """ 
    the f(x) in the formula 
    """
    return np.sqrt(1-x**2)


# simplest
def RK1(func,h):
    """ 
    return integral from zero to one of given func
    func: a numpy-compatible funciton
    h: step_size
    """
    starts = np.arange(0,1,h)
    f = func(starts) 
    return f.sum()*h


def RK2(func,h):
    """ 
    return integral from zero to one of given func
    func: a numpy-compatible funciton
    h: step_size
    """
    starts = np.arange(0,1,h)
    ends =  starts + h
    f = func(starts) 
    s = f.sum() - f[0]/2
    return s*h


def RK4(func,h):
    """ 
    return integral from zero to one of given func
    func: a numpy-compatible funciton
    h: step_size
    """
    starts = np.arange(0,1,h)
    mid_points = starts + h/2
    ends = starts + h
    points_f = func(starts)
    mid_points_f = func(mid_points)
    s=0
    s += 2*points_f.sum() - points_f[0] # first and last points should be added only once
    s += 4*mid_points_f.sum()
    return s*h/6


def RK4_kutta(func, h):
    """ 
    return integral from zero to one of given func
    func: a numpyable funciton
    h: step_size
    """
    starts = np.arange(0,1,h)
    mid_1 = starts + h/3
    mid_2 = starts + h*2/3
    ends =  starts + h
    y1 = func(starts)
    y2 = func(mid_1)
    y3 = func(mid_2)
    #y4 = func(ends)
    return (2*y1.sum() - y1[0] + 3*(y2.sum()+y3.sum()))*h/8


def my_method(func,h):
    """ 
    return integral from zero to one of given func
    func: a numpyable funciton
    h: step_size
    """
    starts = np.arange(0,1,h)
    mids = starts + h/2
    ends =  starts + h
    f = func(starts) 
    f_m = func(mids) 
    # f_e = func(ends) 
    avg = f.sum() - f[0]/2 # this is equal to (f_start+f_end)/2
    s = h*avg
    s += h*((f_m.sum()-avg)*4)/6
    return s


def pi_error(method,h):
    h = 1/(int(1/h))
    print(h)
    return np.abs(method(cricle_height_np,h)*4 - math.pi)


pi_error_RK1 = functools.partial(pi_error,RK1)
pi_error_RK2 = functools.partial(pi_error,RK2)
pi_error_RK4 = functools.partial(pi_error,RK4)
pi_error_RK4_me = functools.partial(pi_error,my_method)
pi_error_RK4_kutta = functools.partial(pi_error,RK4_kutta)


n_iter = np.logspace(1,3,5)
step_size = 1/n_iter

errs_rk1 = list(map(pi_error_RK1, step_size))
errs_rk2 = list(map(pi_error_RK2, step_size))
errs_rk4 = list(map(pi_error_RK4, step_size))
errs_rk4_kutta= list(map(pi_error_RK4_kutta, step_size))
# errs_rk4_me = list(map(pi_error_RK4_me, step_size))

def plot(x,y):
    plt.plot(x,y,'o-')

plt.figure()
plot(n_iter,errs_rk1)
plot(n_iter,errs_rk2)
plot(n_iter,errs_rk4)
plot(n_iter,errs_rk4_kutta)
# plot(n_iter,errs_rk4_me) # this plot will be on the RK4
plt.legend([
    "RK1",
    "RK2",
    "RK4",
    "kutta-1991",
    # "my-parabolic-method",
])
plt.loglog()
plt.xlabel("number of steps (1/h)")
plt.ylabel("error")
plt.savefig("result.jpg")
plt.show()

