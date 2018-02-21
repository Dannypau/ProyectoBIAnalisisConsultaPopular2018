from textblob.classifiers import NaiveBayesClassifier

ftrain=open('E:\\semestre2017B\\bi\\proyectoFinalGithub\\proyectoFinal\\clasificador\\pruebaClasificadorTrain.json', 'r')

cl = NaiveBayesClassifier(ftrain,format="json")
ftrain.close
print('trained')
ftest=open('E:\\semestre2017B\\bi\\proyectoFinalGithub\\proyectoFinal\\clasificador\\pruebaClasificadorTest.json','r')

a=cl.accuracy(ftest, format="json")
ftest.close
print ('Accuracy:')
print(a)
resultado=cl.classify("en la consulta al traidor diles no")
print resultado
print(cl.show_informative_features(10))
