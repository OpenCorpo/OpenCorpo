#!/usr/bin/env python
import time
import os
import json
import logging
from autogen import ConversableAgent
from colorlog import ColoredFormatter

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

file_handler = logging.FileHandler('interviews.log')
stream_handler = logging.StreamHandler()
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.info(f"File and stream handlers added to logger. Handlers: {logger.handlers}")

# Define configurations for the AI model
model_config_1 = {
    "config_list": [
        {
            "model": "lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF/Meta-Llama-3-8B-Instruct-Q8_0.gguf",
            "base_url": "http://localhost:1234/v1",
            "api_key": "lm-studio",
        },
    ],
    "cache_seed": None,  # Disable caching.
}
logger.info(f"Model configuration 1 defined. Configuration: {model_config_1}")

model_config_2 = {
    "config_list": [
        {
            "model": "lmstudio-ai/gemma-2b-it-GGUF/gemma-2b-it-q8_0.gguf",
            "base_url": "http://localhost:1234/v1",
            "api_key": "lm-studio",
        },
    ],
    "cache_seed": None,  # Disable caching.
}
logger.info(f"Model configuration 2 defined. Configuration: {model_config_2}")

import uuid
from itertools import permutations

# Initialize agents
try:
    OpenCorpo_Assistant = ConversableAgent("OpenCorpo-Assistant (Llama3)", llm_config=model_config_1)
    logger.info(f"OpenCorpo_Assistant initialized with configuration: {model_config_1}")
    Candidate_Gemma = ConversableAgent("Candidate (Gemma)", llm_config=model_config_2)
    logger.info(f"Candidate_Gemma initialized with configuration: {model_config_2}")
except Exception as e:
    logger.error(f"Error initializing agents: ", exc_info=True)
    exit(1)

# Define topics for interview
topics = [
    "OpenCorpo specific solutions", 
    "common business startup problems", 
    "technological challenges", 
    "scalability issues", 
    "customer acquisition",
    "AI integration in business",
    "data privacy and security",
    "cloud computing",
    "digital marketing strategies",
    "business process automation",
    "blockchain technology in business",
    "business intelligence and analytics",
    "enterprise resource planning",
    "customer relationship management",
    "supply chain management",
    "financial technology solutions",
    "human resources management",
    "project management techniques",
    "business law and ethics",
    "corporate social responsibility",
    "e-commerce strategies",
    "business innovation and creativity",
    "leadership and team management",
    "strategic planning and execution",
    "quality management and lean processes",
    "risk management and mitigation",
    "business continuity planning",
    "corporate finance and investment strategies",
    "mergers and acquisitions",
    "international business and globalization"
]
logger.info(f"Interview topics defined. Topics: {topics}")

# Define problems to be proposed during interview
proposed_problems = [
    "Innovation in this area", 
    "Distuption of existing human business in this area", 
    "Develop a new business model for this area",
    "Revolutionizing customer experience in this area",
    "Implementing AI solutions in this area",
    "Creating a sustainable business model for this area"
]
logger.info(f"Proposed problems for interview defined. Problems: {proposed_problems}")

# Conducting multiple interviews

import random

for i, interview in enumerate(permutations(zip(topics, proposed_problems), 2)):
    topic, problem = None, None
    try:
        (topic, problem) = interview
        logger.info(f"Interview {i} started with topic {topic[0]} and problem {problem[0]}.")

        # Generate interview message
        message = f"OpenCorpo-Assistant (Llama3), whiteboard for me some {topic[0]}. Propose a solution for {problem[0]}. I will evaluate your answers and give my feedback, then propose a problem to you. You will answer and I will evaluate. Let's now begin. You have 30 minutes."
        logger.info(f"Interview message generated. Message: {message}")

        # Randomize the number of conversation iterations
        max_turns = random.randint(3, 6)
        logger.info(f"Number of conversation iterations: {max_turns}")

        # Initiate the chat
        try:
            chat_result = OpenCorpo_Assistant.initiate_chat(Candidate_Gemma, message=message, max_turns=max_turns)
            logger.info(f"Chat initiated. Max turns: {max_turns}")
        except KeyboardInterrupt:
            logger.warning("Chat initiation interrupted by user.")
            continue

        # Create a subdirectory for each interview
        interview_dir = f'interview_{i}'
        os.makedirs(interview_dir, exist_ok=True)
        logger.info(f"Interview directory {interview_dir} created.")

        # Save the chat result in different formats
        date = time.strftime("%Y-%m-%d", time.gmtime())
        transcript_file_name_json = f'{interview_dir}/interview_transcript_{date}_{topic[0].replace(" ", "_")}_{max_turns}.json'
        transcript_file_name_txt = f'{interview_dir}/interview_transcript_{date}_{topic[0].replace(" ", "_")}_{max_turns}.txt'
        logger.info(f"Transcript file names generated. JSON: {transcript_file_name_json}, TXT: {transcript_file_name_txt}")

        if os.path.exists(transcript_file_name_json):
            transcript_file_name_json = f"{transcript_file_name_json}_{uuid.uuid4()}"
            logger.info(f"JSON transcript file name updated to avoid overwrite. New name: {transcript_file_name_json}")

        if os.path.exists(transcript_file_name_txt):
            transcript_file_name_txt = f"{transcript_file_name_txt}_{uuid.uuid4()}"
            logger.info(f"TXT transcript file name updated to avoid overwrite. New name: {transcript_file_name_txt}")

        # Save the chat result in JSON format
        transcript_file_name_json = f"{transcript_file_name_json}_{uuid.uuid4()}"
        with open(transcript_file_name_json, 'w') as file:
            json.dump(chat_result.__dict__, file, indent=4)
            file.flush()
            os.fsync(file.fileno())
        logger.info(f"Chat result saved in JSON format as {transcript_file_name_json}.")

        # Convert the JSON file to a TXT and Markdown file
        with open(transcript_file_name_json, 'r') as json_file:
            data = json.load(json_file)
            transcript_file_name_txt = f"{transcript_file_name_txt}_{uuid.uuid4()}"
            with open(transcript_file_name_txt, 'w') as txt_file, open(transcript_file_name_txt.replace('.txt', f'_{uuid.uuid4()}.md'), 'w') as md_file:
                for key in ["chat_history", "chat_id", "cost", "human_input", "summary"]:
                    if key in data:
                        if key == "chat_history":
                            for i, chat in enumerate(data[key]):
                                txt_file.write(f"{chat['role'].capitalize()}: {chat['content']}\n\n")
                                md_file.write(f"**{chat['role'].capitalize()}**: {chat['content']}\n\n")
                        else:
                            txt_file.write(f"{key.capitalize()}: {data[key]}\n\n")
                            md_file.write(f"**{key.capitalize()}**: {data[key]}\n\n")
        logger.info(f"Chat result converted to TXT and Markdown formats. Files: {transcript_file_name_txt}, {transcript_file_name_txt.replace('.txt', '.md')}")
        logger.info(f"--- Interview Completed. Transcript saved as {transcript_file_name_json}, {transcript_file_name_txt}, and {transcript_file_name_txt.replace('.txt', '.md')}. ---")
    except Exception as e:
        logger.error(f"An error occurred during the interview. Details: ", exc_info=True)

logger.info("\nAll Interviews completed.")
