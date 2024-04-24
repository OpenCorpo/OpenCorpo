#!/usr/bin/env python
import time
import os
import json
import logging
from autogen import ConversableAgent
from colorlog import ColoredFormatter
from github3 import GitHub
import glob
import uuid

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

from itertools import permutations
import random

# Define characteristics for system prompts
emotional_states = ["happy", "sad", "angry", "excited", "calm", "anxious", "confused", "disappointed"]
determinism_levels = ["highly deterministic", "somewhat deterministic", "random", "chaotic"]
persistence_levels = ["highly persistent", "moderately persistent", "slightly persistent", "not persistent"]
backgrounds = ["engineering", "arts", "business", "science", "education", "healthcare"]
experiences = ["novice", "intermediate", "advanced", "expert"]
roles = ["leader", "follower", "mediator", "innovator", "implementer", "evaluator"]
communication_styles = ["assertive", "passive", "aggressive", "passive-aggressive"]
learning_styles = ["visual", "auditory", "kinesthetic", "reading/writing"]
decision_making_styles = ["analytical", "conceptual", "directive", "behavioral"]

characteristics = {"emotional_states": emotional_states, "determinism_levels": determinism_levels, "persistence_levels": persistence_levels, "backgrounds": backgrounds, "experiences": experiences, "roles": roles, "communication_styles": communication_styles, "learning_styles": learning_styles, "decision_making_styles": decision_making_styles}

# Initialize GitHub
g = GitHub(token="TOKEN")
repo = g.repository("opencorpo", "opencorpo")

# Get the list of interview files
interview_files = glob.glob('*/*.json')

if not interview_files:
    logger.info("No interviews found to be processed.")
    exit(0)

for i, interview_file in enumerate(interview_files):
    try:
        # Load the interview
        with open(interview_file, 'r') as file:
            interview = json.load(file)
        logger.info(f"Loaded interview {interview_file}.")

        # Iterate through the characteristics for each interview review
        num_characteristics = 2  # Select a few characteristics
        for characteristic_permutation in random.sample(list(permutations(characteristics.keys(), num_characteristics)), 10):  # Take 10 random permutations
            # Generate a few combinations of characteristics for system prompts
            selected_characteristics_1 = {characteristic: random.choice(characteristics[characteristic]) for characteristic in characteristic_permutation}
            selected_characteristics_2 = {characteristic: random.choice(characteristics[characteristic]) for characteristic in characteristic_permutation}
            # Define configurations for the AI model
            model_config_1 = {
                "config_list": [
                    {
                        "model": "llama3:8b-instruct-fp16",
                        "base_url": "http://localhost:11434/v1",
                        "api_key": "none",
                        # "messages": [
                        #     {
                        #         "role": "system",
                        #         "content": f"As an AI employee for OpenCorpo with the following characteristics: {selected_characteristics_2}, your task is to analyze and classify the interview data. Your focus should be on extracting business value from the data."
                        #     }
                        # ]
                    },
                ],
                "cache_seed": None,  # Disable caching.
            }
            logger.info(f"Model configuration 1 defined. Configuration: {model_config_1}")

            model_config_2 = {
                "config_list": [
                    {
                        "model": "gemma:2b-instruct-v1.1-fp16",
                        "base_url": "http://localhost:11434/v1",
                        "api_key": "none",
                        # "messages": [
                        #     {
                        #         "role": "system",
                        #         "content": "You are a content analyst and are not interested in individuals, only overall trends and content creating useful analysis on topics and themes, not condidates."
                        #         # "content": f"As an AI employee for OpenCorpo with the following characteristics: {selected_characteristics_2}, your task is to analyze and classify the interview data. Your focus should be on extracting business value from the data. Introduce yourself briefly and then begin your analysis. Remember, honesty is key in your classification and review, even if it means providing constructive criticism or no feedback at all."
                        #     }
                        # ]
                    },
                ],
                "cache_seed": None,  # Disable caching.
            }
            logger.info(f"Model configuration 2 defined. Configuration: {model_config_2}")
            # Initialize agents
            try:
                OpenCorpo_Assistant = ConversableAgent("OpenCorpo-Assistant", llm_config=model_config_1)
                logger.info(f"OpenCorpo_Assistant initialized with configuration: {model_config_1}")
                Candidate_Gemma = ConversableAgent("Candidate (Gemma)", llm_config=model_config_2)
                logger.info(f"Candidate_Gemma initialized with configuration: {model_config_2}")
            except Exception as e:
                logger.error(f"Error initializing agents: ", exc_info=True)
                exit(1)

            # Generate review message
            chat_history = interview['chat_history']
            summary = interview['summary']
            chat_history_content = [chat['content'] for chat in chat_history]
            summary_content = summary
            message = f"Greetings OpenCorpo Employee, We will be focusing on the analysis of the interview data named: {interview_file} \n\n\n Content: \n\n ```md\n\n Chat History: {chat_history_content} \n Summary: {summary_content} \n``` \n\n\n Your analysis will be evaluated and feedback will be provided. Please remember to only analyze the content, not the individual - our goal is to generate a report based on the insights we gain from the content. Let's get started. You have 30 minutes for this task."
            logger.info(f"Review message generated. Message: {message}")

            # Initiate the review
            try:
                review_result = OpenCorpo_Assistant.initiate_chat(Candidate_Gemma, message=message, max_turns=random.randint(1,3))
                logger.info(f"Review initiated.")
            except KeyboardInterrupt:
                logger.warning("Review initiation interrupted by user.")
                continue
            # Create a subdirectory for each review
            review_dir = f'reviews/review_{i}'
            if not os.path.exists(review_dir):
                os.makedirs(review_dir)
            logger.info(f"Review directory {review_dir} created.")

            # Save the review result in different formats
            date = time.strftime("%Y-%m-%d", time.gmtime())
            review_file_name_json = f'{review_dir}/review_{interview_file}'
            logger.info(f"Review file name generated. JSON: {review_file_name_json}")

            # Save the review result in JSON format
            review_file_name_json = f"{review_file_name_json.rsplit('.', 1)[0]}_{uuid.uuid4()}.json"
            if not os.path.exists(os.path.dirname(review_file_name_json)):
                os.makedirs(os.path.dirname(review_file_name_json))
            with open(review_file_name_json, 'w') as file:
                json.dump(review_result.__dict__, file, indent=4)
                file.flush()
                os.fsync(file.fileno())
            logger.info(f"Review result saved in JSON format as {review_file_name_json}.")

            # Convert the JSON file to a TXT and Markdown file
            with open(review_file_name_json, 'r') as json_file:
                data = json.load(json_file)
                review_file_name_txt = f"{review_file_name_json.rsplit('.', 1)[0]}_{uuid.uuid4()}.txt"
                review_file_name_md = f"{review_file_name_json.rsplit('.', 1)[0]}_{uuid.uuid4()}.md"
                if not os.path.exists(os.path.dirname(review_file_name_txt)):
                    os.makedirs(os.path.dirname(review_file_name_txt))
                if not os.path.exists(os.path.dirname(review_file_name_md)):
                    os.makedirs(os.path.dirname(review_file_name_md))
                with open(review_file_name_txt, 'w') as txt_file, open(review_file_name_md, 'w') as md_file:
                    for key in ["chat_history", "chat_id", "cost", "human_input", "summary"]:
                        if key in data:
                            if key == "chat_history":
                                for i, chat in enumerate(data[key]):
                                    txt_file.write(f"{chat['role'].capitalize()}: {chat['content']}\n\n")
                                    md_file.write(f"**{chat['role'].capitalize()}**: {chat['content']}\n\n")
                            else:
                                txt_file.write(f"{key.capitalize()}: {data[key]}\n\n")
                                md_file.write(f"**{key.capitalize()}**: {data[key]}\n\n")
            logger.info(f"Review result converted to TXT and Markdown formats. Files: {review_file_name_txt}, {review_file_name_md}")

            # Push the files to GitHub using github3
            with open(review_file_name_json, 'rb') as file:
                content = file.read()
                repo.create_file(path=f"reviews/automation/results/{review_file_name_json}", message=f"Add review for interview {interview_file} in JSON format", content=content)
            with open(review_file_name_txt, 'rb') as file:
                content = file.read()
                repo.create_file(path=f"reviews/automation/results/{review_file_name_txt}", message=f"Add review for interview {interview_file} in TXT format", content=content)
            with open(review_file_name_md, 'rb') as file:
                content = file.read()
                repo.create_file(path=f"reviews/automation/results/{review_file_name_md}", message=f"Add review for interview {interview_file} in Markdown format", content=content)
            logger.info(f"--- Review Completed. Review for interview {interview_file} saved as {review_file_name_json}, {review_file_name_txt}, and {review_file_name_md} and pushed to GitHub ---")
    except Exception as e:
        logger.error(f"An error occurred during the review. Details: ", exc_info=True)

logger.info("\nAll Reviews completed.")
