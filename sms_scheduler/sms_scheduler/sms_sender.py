
import requests
import json



class SMSSender(object):
  """
    to send sms we are creating sms sender
  """
  def __init__(self):
    super(SMSSender, self).__init__()
    self.URL = 'http://www.way2sms.com/api/v1/sendCampaign'
    self.api_key ='SXW0VDWCUUGMAW3IT3KPCKO8CMIJS5FA'
    self.secret_key = 'R9TU8A7WWVZ93G9I'
    self.useType = 'test'
    self.senderid = ''
    

  #If i create a app i will take all this from settings file
  def send_post_req(self,phoneno,msg):
    req_params = {
        'apikey':self.apiKey,
        'secret':self.secretKey,
        'usetype':self.useType,
        'senderid':self.senderId,
        'phone': phoneno,
        'message':msg
    }
    try:
      requests.post(reqUrl, req_params)
    except execption as e:

