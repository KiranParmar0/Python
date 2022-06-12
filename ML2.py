from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from  sklearn import tree
from sklearn.metrics import accuracy_score
#from sklearn.neighbors import KNeighborsClassifer
from sklearn.neighbors import KNeighborsClassifier
def MarvllousDecision():
    dataset = load_iris()
    data = dataset.data
    target = dataset.target
    
    data_train,data_test,target_train,target_test= train_test_split(data,target,test_size=0.5)
    
    cobj = tree.DecisionTreeClassifier()
    
    cobj.fit(data_train,target_train)
    
    output = cobj.predict(data_test)
    
    Accurcy = accuracy_score(target_test,output)
    return Accurcy
    
def MarvllousDecisionKNN():
    dataset = load_iris()
    data = dataset.data
    target = dataset.target
    
    data_train,data_test,target_train,target_test= train_test_split(data,target,test_size=0.5)
    
    cobj = KNeighborsClassifier()
    
    cobj.fit(data_train,target_train)
    
    output = cobj.predict(data_test)
    
    Accurcy = accuracy_score(target_test,output)
    return Accurcy    

def main():
    ret = MarvllousDecision()
    print("Accurcy of DecisionTree Algorithm is :",ret*100,"%")

    brt = MarvllousDecisionKNN()
    brt = print("Accurcy of KNN algorithm is :",brt*100,"%")

if __name__ == "__main__":
    main()

