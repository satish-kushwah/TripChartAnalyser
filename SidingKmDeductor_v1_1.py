def myfunction(tt):
  firstrow=4; BCGNrevCol=13; JPWrevCol=25; BCGNarrivalDutyCol=12; JPWarrivalDutyCol=22

  import pprint,openpyxl,os
  path=os.path.dirname(__file__)+"\\App_data\\"
  tripchart_path=os.path.dirname(__file__)+"\\tripchart_input\\"
  #tt=int(input('Enter 1 for WeekTT, 2 for SatTT, 3 for SunTT: '))
  if tt==1:
    from temp import WeekKmData
    d=WeekKmData.weekkms; dictname='weekkms'
    ctt=openpyxl.load_workbook(tripchart_path+'WEEK.xlsx') # excel file name
    f=open(path+'WeekKmData.py','w') # database name according to tt
  elif tt==2:
    from temp import SatKmData
    d=SatKmData.satkms; dictname='satkms'
    ctt=openpyxl.load_workbook(tripchart_path+'SAT.xlsx') # excel file name
    f=open(path+'SatKmData.py','w') # database name according to tt
  elif tt==3:
    from temp import SunKmData
    d=SunKmData.sunkms; dictname='sunkms'
    ctt=openpyxl.load_workbook(tripchart_path+'SUN.xlsx') # excel file name
    f=open(path+'SunKmData.py','w') # database name according to tt

  ttsheet=ctt.active
  totalrows=ttsheet.max_row
  print('Reading',totalrows,'rows\n')

  for i in range(firstrow,totalrows+1):
    if ttsheet.cell(row=i,column=BCGNrevCol).value!=None and ttsheet.cell(row=i,column=BCGNrevCol).value.strip()=='BCGN UP':
      dutyno=ttsheet.cell(row=i,column=BCGNarrivalDutyCol).value
      dutykm=d[dutyno]
      if dutykm not in ['KM data NA','Wrong Trips','All Trips NA','---']:
        d[dutyno]=str(round(float(dutykm)-0.8,1))
        print('0.8km deducted from duty no',dutyno)

    if ttsheet.cell(row=i,column=JPWrevCol).value!=None and ttsheet.cell(row=i,column=JPWrevCol).value.strip()=='JPW DN':
      dutyno=ttsheet.cell(row=i,column=JPWarrivalDutyCol).value
      dutykm=d[dutyno]
      if dutykm not in ['KM data NA','Wrong Trips','All Trips NA','---']:
        d[dutyno]=str(round(float(dutykm)-1.4,1))
        print('1.4km deducted from duty no',dutyno)

  f.write(dictname+'='+pprint.pformat(d)) 
  f.close()
  #input('\nKm data corrected successfully, press enter to exit')

if __name__ == "__main__":
  tt=int(input('Enter 1 for WeekTT, 2 for SatTT, 3 for SunTT: '))
  myfunction(tt)
  input('\nKm data corrected successfully, press enter to exit')