from fastapi import FastAPI
import os
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
import pwdlib[argon2]
import jwt
from dotenv import load_dotenv
import psycopg



load_dotenv()

conn = psycopg.connect(conninfo=os.getenv('DATABASE_URL'))


security = HTTPBearer()

app = FastAPI()

# Add CORS here




# TODO Setup login here
@app.get("/login")
async def login(email:str, password:str):
    '''
    Hashes email-passwords combos and checks against database to verify users. Then returns a JWT Auth Token
    
    RETURNS: JWT Auth Token
    THROWS: If user-password combo not found in database, throw exception and return a 401 unauthorized code
    '''
    
#     return {""}
    
def verify_token()

@app.get("/search_tags")
async def search_by_tag(project_id:str, tag:str, token:):
    return {"notes_found": [], "links_found": []}  # TODO Just a stub for now

@app.get("/search_note")
async def search_by_tag(project_id:str, note:str):
    return {"notes_found": [], "links_found": []}  # TODO Just a stub for now