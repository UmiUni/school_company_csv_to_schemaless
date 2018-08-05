import http.client
import requests
import io
import csv

# Make sure to give the read permission to anyone having the link, otherwise our python program won't be able to read the file.
# First, we make a simple GET request on the export url of the spreadhseet using the requests module
headers={}
headers["User-Agent"]= "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0"
headers["DNT"]= "1"
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
headers["Accept-Encoding"] = "deflate"
headers["Accept-Language"]= "en-US,en;q=0.5"
lines = []

file_id     =  "19Y_Oi5_riecwonPbtxN4sfDntZO62s_vJbXoogFFp9o"
fortune_500 =  "1z1lsk2sjAPcxZ0nFInf2cReDjhKEc0bvCF8rch9Ev1Y"
url = "https://docs.google.com/spreadsheets/d/{0}/export?format=csv".format(fortune_500)

companyList = [] 

global companyListSize
def putCompaniesTest(num):
  curIndex = 0
  backFillCompanies(curIndex, num) 
 
def getCompaniesTest():
  r = requests.get(url)
  data = {}
  cols = []
  # Once we have the response, it is easy to read it using the csv module
  sio = io.StringIO( r.text, newline=None)
  reader = csv.reader(sio, dialect=csv.excel)
  rownum = 0
  
  for row in reader:
  # Do something with each row
    if rownum == 0:
      for col in row:
        data[col] = ''
        cols.append(col)
        print(col)
    else:
      i = 0
      for col in row:
        data[cols[i]] = col
        i = i +1
      index = data[cols[0]]
      company = data[cols[1]]
      domain = data[cols[2]][4:]
      #print(index)
      #print(company)
      #print(domain)
      tuple = [index, company, domain]
      lines.append(tuple) 
      companyList.append(tuple)
    rownum = rownum + 1
  global companyListSize
  companyListSize = rownum
  putCompaniesTest(50)


def getCompanies1():
  r = requests.get(url)
  data = {}
  cols = []
  # Once we have the response, it is easy to read it using the csv module
  sio = io.StringIO( r.text, newline=None)
  reader = csv.reader(sio, dialect=csv.excel)
  rownum = 0
  
  for row in reader:
  # Do something with each row
    if rownum == 0:
      for col in row:
        data[col] = ''
        cols.append(col)
        print(col)
    else:
      i = 0
      for col in row:
        data[cols[i]] = col
        i = i +1
      index = data[cols[0]]
      company = data[cols[1]]
      domain = data[cols[2]][4:]
      #print(index)
      #print(company)
      #print(domain)
      tuple = [index, company, domain]
      lines.append(tuple) 
      companyList.append(tuple)
    rownum = rownum + 1
  global companyListSize
  companyListSize = rownum
  putCompanies(100)

def getCompanies2():
  r = requests.get(url)
  data = {}
  cols = []
  # Once we have the response, it is easy to read it using the csv module
  sio = io.StringIO( r.text, newline=None)
  reader = csv.reader(sio, dialect=csv.excel)
  rownum = 0
  
  for row in reader:
  # Do something with each row
    if rownum == 0:
      for col in row:
        data[col] = ''
        cols.append(col)
        print(col)
    else:
      i = 0
      for col in row:
        data[cols[i]] = col
        i = i +1
      index = data[cols[0]]
      company = data[cols[1]]
      domain = data[cols[2]][4:]
      #print(index)
      #print(company)
      #print(domain)
      tuple = [index, company, domain]
      lines.append(tuple) 
      companyList.append(tuple)
    rownum = rownum + 1
  global companyListSize
  companyListSize = rownum
  putCompanies(100)

def putCompanies(num):
  curIndex = 0
  while curIndex < companyListSize : 
    if curIndex + num <= companyListSize :
      backFillCompanies(curIndex, num) 
    else:
      backFillCompanies(curIndex, num)
    curIndex += num

def backFillCompanies(startPos, num):
  conn = http.client.HTTPConnection("178.128.0.108:3001")
  payloadStart = "{\n\t\"Entries\":[\n\t"
  payloadCompanies0 = "{\n  \"Domain\": \"" 
  payloadCompanies1 = "\",\n       \"Name\": \""
  payloadCompanies2 ="\"\n    } "
  payloadConnector = ",\n  " 
  payloadEnd = "  ]\n}"
  payloadAll = payloadStart
  endPos = startPos+num
  for i in range(startPos,endPos,1):
    if i < companyListSize - 1:
      payload = payloadCompanies0 + companyList[i][2] + payloadCompanies1 + companyList[i][1] + payloadCompanies2 
      if i!= endPos - 1: 
        payload = payload + payloadConnector
      payloadAll += payload
  payloadAll += payloadEnd
  print(payloadAll)
  msg_string = "Backfilling index range {} -> {}..."
  print(msg_string.format(startPos,endPos))
  headers = {
    'Content-Type': "application/json",
    'Cache-Control': "no-cache",
    'Postman-Token': "0364c8c2-e459-4d17-a665-85d2f3a63482"
  }

  conn.request("POST", "/add_company_batch", payloadAll, headers)
  res = conn.getresponse()
  data = res.read()
  # print(data.decode("utf-8"))

def backFillCompany(domain, name):
  conn = http.client.HTTPConnection("178.128.0.108:3001")

  # payload = "{\n  \"Domain\": \"google.com\",\n  \"Name\": \"Google\"\n}"
  payload = "{\n  \"Domain\": \""+ domain + "\",\n  \"Name\": \"" + name  + "\"\n}"

  headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "705e8d11-b538-c01b-6629-c00669e94314"
  }

  conn.request("POST", "/add_company", payload, headers)

  res = conn.getresponse()
  data = res.read()

  print(data.decode("utf-8"))

# Define main method that calls other functions
def main():
  getCompaniesTest()

# Execute main() function
if __name__ == '__main__':
    main()

