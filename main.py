from fastapi import FastAPI #FastAPI is a python class that prvies all functionalities for your API
import random
import pandas as pd

app = FastAPI()

@app.get('/')
def root():
    return {'message': 'Welcome to the fact generator, just enter /facts to the end of the URL to show the facts'}

def read_facts():
    with open('facts.txt', 'r') as file:
        facts = file.read().splitlines()
    return facts

facts_list = read_facts()

@app.get("/facts")
def get_random_fact(index: int = None):
    if index is not None and index >= 0 and index < len(facts_list):
        return {str(index+1): facts_list[index]}
    else:
        random_fact_index = random.randint(0, len(facts_list) - 1)
        return {str(random_fact_index +1): facts_list[random_fact_index]}

@app.post("/add")
def add_fact(new_fact: str):
    with open('facts.txt', 'a') as file:
        file.write(new_fact + '\n')
    facts_list.append(new_fact)
    return {"message": "Fact added successfully"}