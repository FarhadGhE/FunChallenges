datalist = [['a',[1]],['b',[2]],['c',[3]],['d',[4]],['e',[5]]]

def gossip(data):
    dataLength=len(data)
    print(data)
    if dataLength<=1:
        return data #lonely gossiper. no effect
    else:
        leftWing=gossip(data[0:int(dataLength/2)])
        rigthWing=gossip(data[int(dataLength/2):dataLength])
        result=shareNews(leftWing+rigthWing)
        return result

def shareNews(data):
    dataLength=len(data)
    #since every block of two people has already talked,
    #therefore each half of list, knows the same news.
    #So we need first news and last news to be complete
    news1=data[0][1] 
    news2=data[-1][1] 
    news=news1+news2
    for i in range(dataLength):
        data[i][1]=news
    return data


print(gossip(datalist))