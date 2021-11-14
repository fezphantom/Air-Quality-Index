import pandas as pd
import matplotlib.pyplot as plt


def preprocess(filename):
    hour_count = 24
    yearly_dict = {}
    for name in filename:
        print(f"Preprocessing aqi{str(name)}.csv")
        day_average_list = []
        for rows in pd.read_csv(f'Data/AQI/aqi{str(name)}.csv', chunksize=hour_count):
            day_total = 0
            day_avg = 0.0
            day_data = []
            df = pd.DataFrame(data=rows)
            for index, row in df.iterrows():
                day_data.append(row['PM2.5'])
            for val in day_data:
                if type(val) is float or type(val) is int:
                    day_total = day_total + val
                elif type(val) is str:
                    val = val.strip()
                    if val != 'NoData' and val != 'PwrFail' and val != '---' and val != 'InVld':
                        temp = float(val)
                        day_total = day_total + temp
            day_avg = (day_total / hour_count)
            day_average_list.append(day_avg)
            yearly_dict[name] = day_average_list
    return yearly_dict

def run_process():
    year = range(2013,2019)
    aqi_dict = preprocess(year)
    return aqi_dict
        
if __name__=="__main__":
    year = range(2013,2019)
    csv_dict = run_process()
    
    plt.plot(range(0,365),aqi_dict[2013],label="2013 data")
    plt.plot(range(0,364),aqi_dict[2014],label="2014 data")
    plt.plot(range(0,365),aqi_dict[2015],label="2015 data")
    plt.plot(range(0,365),aqi_dict[2016],label="2016 data")
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    plt.show()