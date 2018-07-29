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

def getCompanies():
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
      company = data[cols[1]]
      domain = data[cols[2]][4:]
      print(company)
      print(domain)
      backFillCompanies(domain, company)
    rownum = rownum + 1
  
def backFillCompanies(domain, name):
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
  getCompanies()

# Execute main() function
if __name__ == '__main__':
    main()

