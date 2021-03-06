from  datetime  import  *
from  optparse  import  OptionParser
import XMLTool
import HTTPTool
import sys



BaseSZIndex = 0.00
BaseAccountSize = 0.00
RateExtr = 0.00
RateDiff = 0.00
DateDiff = 0

LastInDate = "2000-01-01"
LastInIndex = 0.00
curIndex = 0.00

def initSourceData():

	s = HTTPTool.GetSZIndex()
	XMLTool.SetKeyValue("curIndex",s)


	global BaseSZIndex
	BaseSZIndex = float(XMLTool.GetKeyValue("BaseSZIndex"))

	global BaseAccountSize
	BaseAccountSize = float(XMLTool.GetKeyValue("BaseAccountSize"))

	global RateExtr
	RateExtr = float(XMLTool.GetKeyValue("RateExtr"))

	global RateDiff
	RateDiff = float(XMLTool.GetKeyValue("RateDiff"))

	global DateDiff
	DateDiff = int(XMLTool.GetKeyValue("DateDiff"))

	global LastInDate
	LastInDate = XMLTool.GetKeyValue("LastInDate")

	global LastInIndex
	LastInIndex = float(XMLTool.GetKeyValue("LastInIndex"))

	global curIndex
	curIndex = float(XMLTool.GetKeyValue("curIndex"))

def ComputeCurrentAccount(LII,LID,CII):
	account = 0.00

	now = date.today()
	lastDate = datetime.strptime(LID,'%Y-%m-%d').date()
	ddiff = (now-lastDate).days

	rdiff = (CII-LII)*1.0/LII
	if rdiff<=0-RateDiff:
		account = HowMuchMoney(CII)
	else:
		if ddiff>=DateDiff:
			account = HowMuchMoney(CII)
		else:
			print("%d DAYS LEFT"%(DateDiff-ddiff))
	
	return account

def HowMuchMoney(CII):
	if CII>=BaseSZIndex:
		return BaseAccountSize
	account = ((BaseSZIndex-CII)*1.0*RateExtr/BaseSZIndex+1.0)*BaseAccountSize
	return account

def RegisterOption():
	parser = OptionParser()



def Main():
	CII = 2000
	while(CII>=1400):
		print(CII,Count(CII))
		CII = CII - 10
	return

	RegisterOption()

	now = datetime.now()
	dltime1 = now.replace(hour = 14,minute = 55,second = 0)
	dltime2 = now.replace(hour = 15,minute = 30,second = 0)


	usage = "usage: %prog [options] arg"
	parser = OptionParser(usage)
	parser.add_option("-c","--curIndex",action="store_true",dest="getCurIndex",help="get Current Index")
	parser.add_option("-g","--get",action="store_true",dest="getAccountOption",help="get current account over sz")
	parser.add_option("-s","--save",action="store_true",dest="saveCurIndexOption",help="save curindex after buyin")
	parser.add_option("-l","--lastInfo",action="store_true",dest="LastBuyinInfo",help="get Last Buyin Info")

	(options,args) = parser.parse_args()

	if options.getAccountOption == None and options.saveCurIndexOption == None and options.LastBuyinInfo == None and options.getCurIndex == None:
		print('args error , press -h for help')
		return

	if options.getAccountOption == True:
		if(now < dltime1):
			initSourceData()
			a = ComputeCurrentAccount(LastInIndex,LastInDate,curIndex)
			print("NOW IN : %.2f"%a)
		else:
			print("TIME PASS")
	if options.saveCurIndexOption == True:
		if(now > dltime2):
			s = HTTPTool.GetSZIndex()
			print("SZ : "+s)
			XMLTool.SetKeyValue("LastInIndex",s)
			now = date.today()
			s = now.strftime('%Y-%m-%d')
			print("DATE : " +s)
			XMLTool.SetKeyValue("LastInDate",s)
			print("SAVE SUCCESSFULLY ")
		else:
			print("TIME EARLY THAN 15:30")
	if options.LastBuyinInfo == True:
		print("LASTININDEX : "+XMLTool.GetKeyValue("LastInIndex"))
		print("LASTINDATE : "+XMLTool.GetKeyValue("LastInDate"))

	if options.getCurIndex == True:
		l = float(XMLTool.GetKeyValue("LastInIndex"))
		s = float(HTTPTool.GetSZIndex())
		d = float(HTTPTool.GetCurDayRate())
		print("CURRENTINDEX : %s (%.2f %%)[%.2f %%] "%(str(s),d*100,(s-l)*100/l))
		now = date.today()
		s = now.strftime('%Y-%m-%d')
		print("CURRENTDATE : " +s)


	

Main()