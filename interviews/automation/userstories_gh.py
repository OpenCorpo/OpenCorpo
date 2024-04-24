#!/usr/bin/env python
import time
import os
import json
import logging
from autogen import ConversableAgent, GroupChatManager, GroupChat
from colorlog import ColoredFormatter
from github3 import GitHub
import glob
import uuid
import random

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.info(f"Logging setup completed. Logger level set to {logger.getEffectiveLevel()}.")

# Create colored logging
formatter = ColoredFormatter(
    "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s",
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG':    'cyan',
        'INFO':     'green',
        'WARNING':  'yellow',
        'ERROR':    'red',
        'CRITICAL': 'red',
    }
)
logger.info("Colored logging formatter created. Log colors defined for different levels.")

file_handler = logging.FileHandler('reviews.log')
stream_handler = logging.StreamHandler()
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.info(f"File and stream handlers added to logger. Handlers: {logger.handlers}")

# Initialize GitHub
g = GitHub(token="TOKEN")
repo = g.repository("opencorpo", "opencorpo")

# Define configurations for the AI models
gemma_config = {
    "config_list": [
        {
            "model": "gemma:2b-instruct-v1.1-fp16",
            "base_url": "http://localhost:11434/v1",
            "api_key": "none",
        },
    ],
    "cache_seed": None,  # Disable caching.
}

llama_config = {
    "config_list": [
        {
            "model": "llama3:8b-instruct-fp16",
            "base_url": "http://localhost:11434/v1",
            "api_key": "none",
        },
    ],
    "cache_seed": None,  # Disable caching.
}

logger.info(f"Model configurations defined. Configurations: {gemma_config}, {llama_config}")

# Initialize agents
try:
    Gemma_Agent = ConversableAgent("Gemma-Agent", llm_config=gemma_config)
    Llama_Agent = ConversableAgent("Llama-Agent", llm_config=llama_config)
    logger.info(f"Gemma_Agent and Llama_Agent initialized with configurations: {gemma_config}, {llama_config}")
except Exception as e:
    logger.error(f"Error initializing agents: ", exc_info=True)
    exit(1)

# Get the list of review files
review_files = glob.glob('reviews/**/*.json', recursive=True)
if not review_files:
    logger.info("No reviews found to be processed.")
    exit(0)

for i, review_file in enumerate(review_files):
    try:
        # Load the review
        with open(review_file, 'r') as file:
            review = json.load(file)
        logger.info(f"Loaded review {review_file}.")

        # Generate user stories
        chat_history = review['chat_history']
        chat_history_content = [chat['content'] for chat in chat_history]
        message = f"Based on the following discussion: {chat_history_content}, generate a discussion and then 5 user stories."
        logger.info(f"User story generation message: {message}")

        # Initiate the user story generation with Gemma_Agent
        try:
            group_chat = GroupChatManager(groupchat=GroupChat(agents=[Gemma_Agent, Llama_Agent], messages=[], max_round=5))  # Increase max_round to 5 to get full conversation
            Gemma_Agent.initiate_chat(group_chat, message=message, max_turns=5)  # Increase max_turns to 5 to get full conversation
            logger.info(f"User story generation initiated with Gemma_Agent.")
        except AttributeError:
            logger.error(f"Error initiating chat with Gemma_Agent: ", exc_info=True)
            continue

        # Generate final results with Llama_Agent
        try:
            Llama_Agent.initiate_chat(group_chat, message=message, max_turns=5)  # Increase max_turns to 5 to get full conversation
            logger.info(f"Final results generated with Llama_Agent.")
        except AttributeError:
            logger.error(f"Error initiating chat with Llama_Agent: ", exc_info=True)
            continue
        # Create a subdirectory for each user story
        user_story_dir = f'user_stories/user_story_{i}'
        if not os.path.exists(user_story_dir):
            os.makedirs(user_story_dir)
        logger.info(f"User story directory {user_story_dir} created.")

        # Save the user story result in JSON format
        user_story_file_name_json = f"{user_story_dir}/user_story_{review_file.rsplit('.', 1)[0]}_{uuid.uuid4()}.json"
        if not os.path.exists(os.path.dirname(user_story_file_name_json)):
            os.makedirs(os.path.dirname(user_story_file_name_json))
        with open(user_story_file_name_json, 'w') as file:
            json.dump(group_chat.groupchat.messages, file, indent=4)  # Corrected line
            file.flush()
            os.fsync(file.fileno())
        logger.info(f"User story result saved in JSON format as {user_story_file_name_json}.")

        # Convert the JSON file to a TXT and Markdown file
        with open(user_story_file_name_json, 'r') as json_file:
            data = json.load(json_file)
            user_story_file_name_txt = f"{user_story_file_name_json.rsplit('.', 1)[0]}_{uuid.uuid4()}.txt"
            user_story_file_name_md = f"{user_story_file_name_json.rsplit('.', 1)[0]}_{uuid.uuid4()}.md"
            if not os.path.exists(os.path.dirname(user_story_file_name_txt)):
                os.makedirs(os.path.dirname(user_story_file_name_txt))
            if not os.path.exists(os.path.dirname(user_story_file_name_md)):
                os.makedirs(os.path.dirname(user_story_file_name_md))
            with open(user_story_file_name_txt, 'w') as txt_file, open(user_story_file_name_md, 'w') as md_file:
                for chat in data:
                    txt_file.write(f"{chat['role'].capitalize()}: {chat['content']}\n\n")
                    md_file.write(f"**{chat['role'].capitalize()}**: {chat['content']}\n\n")
        logger.info(f"User story result converted to TXT and Markdown formats. Files: {user_story_file_name_txt}, {user_story_file_name_md}")

        # Push the files to GitHub using github3
        with open(user_story_file_name_json, 'rb') as file:
            content = file.read()
            repo.create_file(path=f"user_stories/results/{user_story_file_name_json}", message=f"Add user story for review {review_file} in JSON format", content=content)
        with open(user_story_file_name_txt, 'rb') as file:
            content = file.read()
            repo.create_file(path=f"user_stories/results/{user_story_file_name_txt}", message=f"Add user story for review {review_file} in TXT format", content=content)
        with open(user_story_file_name_md, 'rb') as file:
            content = file.read()
            repo.create_file(path=f"user_stories/results/{user_story_file_name_md}", message=f"Add user story for review {review_file} in Markdown format", content=content)
        logger.info(f"--- User Story Generation Completed. User story for review {review_file} saved as {user_story_file_name_json}, {user_story_file_name_txt}, and {user_story_file_name_md} and pushed to GitHub ---")
    except Exception as e:
        logger.error(f"An error occurred during the user story generation. Details: ", exc_info=True)

logger.info("\nAll User Story Generations completed.")
