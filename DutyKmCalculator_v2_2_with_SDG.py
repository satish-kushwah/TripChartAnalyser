import os
temp_path=os.path.dirname(__file__)+"\\temp\\"
def myfunction(tt):
	import pprint
	#tt=int(input('Enter 1 for WeekTT, 2 for SatTT, 3 for SunTT: '))
	if tt==1:
		from temp import WeekTripsData
		d=WeekTripsData.weektrips; filename='WeekKmData.py' ; dictname='weekkms'
	elif tt==2:
		from temp import SatTripsData
		d=SatTripsData.sattrips; filename='SatKmData.py' ; dictname='satkms'
	elif tt==3:
		from temp import SunTripsData
		d=SunTripsData.suntrips; filename='SunKmData.py' ; dictname='sunkms'

	#totalduties=int(input('Enter total no of duties: '))
	totalduties=len(d)
	d1={}
	for i in range(totalduties):
		goahead=1
		if len(d[i+1])==0:
			d1[i+1]='---'; goahead=0
		elif (len(d[i+1])%2)!=0:
			d1[i+1]='All Trips NA'; goahead=0
		else:
			for x in range(int(len(d[i+1])/2)):
				if d[i+1][x*2][0]!='Board' and d[i+1][x*2+1][0]!='Deboard':
					d1[i+1]='Wrong Trips'; goahead=0; break
		if goahead==1:
			dutykm=0; kmcal=1
			for j in range(int(len(d[i+1])/2)):
				#from OKNS to OKNS
				if d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='UP  UP  ':
					dutykm+=74.4
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='UP  DOWN':
					dutykm+=52.2
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='DOWNDOWN':
					dutykm+=74.4
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='DOWNUP  ':
					dutykm+=22.2
				#from Depot to OKNS and viceversa
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='KKD_JDUP  ':
					dutykm+=18.6
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='KKD_JUUP  ':
					dutykm+=6.6
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='KKD_JDDOWN':
					dutykm+=70.8
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='KKD_JUDOWN':
					dutykm+=58.8
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='UP  KKD_JD':
					dutykm+=58.8
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='UP  KKD_JU':
					dutykm+=70.8
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='DOWNKKD_JD':
					dutykm+=6.6
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='DOWNKKD_JU':
					dutykm+=18.6
				#from OKNS to other than Depot
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='UP  IWNR DN':
					dutykm+=53.3
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='DOWNIWNR DN': #after full trip
					dutykm+=75.5
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='UP  OVA DN':
					dutykm+=55.6
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='DOWNOVA DN':  #after full trip
					dutykm+=77.8
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='UP  JLA DN':
					dutykm+=57.3
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='UP  KIKJ UP':
					dutykm+=67.3
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='DOWNKIKJ UP':
					dutykm+=15.1
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='UP  BCGN DN':
					dutykm+=62.9
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='DOWNBCGN DN':
					dutykm+=10.7
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='UP  BCGN DN SDG':
					dutykm+=63.3
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='DOWNBCGN DN SDG':
					dutykm+=11.1
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='UP  BCGN UP SDG':
					dutykm+=63.3
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='DOWNBCGN UP SDG':
					dutykm+=11.1
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='UP  JPW UP SDG':
					dutykm+=26.1
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='UP  JPW DN SDG':
					dutykm+=26.1
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='DOWNJPW DN SDG':
					dutykm+=48.3
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='DOWNJPW UP SDG':
					dutykm+=48.3
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='UP  JPW UP':
					dutykm+=25.4
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='UP  JPW DN':
					dutykm+=25.4
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='DOWNJPW DN':
					dutykm+=47.6
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='DOWNJPW UP':
					dutykm+=47.6
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='DOWNKJMD DN':
					dutykm+=73.4
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='DOWNKJMD UP':
					dutykm+=23.2
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='UP  KJMD DN':
					dutykm+=51.2
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='UP  KJMD UP':
					dutykm+=75.4
				#from other than Depot to OKNS
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='IWNR DNUP  ':
					dutykm+=21.1
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='IWNR DNDOWN':
					dutykm+=73.3
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='OVA DNUP  ':
					dutykm+=18.8
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='OVA DNDOWN':
					dutykm+=71
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='JLA DNUP  ':
					dutykm+=17.1
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='JLA DNDOWN':
					dutykm+=69.3
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='KIKJ UPUP  ':
					dutykm+=7.1
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='KIKJ UPDOWN':
					dutykm+=59.3
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='BCGN DNUP  ':
					dutykm+=11.5
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='BCGN DNDOWN':
					dutykm+=63.7
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='BCGN DN SDGUP  ':
					dutykm+=11.1
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='BCGN DN SDGDOWN':
					dutykm+=63.3
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='BCGN UP SDGUP  ':
					dutykm+=11.1
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='BCGN UP SDGDOWN':
					dutykm+=63.3
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='JPW UP SDGUP  ':
					dutykm+=48.3
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='JPW DN SDGUP  ':
					dutykm+=48.3
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='JPW DN SDGDOWN':
					dutykm+=26.1
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='JPW UP SDGDOWN':
					dutykm+=26.1
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='JPW UPUP  ':
					dutykm+=47.6
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='JPW DNUP  ':
					dutykm+=47.6
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='JPW DNDOWN':
					dutykm+=25.4
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='JPW UPDOWN':
					dutykm+=25.4
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='KJMD DNDOWN':
					dutykm+=75.4
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='KJMD DNUP  ':
					dutykm+=23.2
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='KJMD UPUP  ':
					dutykm+=73.4
				elif d[i+1][j*2][1].split('/')[1]+d[i+1][j*2+1][1].split('/')[1]=='KJMD UPDOWN':
					dutykm+=51.2
				
				else:
					kmcal=0
					break
			d1[i+1]=str(round(dutykm,1))
			if kmcal==0:
				d1[i+1]='KM data NA'
	fp=open(temp_path+ filename,'w')
	fp.write(dictname+'='+pprint.pformat(d1))
	fp.close()
	#input('Km calculated successfully, press enter to exit')

if __name__ == "__main__":
	tt=int(input('Enter 1 for WeekTT, 2 for SatTT, 3 for SunTT: '))
	myfunction(tt)
	input('Km calculated successfully, press enter to exit')