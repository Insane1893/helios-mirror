from pyrogram import Client
api_id = int(input("Enter API KEY: "))
api_hash = input("Enter API HASH: ")

app = Client("Anything", api_id=api_id, api_hash=api_hash)
with app:
 x = app.export_session_string()
 print(x)
