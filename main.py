from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app=FastAPI()

# / as in normal website denotes the home ,landing or in more technical terms the root page
@app.get("/")
def root():
    return "Henlo World"

# we are trying to create a todo list app so we crete a items array to store all the tasks and then need endpoints to view or edit the tasks

#  create a custom object class , this is not something that we have done in express this resembles more of the schema formation of Convex , MongoDB or the class formation in LLD problems

class Item(BaseModel):
    # create a custom model for each task on the todo list
    text:str = "None"
    is_done:bool =False
# set the default values for each task

items=[]
@app.post("/add-item") 
# here we have type checking for the variable item via pydantic ,type checking is not naturally available in python
def add_item(item:Item):
    items.append(item)
    return items
    # return the list of items
# to test this send request via postman, make sure while testing to use link/add-item

# now to get a particular entry with an id ,  make sure while testing this to add a couple of entries into the items array as each change causes the server to reload causing itesm array to become empty

@app.get("get-item/{index}",response_model=Item)
def get_item(index:int) :
    if(items[index]) :
        return items[index]
    else :
        return HTTPException(status_code=404,detail=f"Item with index :{index} not found, This is a client side error");
# use {} to directly send variable necessary in the request else use a post request and specify the index in the body but dont make a get request here and send a post request from postman 


# this method allows us to extract the value of index from the dynamic url and then return the sliced version of that array up to that index
@app.get("list_items/{index}")
def list_items(index:int=len(items)):
    return items[0:index]

# now for creating a proper app , we may need more complex data types for type checking this is where pydantic comes in 


