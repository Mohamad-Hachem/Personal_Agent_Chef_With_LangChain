from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from prompts import CHEF_SYSTEM_PROMPT
from tools import web_search
from uploading_images_to_agents import choose_image_file, build_image_message
import logging

# logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

# creating our model
logging.info("creating our model...")
model = init_chat_model(model="gpt-5-nano")
logging.info(f"our model {model.name} was created successfulyy!")

# creating my agent
logging.info("creating our agent...")
chef_agent = create_agent(model=model,
                          tools=[web_search], 
                          system_prompt=CHEF_SYSTEM_PROMPT)  #checkpointer=InMemorySaver()
                          
logging.info(f"our agent {chef_agent.name} was created successfully!")

# getting path to image
path = choose_image_file()

# building our message for our agent that contains our prompt and our image
question = build_image_message(image_path=path, prompt=CHEF_SYSTEM_PROMPT)

# memory config
# config = {"configurable":{"thread_id":"1"}}

# Sending message to my agent
logging.info("we are invoking our agent...")
answer = chef_agent.invoke({"messages": question}) #, config=config

# printing my answer
logging.info("agent response:")
logging.info(answer["messages"][-1].content)





