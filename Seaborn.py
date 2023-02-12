import seaborn as sns
import  matplotlib.pyplot as plt
import pandas as pd

def main():
    df  = sns.load_dataset("tips")
    print(df)
    print(df.boxplot(by = 'day' , column= ['total_bill'] , grid= False))

    titanic = sns.load_dataset("titanic")
    print(titanic.head())
    age1 = titanic['age'].dropna()
    #sns.displot(age1 , bins = 30 , kde = False)

    data = sns.load_dataset("mpg")
    print(data.head())

    sns.regplot(x='mpg' , y='acceleration' , data = data)

    plt.show()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
