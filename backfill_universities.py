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
universities =  "1BjF5J_Ki5_DiDBXWqMeoXVRlfKwxpLe71RmjBhlZdlg"
url = "https://docs.google.com/spreadsheets/d/{0}/export?format=csv".format(universities)
universityList = []
global universityListSize

def getUniversities0():
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
      university = data[cols[1]]
      domain = data[cols[2]][7:]
      print(data[cols[0]])
      print(university)
      print(domain)
      backFillUniversities(domain, university)
    rownum = rownum + 1

def getUniversitiesTest():
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
      university = data[cols[1]]
      domain = data[cols[2]][7:]
      #print(data[cols[0]])
      #print(university)
      #print(domain)
      tuple = [rownum, university, domain]
      universityList.append(tuple)
    rownum = rownum + 1
    global universityListSize
    universityListSize = rownum
    backFillUniversitiesBatch(0,50)
  
def backFillUniversities(domain, name):
  conn = http.client.HTTPConnection("178.128.0.108:3001")

  # payload = "{\n  \"Domain\": \"google.com\",\n  \"Name\": \"Google\"\n}"
  payload = "{\n  \"Domain\": \""+ domain + "\",\n  \"Name\": \"" + name  + "\"\n}"

  headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "705e8d11-b538-c01b-6629-c00669e94314"
  }

  conn.request("POST", "/add_school", payload, headers)

  res = conn.getresponse()
  data = res.read()

  print(data.decode("utf-8"))

def backFillUniversitiesBatch(startPos, num):
  conn = http.client.HTTPConnection("178.128.0.108:3001")
  payloadStart = "{\n\t\"Entries\":[\n\t"
  payloadUniversity0 = "{\n  \"Domain\": \""
  payloadUniversity1 = "\",\n       \"Name\": \""
  payloadUniversity2 ="\"\n    } "
  payloadConnector = ",\n  "
  payloadEnd = "  ]\n}"
  payloadAll = payloadStart
  endPos = startPos+num
  for i in range(startPos,endPos,1):
    if i < universityListSize - 1:
      payload = payloadUniversity0 + universityList[i][2] + payloadUniversity1 + universityList[i][1] + payloadUniversity2
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

  conn.request("POST", "/add_university_batch", payloadAll, headers)
  res = conn.getresponse()
  data = res.read()
  # print(data.decode("utf-8"))


# Define main method that calls other functions
def main():
  getUniversitiesTest()

# Execute main() function
if __name__ == '__main__':
    main()

