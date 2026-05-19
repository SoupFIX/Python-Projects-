"""
Utility functions for Titanic Survival Prediction Model
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    roc_curve,
    auc,)
from sklearn.model_selection import cross_val_score

#============================================================
# data Loading
def load_data(filepath = 'Data/titanic_data.csv'):
    df = pd.read_csv(filepath)
    return df
#============================================================
# Feature Engineering

def extract_title(name):
    """
    Extract the title(Mr,Ms,Mrs,Miss,Master ,etc.)
    from a passengre name.
    """
    title = name.split(',')[1].split('.')[0].strip()
    return title

def create_features(df):
    df = df.copy()
    df['Title'] = df['Name'].apply(extract_title)
    rare_title = df['Title'].value_counts()
    rare_title = rare_title[rare_title<10].index.tolist()
    df['Title'] = df['Title'].replace(rare_title,'Rare')

# Family Size
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1 # count ownself
    df['IsAlone'] = (df['FamilySize']==1).astype(int)

    df['AgeGroup'] = pd.cut(df['Age'],bins = [0,12,18,35,60,80],labels = ['child','Teen','Young Adult','Adult','Senior'])
    
    df['FareBin'] = pd.qcut(df['Fare'],q=4,labels = ['Low','Medium','High','Very High'])
    return df

def preprocess_data(df):
    df = df.copy()
    
    df['Age'] = df.groupby(['Pclass','Sex'])['Age'].transform(lambda x:x.fillna(x.median()))
    df['Age'] = df['Age'].fillna(df['Age'].median())

    #Embarked with mode
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

    # Filling Fares with Median
    df['Fare'] = df['Fare'].fillna(df['Fare'].median())

    # Dropping Useless columns :
    drop_cols = ['cabin','Name','Ticket' ,'PassengerId']
    df = df.drop(columns = [c for c in drop_cols if c in df.columns])

    # Encode Sex Column
    df['Sex'] = df['Sex'].map({'male' : 0,'female' : 1})

    if 'Title' in df.columns:
        df = pd.get_dummies(df,columns = ['Title'],drop_first = True,dtype = int)

    for col in ["AgeGroup", "FareBin"]:
        if col in df.columns:
            df = pd.get_dummies(df, columns=[col], drop_first=True, dtype=int)
    return df

def evaluate_model(y_true,y_pred,model_name = 'Model'):
    """
    Prints Classification Metrix and returns them as a dict. 
    """
    metrics = {
              'Model' : model_name,
              'Accuracy':  accuracy_score(y_true,y_pred),
              'Precision' : precision_score(y_true,y_pred),
              'Recall' : recall_score(y_true,y_pred),
              'F1 Score': f1_score(y_true,y_pred),
              }
    print(40*'=')
    print(f'{model_name} Results : ')
    print(40*'=')
    print(f'MODEL     : {metrics['Model']}' )
    print(f'ACCURACY  : {metrics['Accuracy']}')
    print(f'PRECISION : {metrics['Precision']}')
    print(f'RECALL    : {metrics['Recall']}')
    print(f'F1 SCORE  : {metrics['F1 Score']}')
def plot_confusion_matrix(y_true,y_pred,model_name = 'Model'):
    """
    plot a styled confusion matrix heatmap.
    """
    cm = confusion_matrix(y_true,y_pred)
    plt.figure(figsize = (6,4))
    sns.heatmap(cm,annot = True,fmt = 'd',cmap = 'Blues',xticklabels = ['Did not survived','Survived'],yticklabels = ['Did not survived','Survived'],)
    plt.title(f'Confusion Matrix : {model_name}')
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.show()

def plot_roc_curves(models_dict,X_test,y_test):
    """
    Plot ROC Curves for multiple models on the same figure.
    Parameters:
    models_dict : dict of {model_name : fitted_model}
    X_test : test features
    y_test : test labels
    """
    plt.figure(figsize = (8,6))

    for name,model in models_dict.items():
        if hasattr(model,"predict_proba"):
            y_prob = model.predict_proba(X_test)[:,1]
        else:
            y_prob = model.decision_function(X_test)
        fpr,tpr,_ = roc_curve(y_test,y_prob)
        roc_auc = auc(fpr,tpr)
        plt.plot(fpr,tpr,label = f"{name}")

    plt.plot([0,1],[0,1],'k--',label = 'Random (AUC = 0.500)')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve Comparision')
    plt.tight_layout()
    plt.show()



def cross_validate_model(model,X,y,cv=5):
    """
    Run cross-validation and print mean/std accuracy.
    """
    scores = cross_val_score(model,X,y,cv = cv,scoring = 'accuracy')
    print(f"Cross-Validation Accuracy: {scores.mean():.4f} (+/- {scores.std():.4f})")
    return scores


def compare_models(results_list):
    """
    Take a list of metric dicts from evaluate_model() and return
    a comparison DataFrame sorted by F1 Score.
    """
    df = pd.DataFrame(results_list)
    df = df.sort_values("F1 Score", ascending=False).reset_index(drop=True)
    return df