from langchain_core.messages import HumanMessage,AIMessage #to keep track of the history {what ai is saying and what human is saying},basically to keep track of the conversation
from src.chains.itinerary_chain import generate_itineary
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException

logger = get_logger(__name__) 

class TravelPlanner:
    def __init__(self):
        self.messages=[]#conversation is stored in self.messages
        self.city=""
        self.interests=[]
        self.itineary=""

        logger.info("Initialized TravelPlanner instance")

    def set_city(self,city:str):
        try:
            self.city = city
            self.messages.append(HumanMessage(content=city))
            logger.info("City set successfully")
        except Exception as e:
            logger.error(f"error while setting city:{e}")
            raise CustomException("Failed to set city",e)
        
    def set_interests(self,interests_str:str):
        #converting comma seperated string given by the user to list
        try:
            self.interests = [i.strip() for i in interests_str.split(",")]
            self.messages.append(HumanMessage(content=interests_str))
            logger.info("Interest also set successfully..")
        except Exception as e:
            logger.error(f"error while setting interests : {e}")
            raise CustomException("Failed to set interest",e)
        
    def create_itineary(self):
        try:
            logger.info(f"Generating itineary for {self.city} and for interests : {self.interests}")
            itineary = generate_itineary(self.city,self.interests)
            self.itineary = itineary
            self.messages.append(AIMessage(content=itineary)) #content=itineary means the actual text of the AI’s response is stored in the variable itineary
            logger.info("Itineary generated successfully..")
            return itineary
        except Exception as e:
            logger.error(f"error while creating itineary : {e}")
            raise CustomException("Failed to create itineary",e)
        
'''
This is how the chat history will get recorded

[
    "Human":"delhi",
    "Human":"Red Fort"
    "AI": "---------------"
]
'''