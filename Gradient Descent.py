import numpy as np
import random
import sklearn
import pylab

from scipy import stats
from sklearn.datasets.samples_generator import make_regression

def gradient_descent(alpha, x, y, ep, max_iter):
    converged = False
    iterations = 0
    m = x.shape[0]
    print "m is %s" %(m)

    # initial theta
    theta0 = np.random.random(x.shape[1])
    theta1 = np.random.random(x.shape[1])
    print "theta0 is %s, theta1 is %s" %(theta0, theta1)

    # total error, J(theta)
    # J(theta) = 1/2m * sum(theta0 + theta1 * xi - yi)^2
    J = sum([(theta0 + theta1 * x[i] - y[i])**2 for i in range(m)])
    print "J is %s" %(J)

    cost_f = []
    cost_f.append(J)
    # iterate
    while not converged:
        # derivative of theta0
        # 1/m * sum(theta0 + theta1 * xi - yi)
        # derivative of theta1
        # 1/m * sum(theta0 + theta1 * xi - yi) * xi
        gradient0 = 1.0 / m * sum([(theta0 + theta1 * x[i] - y[i]) for i in range(m)])
        gradient1 = 1.0 / m * sum([(theta0 + theta1 * x[i] - y[i]) * x[i] for i in range(m)])

        # updating theta
        theta0 = theta0 - alpha * gradient0
        theta1 = theta1 - alpha * gradient1

        # mean squared error
        err = sum([(theta0 + theta1 * x[i] - y[i]) ** 2 for i in range(m)])
        print "Convergence Error: %s " %(abs(J - err))
        if abs(J - err) <= ep:
            print 'Total Iterations: %s' %(iterations)
            converged = True

        J = err
        cost_f.append(J)
        iterations += 1

        if iterations == max_iter:
            print "Max iterations reached"
            converged = True

    print "theta 0 is %s" %(theta0)
    print "theta 1 is %s" %(theta1)
    return theta0, theta1, cost_f

def create_regression():
    x, y = make_regression(
        n_samples=100,
        n_features=1,
        n_informative=1,
        random_state=0,
        noise=35
    )

    # learning rate
    alpha = 1
    # convergence criteria
    ep = 1e-12
    # max iterations
    max_iter = 20

    theta0, theta1, cost_f = gradient_descent(alpha, x, y, ep, max_iter)

    slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x[:, 0], y)
    print ('intercept = %s slope = %s') % (intercept, slope)

    for i in range(x.shape[0]):
        y_predict = theta0 + theta1 * x

    pylab.plot(x, y, 'o')
    pylab.plot(x, y_predict, '-')
    pylab.show()
    print "Done."

if __name__ == '__main__':
    create_regression()
