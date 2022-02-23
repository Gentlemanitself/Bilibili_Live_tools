import aiohttp
def sc_send(self, sc_title: str = '', sc_desp: str = '', text: str = '') -> list:
    sc_desp = sc_desp or text
    sc_data = {'summary': sc_title, 'content': sc_desp, 'contentType':1,'topicIds': [1545],"url": "https://live.bilibili.com/11680300"}
    async with aiohttp.ClientSession() as session:
        for a in [0, 1, 2]:
            try:
                session.post(url='http://wxpusher.zjiecode.com/api/send/message' % self.sc_token, data=sc_data)
                return ['success', True]
            except:
                pass
    return ['sc', False]