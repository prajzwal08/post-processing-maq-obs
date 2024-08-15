#Load modules

import datetime as dt
from fetch_data import *
import os 

output_file_path = "/home/khanalp/data/fluxsites_NL/incoming/veenkampen"

#User defined input, specify your wishes below
site = 1       
# These are variables in 1 mins resolution.                              #Site 1=Veenkampen, 2=Loobos, 3=Amsterdam
# variables = ['SW_IN_1_1_1',
#              'LW_IN_1_1_1',
#              'P_1_1_7',
#              'RN_1_1_1',
#              'G_1_1_1',
#              'G_2_1_1', 
#              'G_3_1_1', 
#              'G_4_1_1',
#              'TS_1_1_1', 
#              'TS_1_2_1',
#              'TS_1_3_1', 
#              'TS_1_4_1',
#              'TS_1_5_1', 
#              'TS_1_6_1', 
#              'TS_2_1_1', 
#              'TS_2_2_1',
#              'TS_2_3_1', 
#              'TS_2_4_1',
#              'VWC_1_1_1', 
#              'VWC_1_2_1', 
#              'VWC_1_3_1',
#              'VWC_1_4_1',
#              'VWC_2_1_1',
#              'VWC_2_2_1',
#              'VWC_2_3_1',
#              'VWC_2_4_1',
            #  'VWC_3_1_1'  ] 
 
 #These are variables in 30 mins resolution directly available. 
variables = ['air_temperature',
             'VPD',
             'air_pressure',
            'wind_speed',
            'co2_mole_fraction',
            'RH',
            'specific_humidity',
            'H',
            'qc_H',
            'LE',
            'qc_LE',
            'co2_flux',
            'qc_co2_flux'
 ]
                                            
API_KEY = <>                            #Put you API key here as a string, see https://maq-observations.nl/api/

#Run the request
start_year = 2012
end_year = 2023          #End date (yyyy,mm,dd)
for year in range(start_year, end_year + 1):
    for month in range(1, 13):
        start_date = dt.datetime(year, month, 1)
        # Determine the last day of the month
        if month == 12:
            end_date = dt.datetime(year + 1, 1, 1) - dt.timedelta(days=1)
        else:
            end_date = dt.datetime(year, month + 1, 1) - dt.timedelta(days=1)
        
        # Define a unique filename for each month's data
        save_filename = os.path.join(output_file_path,f'MAQ-data_veenkampen_30mins_{year}_{month:02}.csv')
        
        # Run the request
        fetch_data(start_date, end_date, site, variables, API_KEY, True, save_filename)

