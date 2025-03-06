from fastapi import FastAPI


from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel
import uvicorn
import os
api_key = os.environ['OPENAI_API']
app = FastAPI()

class Body(BaseModel):
    text:str




llm_mini=ChatOpenAI(model="gpt-4o-mini",api_key=api_key) 
prompt_template = PromptTemplate.from_template("You are a helpful assistant answer with max 30 words, {prompt}")

# get, post, put, and delete

@app.get("/")
def welcome():
    return {"message":"Welcome to ChatGpt AI application v2!"}


@app.get("/home")
def welcome():
    return {"message":"Hello home"}


@app.post("/dummy")
def demo_function(data):
    return {"message":data}


@app.post("/response")
def generate(body: Body):
    prompt = body.text
    chain = prompt_template|llm_mini
    res = chain.invoke({"prompt":prompt})
    return res.content

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
