import numpy as np 

''' 
Trend Indicators:  
'''
def get_moving_average(data, days):
    '''
    Returns a list with the values of the technical indicator Moving Average
    
    Parameters:
    - data: the stock Pandas dataset
    - days: the number of days taken into account for the calculation of the indicator.
    '''
    moving_average_list = []
    
    for i in range(days, data.shape[0]):  
        
        average = sum(data['Close'][i-days:i]) /days 
        
        moving_average_list.append(average)
        
    return moving_average_list

def get_exponential_moving_average(data, days):
    ''' 
    Returns a list with the values of the technical indicator Exponential Moving Average
    
    Parameters:
    - data: the stock Pandas dataset
    - days: the number of days taken into account for the calculation of the indicator.
    '''
    K = 2/(days + 1)
    
    exp_moving_average_list = []
    exp_moving_average_list.append(K * data['Close'][0])
    
    for i in range(1, data.shape[0]):
        previous_exp_moving_avg = exp_moving_average_list[i - 1]
        exp_moving_average = previous_exp_moving_avg + K*(data['Close'][i] - previous_exp_moving_avg)
        
        exp_moving_average_list.append(exp_moving_average)
        
    return exp_moving_average_list

def get_MACD(data):
    ''' 
    Returns a list with the values of the technical indicator Moving Average Convergence / Divergence
    
    Parameters:
    - data: the stock Pandas dataset 
    '''
    
    EMA12 = get_exponential_moving_average(data,12)
    EMA26 = get_exponential_moving_average(data,26)
    EMA12 = EMA12[len(EMA26)-len(EMA12):]
    
    MACD_list = []
    for i in range(len(EMA26)):
        MACD_list.append(EMA26[i] - EMA12[i])
        
    return MACD_list

'''
Moment Indicators:
'''
def get_RSI(data, days):
    ''' 
    Returns a list with the values of the technical indicator Relative Strength Index
    
    Parameters:
    - data: the stock Pandas dataset
    - days: the number of days taken into account for the calculation of the indicator.
    '''
    ifr_list = []
    for i in range(days, data.shape[0]):  
        low  = sum(data['Low'][i-days:i]) / days
        high = sum(data['High'][i-days:i]) / days
        
        rs = high / low
        ifr = 100 - (100 / (1 + rs))
        
        ifr_list.append(ifr)
        
    return ifr_list

def get_ROC(data, days):
    ''' 
    Returns a list with the values of the technical indicator Rate of Change
    
    Parameters:
    - data: the stock Pandas dataset
    - days: the number of days taken into account for the calculation of the indicator.
    '''
    roc_list = []
    for i in range(days, data.shape[0]):
        
        momentum = data['Close'][i] - data['Close'][i - days]
        roc = momentum / data['Close'][i - days]
        
        roc_list.append(roc)
        
    return roc_list

def get_stochastic_oscillatorK(data, days):
    ''' 
    Returns a list with the values of the technical indicator Stochastic oscillator K
    
    Parameters:
    - data: the stock Pandas dataset
    - days: the number of days taken into account for the calculation of the indicator.
    '''
    oscilatorK_list = []
    
    for i in range(days, data.shape[0]):
        minimum = min(data['Close'][i - days : i])
        maximum = max(data['Close'][i - days : i])
        close = data['Close'][i]
        
        k = (close - minimum) / (maximum - (minimum * 100))
        oscilatorK_list.append(k)
    
    return oscilatorK_list

def get_stochastic_oscillatorD(K_list):
    ''' 
    Returns a list with the values of the technical indicator Stochastic oscillator D
    
    Parameters:
    - K_list: List of the Stochastic oscillator K values
    '''
    oscilatorD_list = []
    for i in range(3, len(K_list)):
        
        average = sum(K_list[i - 3 : i]) / 3
        
        oscilatorD_list.append(average)
        
    return oscilatorD_list

'''
Volume Indicators:
'''
def get_OBV(data):
    ''' 
    Returns a list with the values of the technical indicator On Balance Volume
    
    Parameters:
    - data: the stock Pandas dataset 
    '''
 
    obv_list = []
    obv_list.append(0)
    
    for i in range(1, data.shape[0]):
        
        volume = 0
        if(data['Close'][i] > data['Close'][i - 1]):
            volume = data['Volume'][i]
            
        elif(data['Close'][i] < data['Close'][i - 1]):
            volume = - data['Volume'][i]
                
        previous_obv = obv_list[i - 1]
        
        obv_list.append(previous_obv + volume)
        
    
    return obv_list

'''
Volatility Indicators:
'''
def get_bollinger_band(data, days = 20, K = 2):
    '''
    Returns a tuple containing a list with the values of the upper band of the Bollinger Band technical indicator and
    a list with the lower band values of the same indicator.
    
    Parameters:
    - data: the stock Pandas dataset
    - days: the number of days taken into account for the calculation of the indicator.
    - K: multiplicative constant of the standard deviation
    '''
    
    MA = get_moving_average(data, days)
    
    upper_band = []
    lower_band = []
    
    for i in range(days, data.shape[0]):  
      
        std = np.array(data['Close'][i-days:i]).std()
          
        # (MA +− Kσ)
        upper_band.append(MA[i - days] + K*std)
        lower_band.append(MA[i - days] - K*std) 
    
    return (upper_band, lower_band)

