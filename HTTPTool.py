import urllib.request

url = "http://hq.sinajs.cn/list=sz399006"

def GetSZIndex():
	res_data = urllib.request.urlopen(url)
	res = res_data.read()
	res =  res.decode("gb2312")
	return (res.split("\"")[1]).split(",")[3]

def GetCurDayRate():
	res_data = urllib.request.urlopen(url)
	res = res_data.read()
	res =  res.decode("gb2312")
	ck = float((res.split("\"")[1]).split(",")[2])
	c = float((res.split("\"")[1]).split(",")[3])
	return (c-ck)*1.0/ck
