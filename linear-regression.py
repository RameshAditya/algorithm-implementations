#Import necessary modules
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import pandas
import datetime
import quandl

class customlinearregression():

    def __init__(self):
        self.intercept=0
        self.slope=0

    #Function to calculate mean of a parameter array 'dim'
    def am(self, dim):
        tot=0.0
        for i in dim:
            tot+=i
        return tot/len(dim)

    #Function to calculate slope of the line of best fit using statistical formula
    def best_fit(self, dimOne, dimTwo):
        self.slope=( (self.am(dimOne)*self.am(dimTwo) - self.am(dimOne*dimTwo))/(-self.am(dimOne**2) + (self.am(dimOne))**2) )
        return self.slope

    #Function to determine y-intercept of line of best fit
    def y_intercept(self, dimOne, dimTwo):
        self.intercept=self.am(dimTwo) - self.am(dimOne)*self.slope
        return self.intercept

    #Function to generate co-ordinates of line of best fit
    def predict(self, ip):
        ip=np.array(ip)
        predicted=[self.slope*param + self.intercept for param in ip]
        return predicted

    #Function to calculate squared error
    def sq_error(self,original,model):
        return sum((original-model)**2)

    #Function to calculate coefficient of determination for R-squared model
    def cod(self,original,model):
        am_line=[self.am(original) for y in original]
        sq_err=self.sq_error(original,model)
        sq_err_am=self.sq_error(original,am_line)
        return 1-(sq_err/sq_err_am)

def main():
    #Acquire data
    stk=quandl.get("WIKI/TSLA")

    #Create class object
    simple_linear_regression=customlinearregression()

    #Reset dates
    stk=stk.reset_index()

    #Consider only necessary attributes
    stk=stk[['Date','Adj. Open','Adj. High','Adj. Low','Adj. Close','Volume']]

    #Typecast and convert to day numerical format
    stk['Date']=pandas.to_datetime(stk['Date'])
    stk['Date']=(stk['Date']-stk['Date'].min())/np.timedelta64(1,'D')

    #Identify actual output to regress against
    forecast_col='Adj. Close'

    #Fill in the holes
    stk.fillna(-999999, inplace=True)

    #Assign 'label' as title for comparator value
    stk['label']=stk[forecast_col]

    #Remove holes
    stk.dropna(inplace=True)

    #Take in the dates as variables
    x=np.array(stk['Date'])

    #Take in the prices as outputs
    y=np.array(stk['label'])

    #Generate line of best fit from these two
    slope=simple_linear_regression.best_fit(x,y)
    intercept=simple_linear_regression.y_intercept(x,y)

    #Acquire input day
    ip=list(map(int,input("Enter time to predict for:").split()))

    #Solve for value, store in 'line'
    line=simple_linear_regression.predict(ip)

    #Determine predicted values in line of best fit
    reg=[(slope*param)+intercept for param in x]

    #Display answer
    print("Predicted value after Linear Regression: ",line)

    #Calculate R-squared coefficient
    r_sqrd=simple_linear_regression.cod(y,reg)
    print("R^2 Value: ",r_sqrd)
    
    #Print and close
    plt.scatter(x,y)
    plt.scatter(ip,line,color="red")
    plt.plot(x,reg)
    plt.show()
    
if __name__=="__main__":
    main()
