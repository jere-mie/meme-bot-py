# Note you must pip install gspread oauth2client first
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("drive.json", scope)

driveClient = gspread.authorize(creds)

sheet = driveClient.open("Verification").sheet1
col = sheet.col_values(2)  # Get a specific column

# print(col[1])