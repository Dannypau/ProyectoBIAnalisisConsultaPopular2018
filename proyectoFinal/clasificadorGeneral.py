from textblob.classifiers import NaiveBayesClassifier

ftrain=open('E:\\pruebaClasificadorTrain.json', 'r')

cl = NaiveBayesClassifier(ftrain,format="json")
ftrain.close
print('trained')
ftest=open('E:\\pruebaClasificadorTest.json','r')

a=cl.accuracy(ftest, format="json")
ftest.close
print ('Accuracy:')
print(a)
resultado=cl.classify("diles no")
print resultado
print(cl.show_informative_features(5))
