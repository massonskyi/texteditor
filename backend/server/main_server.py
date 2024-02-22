from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/get_file")
def get_file():
    with open("example_file.txt", "r") as file:
        content = file.read()
    return content


@app.post("/save_file")
def save_file(content: str):
    with open("example_file.txt", "w") as file:
        file.write(content)
    return {"message": "File saved successfully"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main_server:app", reload=True)
