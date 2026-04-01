from fastapi import FastAPI

app = FastAPI()

# Add CORS here




# TODO Setup login here
# @app.get("/login")
# async def login(email:str, password:str):
#     return {""}
    

@app.get("/search_tags")
async def search_by_tag(project_id:str, tag:str):
    return {"notes_found": [], "links_found": []}  # TODO Just a stub for now

@app.get("/search_note")
async def search_by_tag(project_id:str, note:str):
    return {"notes_found": [], "links_found": []}  # TODO Just a stub for now