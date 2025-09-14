from langchain_groq import ChatGroq #use to interact eith llm models inside groq
from langchain_core.prompts import ChatPromptTemplate #will define in what way llm has to respond(to give output in this way)
from src.config.config import GROQ_API_KEY

#llm initialisation
llm = ChatGroq(
    groq_api_key =GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile",
    temperature=0.3
)

#initialise prompt in what way llm has to give answer

itnineary_prompt = ChatPromptTemplate([
    ("system","You are a helpful travel assistant. Create a day trip itineary for {city} based on user's interest : {interests}. Provide a brief , bulleted itineary"), #for llm
    ("human","create a itineary for my day trip") #the human message will be written as create a itinerary for my day trip on this particular city and on this interest.It is a stimulated human message that will act as a starting point of every chat.
])

def generate_itineary(city:str,interests:list[str]) -> str:
    response=llm.invoke( #sending prompt to model and getting a response
        itnineary_prompt.format_messages(city=city,interests=', '.join(interests))
    )
    return response.content

'''
response format

response = {
    "context" : ----
    "content" : ---
}
'''
