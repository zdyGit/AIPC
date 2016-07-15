import urllib.request

url = "http://hq.sinajs.cn/list=sh000001"

def GetSZIndex():
	res_data = urllib.request.urlopen(url)
	res = res_data.read()
	res =  res.decode("gb2312")
	return (res.split("\"")[1]).split(",")[3]