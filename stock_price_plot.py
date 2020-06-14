import pandas as pd  # file reader
import matplotlib.pyplot as plt  # plot tool
plt.style.use('ggplot') # plot style

data_file = pd.read_csv('TSLA.csv')
print('########## Welcome to Tesla stock generator ########## \n')
print('########## TESTING FILE ########## \n '
      'Showing the first 6 data on the file \n')
print(data_file.head(6))
print('########## TESTING COMPLETE ########## \n')
print('The total number of rows and columns of the file: ')
print(data_file.shape)

print('The most recent Tesla stock price is:')
print(data_file.tail(1))

plt.figure(figsize=(16,8))
plt.title('TESLA')
plt.xlabel('Days')
plt.ylabel('Close Price USD ($)')
plt.plot(data_file['Close'])
plt.show()  # show the plot


