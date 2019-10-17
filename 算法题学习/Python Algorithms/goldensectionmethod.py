# 使用最优化导论（第四版）例题进行验证
"""
使用MATLAB求解最小值点,验证压缩区间是否合理
f = @(x) (x^4-14*x^3+60*x^2-70*x)
[x, fval] = fminbnd(f,0,2)
"""



# --------------------------------------- #
def step2(a, b, my_lambda, miu, k, sigma):
    print("对应目标的函数值：",f(my_lambda), f(miu))
    if f(my_lambda) > f(miu):
        step3(a, b, my_lambda, miu, k, sigma)
    elif f(my_lambda) < f(miu):
        #
        step4(a, b, my_lambda, miu, k, sigma)


# --------------------------------------- #
def step3(a, b, my_lambda, miu, k, sigma):
    if (b - my_lambda) < sigma:
        print(f"压缩结果[{my_lambda},{b}],迭代{k}次")
        # print("over??")
        # stop
        return None
    else:
        a = my_lambda
        my_lambda = miu
        miu = a + 0.618 * (b - a)
        step5(a, b, my_lambda, miu, k, sigma)

# --------------------------------------- #
def step4(a, b, my_lambda, miu, k, sigma):
    if (miu - a) < sigma:
        print(f"压缩结果[{a},{miu}],迭代{k}次")
        
        # print("??")
        return None
    else:
    
        b = miu
        miu = my_lambda
        my_lambda = a + 0.382 * (b - a)
        
        step5(a, b, my_lambda, miu, k, sigma)

# --------------------------------------- #
def step5(a, b, my_lambda, miu, k, sigma):
    k = k + 1
    step2(a, b, my_lambda, miu, k, sigma)


def f(x):
    # y = x^4-14*x^3+60*x^2-70*x;
    return x**4-14*x**3+60*x**2-70*x

def step1():
    a, b = 0, 2  # [0,2]闭区间
    # 将极小值点所在区间的长度压缩到sigma之内，精度要求：sigma
    sigma = 0.3
    k = 1
    my_lambda = a + 0.382 * (b - a)
    miu = a + 0.618 * (b - a)
    print(my_lambda, miu)
    
    step2(a, b, my_lambda, miu, k, sigma)
    #

if __name__ == '__main__':
    step1()