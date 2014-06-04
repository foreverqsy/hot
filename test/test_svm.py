#encoding=utf8
import sys
sys.path.append('/Users/acmer/Desktop/hot/lib')
import svmMLiA as svm
import matplotlib
import matplotlib.pyplot as plt
from numpy import *


def testRbf(k1=100):
    dataArr,labelArr = svm.loadDataSet('../data/test1.txt')
    dataMat = mat(dataArr)
    #print dataMat
    b,alphas = svm.smoP(dataArr, labelArr, 200, 0.01, 10000, ('rbf', k1)) #C=200 important
    datMat=mat(dataArr); labelMat = mat(labelArr).transpose()
    #print alphas.A>0
    svInd=nonzero(alphas.A>0)[0]
    sVs=datMat[svInd] #get matrix of only support vectors
    #print dataMat
    #ax.scatter(sVs[:,0], sVs[:,1], s=30, c='green', marker='s')
    #ax.scatter(sVs[:,0], sVs[:,1])
    labelSV = labelMat[svInd];
    print "there are %d Support Vectors" % shape(sVs)[0]
    m,n = shape(datMat)
    errorCount = 0
    for i in range(m):
        kernelEval = svm.kernelTrans(sVs,datMat[i,:],('rbf', k1))
        predict=kernelEval.T * multiply(labelSV,alphas[svInd]) + b
        if sign(predict)!=sign(labelArr[i]): errorCount += 1
    print "the training error rate is: %f" % (float(errorCount)/m)
    dataArr,labelArr = svm.loadDataSet('../data/test2.txt')
    errorCount = 0
    datMat=mat(dataArr); labelMat = mat(labelArr).transpose()
    m,n = shape(datMat)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    #print sVs
    for i in range(m):
        kernelEval = svm.kernelTrans(sVs,datMat[i,:],('rbf', k1))
        predict=kernelEval.T * multiply(labelSV,alphas[svInd]) + b
        if sign(predict)!=sign(labelArr[i]): 
            errorCount += 1    
        if sign(predict) > 0:
            #c = [int((0.2/float(predict))) for cc in range(0, 60)]
            #ax.scatter(range(0, 60), array(datMat[i,:]), array(c), array(c))
            ax.scatter(range(0, 60), array(datMat[i,:]), s=20, c='green', marker='s')
            #print datMat[i,:], sign(predict), sign(labelArr[i])
            continue
        else:
            ax.scatter(range(0, 60), array(datMat[i,:]), s=20, c='red', marker='s')
            #print datMat[i,:], sign(predict), sign(labelArr[i])
            continue
    for i in range(shape(sVs)[0]):
        ax.scatter(range(0, 60), array(sVs[i]), s=10, c='yellow', marker='s')
        continue
    plt.show()
    print "the test error rate is: %f" % (float(errorCount)/m)    

if __name__ == '__main__':
    testRbf()




