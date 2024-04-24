#!/usr/bin/env python
import time
import os
import json
import logging
from autogen import ConversableAgent
from colorlog import ColoredFormatter
from github3 import GitHub
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
            "model": "llama3:8b-instruct-fp16",
            "base_url": "http://localhost:11434/v1",
            "api_key": "none",
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
        },
    ],
    "cache_seed": None,  # Disable caching.
}
logger.info(f"Model configuration 2 defined. Configuration: {model_config_2}")

import uuid
from itertools import permutations

# Initialize agents
try:
    OpenCorpo_Assistant = ConversableAgent("OpenCorpo-Assistant", llm_config=model_config_1)
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
    "international business and globalization",
    "product development and management",
    "sales strategies and techniques",
    "market research and analysis",
    "branding and brand management",
    "public relations and media strategies",
    "corporate communication",
    "business ethics and corporate governance",
    "organizational behavior and culture",
    "change management and innovation",
    "business strategy and policy",
    "operations management",
    "logistics and supply chain strategies",
    "performance management",
    "employee engagement and motivation",
    "talent acquisition and retention",
    "workforce diversity and inclusion",
    "corporate training and development",
    "compensation and benefits management",
    "labor laws and industrial relations",
    "business analytics and decision making",
    "financial planning and analysis",
    "capital budgeting",
    "financial risk management",
    "corporate taxation",
    "auditing and assurance",
    "accounting standards and regulations",
    "business valuation",
    "investment analysis and portfolio management",
    "financial markets and institutions",
    "corporate restructuring",
    "international finance",
    "e-business and e-commerce",
    "information systems management",
    "data management and data warehousing",
    "network security and cyber security",
    "software development and management",
    "IT project management",
    "business process re-engineering",
    "knowledge management",
    "IT governance and compliance",
    "emerging technologies",
    "sustainable business practices",
    "environmental management",
    "corporate philanthropy and community involvement",
    "business and society",
    "business and government relations",
    "business and human rights",
    "business and the environment",
    "business and public policy",
    "business and international relations",
    "business and economic development",
    "business and social entrepreneurship",
    "business and non-profit management",
    "business and healthcare management",
    "business and education management",
    "business and sports management",
    "business and hospitality management",
    "business and tourism management",
    "business and entertainment management",
    "business and arts management",
    "business and fashion management",
    "business and real estate management",
    "business and agriculture management",
    "business and energy management",
    "business and construction management",
    "business and manufacturing management",
    "business and retail management",
    "business and logistics management",
    "business and transportation management",
    "business and food service management",
    "business and facilities management",
    "business and event management",
    "business and project management",
    "business and risk management",
    "business and quality management",
    "business and operations management",
    "business and information management",
    "business and human resource management",
    "business and financial management",
    "business and marketing management",
    "business and strategic management",
    "business and organizational management",
    "business and production management",
    "business and service management",
    "business and systems management",
    "business and technology management",
    "business and innovation management",
    "business and knowledge management",
    "business and change management",
    "business and performance management",
    "business and process management",
    "business and product management",
    "business and program management",
    "business and relationship management",
    "business and resource management",
    "business and talent management",
    "business and vendor management",
    "business and workflow management",
    "business and yield management",
    "business and zone management"
]
logger.info(f"Interview topics defined. Topics: {topics}")

# Define problems to be proposed during interview
proposed_problems = [
     "Challenges of business continuity planning in this area",
    "Challenges of business integration in this area",
    "Challenges of business intelligence in this area",
    "Challenges of business performance management in this area",
    "Challenges of business process automation in this area",
    "Challenges of business process excellence in this area",
    "Challenges of business process governance in this area",
    "Challenges of business process modeling in this area",
    "Challenges of business process quality in this area",
    "Challenges of business process transformation in this area",
    "Challenges of business process validation in this area",
    "Challenges of business process value chain in this area",
    "Challenges of business process variability in this area",
    "Challenges of business process verification in this area",
    "Challenges of business process virtualization in this area",
    "Challenges of business process volatility in this area",
    "Challenges of business valuation in this area",
    "Challenges of change management in this area",
    "Challenges of cybersecurity in this area",
    "Challenges of data privacy in this area",
    "Challenges of financial management in this area",
    "Challenges of intellectual property rights in this area",
    "Challenges of maintaining quality in this area",
    "Challenges of project management in this area",
    "Challenges of regulatory compliance in this area",
    "Challenges of remote work in this area",
    "Challenges of scaling up in this area",
    "Challenges of supply chain management in this area",
    "Challenges of talent retention in this area",
    "Challenges to implement ideas in this area",
    "Creating a sustainable business model for this area",
    "Current landscape of this area",
    "Develop a new business model for this area",
    "Difficulty in this area",
    "Distuption of existing human business in this area",
    "Emerging trends in this area",
    "Ethical considerations in this area",
    "Impact of 5G technology in this area",
    "Impact of advanced technology in this area",
    "Impact of artificial intelligence in this area",
    "Impact of augmented reality in this area",
    "Impact of biotechnology in this area",
    "Impact of blockchain technology in this area",
    "Impact of breakthrough technology in this area",
    "Impact of clean technology in this area",
    "Impact of climate change in this area",
    "Impact of cutting-edge technology in this area",
    "Impact of digital technology in this area",
    "Impact of disruptive technology in this area",
    "Impact of economic downturn in this area",
    "Impact of emerging technology in this area",
    "Impact of future technology in this area",
    "Impact of government regulations in this area",
    "Impact of green technology in this area",
    "Impact of high-tech technology in this area",
    "Impact of information technology in this area",
    "Impact of innovative technology in this area",
    "Impact of internet of things in this area",
    "Impact of machine learning in this area",
    "Impact of nanotechnology in this area",
    "Impact of next generation technology in this area",
    "Impact of quantum computing in this area",
    "Impact of revolutionary technology in this area",
    "Impact of social media in this area",
    "Impact of state-of-the-art technology in this area",
    "Impact of tech-centric technology in this area",
    "Impact of tech-driven technology in this area",
    "Impact of tech-enabled technology in this area",
    "Impact of tech-forward technology in this area",
    "Impact of tech-infused technology in this area",
    "Impact of tech-innovative technology in this area",
    "Impact of tech-inspired technology in this area",
    "Impact of tech-integrated technology in this area",
    "Impact of tech-intensive technology in this area",
    "Impact of tech-interacting technology in this area",
    "Impact of tech-interactive technology in this area",
    "Impact of tech-interchangeable technology in this area",
    "Impact of tech-interconnected technology in this area",
    "Impact of tech-interdependent technology in this area",
    "Impact of tech-interdisciplinary technology in this area",
    "Impact of tech-interfacing technology in this area",
    "Impact of tech-interlacing technology in this area",
    "Impact of tech-interlinked technology in this area",
    "Impact of tech-intermeshing technology in this area",
    "Impact of tech-intermixing technology in this area",
    "Impact of tech-interoperable technology in this area",
    "Impact of tech-interpenetrating technology in this area",
    "Impact of tech-interposing technology in this area",
    "Impact of tech-interrelated technology in this area",
    "Impact of tech-intersecting technology in this area",
    "Impact of tech-interweaving technology in this area",
    "Impact of tech-interwinding technology in this area",
    "Impact of tech-interworking technology in this area",
    "Impact of tech-interwoven technology in this area",
    "Impact of tech-interwrought technology in this area",
    "Impact of tech-intricate technology in this area",
    "Impact of tech-inventive technology in this area",
    "Impact of technology in this area",
    "Impact of tech-savvy technology in this area",
    "Impact of transformative technology in this area",
    "Impact of virtual reality in this area",
    "Implementing AI solutions in this area",
    "Importance of brand reputation in this area",
    "Importance of business agility in this area",
    "Importance of business ethics in this area",
    "Importance of business process alignment in this area",
    "Importance of business process analysis in this area",
    "Importance of business process lifecycle management in this area",
    "Importance of business process management in this area",
    "Importance of business process mapping in this area",
    "Importance of business process outsourcing in this area",
    "Importance of business process reengineering in this area",
    "Importance of business process validation in this area",
    "Importance of business process value capture in this area",
    "Importance of business process value creation in this area",
    "Importance of business process value delivery in this area",
    "Importance of business process value elevation in this area",
    "Importance of business process value enhancement in this area",
    "Importance of business process value enrichment in this area",
    "Importance of business process value escalation in this area",
    "Importance of business process value estimation in this area",
    "Importance of business process value evolution in this area",
    "Importance of business process value expansion in this area",
    "Importance of business process value extension in this area",
    "Importance of business process value extraction in this area",
    "Importance of business process value proposition in this area",
    "Importance of business process value realization in this area",
    "Importance of business process value stream in this area",
    "Importance of business process velocity in this area",
    "Importance of business process versatility in this area",
    "Importance of business process visibility in this area",
    "Importance of business process vitality in this area",
    "Importance of business process vulnerability in this area",
    "Importance of competitive analysis in this area",
    "Importance of corporate culture in this area",
    "Importance of customer feedback in this area",
    "Importance of customer loyalty in this area",
    "Importance of customer relationship management in this area",
    "Importance of customer satisfaction in this area",
    "Importance of employee engagement in this area",
    "Importance of employee training in this area",
    "Importance of innovation culture in this area",
    "Importance of market segmentation in this area",
    "Importance of operational efficiency in this area",
    "Importance of strategic partnerships in this area",
    "Importance of work-life balance in this area",
    "Influence of global trends in this area",
   "Innovation in this area",
    "New Approaches",
    "Old proven methods",
    "Pragmatic solutions",
    "Revolutionizing customer experience in this area",
    "Risky ideas",
    "Role of agile methodologies in this area",
    "Role of automation in this area",
    "Role of big data in this area",
    "Role of cloud computing in this area",
    "Role of continuous learning in this area",
    "Role of corporate branding in this area",
    "Role of corporate communication in this area",
    "Role of corporate culture in this area",
    "Role of corporate development in this area",
    "Role of corporate finance in this area",
    "Role of corporate governance in this area",
    "Role of corporate identity in this area",
    "Role of corporate image in this area",
    "Role of corporate influence in this area",
    "Role of corporate initiative in this area",
    "Role of corporate innovation in this area",
    "Role of corporate insight in this area",
    "Role of corporate inspiration in this area",
    "Role of corporate instinct in this area",
    "Role of corporate instruction in this area",
    "Role of corporate integration in this area",
    "Role of corporate integrity in this area",
    "Role of corporate intelligence in this area",
    "Role of corporate intention in this area",
    "Role of corporate interaction in this area",
    "Role of corporate intercommunication in this area",
    "Role of corporate interconnection in this area",
    "Role of corporate interdependence in this area",
    "Role of corporate interexchange in this area",
    "Role of corporate interface in this area",
    "Role of corporate interlock in this area",
    "Role of corporate interplay in this area",
    "Role of corporate interpretation in this area",
    "Role of corporate interrelation in this area",
    "Role of corporate intertwine in this area",
    "Role of corporate intertwist in this area",
    "Role of corporate interweave in this area",
    "Role of corporate intuition in this area",
    "Role of corporate investigation in this area",
    "Role of corporate investment in this area",
    "Role of corporate involvement in this area",
    "Role of corporate leadership in this area",
    "Role of corporate learning in this area",
    "Role of corporate performance in this area",
    "Role of corporate responsibility in this area",
    "Role of corporate social responsibility in this area",
    "Role of corporate strategy in this area",
    "Role of corporate sustainability in this area",
    "Role of data in decision making in this area",
    "Role of design thinking in this area",
    "Role of digital transformation in this area",
    "Role of diversity and inclusion in this area",
    "Role of e-commerce in this area",
    "Role of leadership in this area",
    "Role of mobile technology in this area",
    "Role of social entrepreneurship in this area",
    "Role of sustainability in this area",
    "Safe and trusted pathways"
    "Safe and trusted pathways",
    "Strategies for business continuity in this area",
    "Strategies for business diversification in this area",
    "Strategies for business expansion in this area",
    "Strategies for business process engineering in this area",
    "Strategies for business process improvement in this area",
    "Strategies for business process integration in this area",
    "Strategies for business process management in this area",
    "Strategies for business process maturity in this area",
    "Strategies for business process optimization in this area",
    "Strategies for business process standardization in this area",
    "Strategies for business process value in this area",
    "Strategies for business process variation in this area",
    "Strategies for business process vector analysis in this area",
    "Strategies for business process vector control in this area",
    "Strategies for business process vectoring in this area",
    "Strategies for business process vectorization in this area",
    "Strategies for business process vector optimization in this area",
    "Strategies for business process vector perfection in this area",
    "Strategies for business process vector prediction in this area",
    "Strategies for business process vector prevention in this area",
    "Strategies for business process vector projection in this area",
    "Strategies for business process vector protection in this area",
    "Strategies for business process vector transformation in this area",
    "Strategies for business process venturing in this area",
    "Strategies for business process viability in this area",
    "Strategies for business process visualization in this area",
    "Strategies for business process vitality in this area",
    "Strategies for business sustainability in this area",
    "Strategies for business transformation in this area",
    "Strategies for cost reduction in this area",
    "Strategies for crisis management in this area",
    "Strategies for customer acquisition in this area",
    "Strategies for customer retention in this area",
    "Strategies for digital marketing in this area",
    "Strategies for growth in this area",
    "Strategies for market penetration in this area",
    "Strategies for product development in this area",
    "Strategies for revenue growth in this area",
    "Strategies for risk management in this area",
    "Strategies for talent acquisition in this area",

]

logger.info(f"Proposed problems for interview defined. Problems: {proposed_problems}")

# Conducting multiple interviews

import random

# Initialize GitHub
g = GitHub(token="TOKEN")
repo = g.repository("opencorpo", "opencorpo")

interview_permutations = list(permutations(zip(topics, proposed_problems), 2))
random.shuffle(interview_permutations)

for i, interview in enumerate(interview_permutations):
    topic, problem = None, None
    try:
        (topic, problem) = interview
        logger.info(f"Interview {i} started with topic {topic[0]} and problem {problem[0]}.")

        # Generate interview message
        message = f"OpenCorpo-Assistant (Llama3), whiteboard for me some {topic[0]}. Propose a solution for {problem[0]}. I will evaluate your answers and give my feedback, then propose a problem to you. You will answer and I will evaluate. Let's now begin. You have 30 minutes."
        logger.info(f"Interview message generated. Message: {message}")

        # Randomize the number of conversation iterations
        max_turns = random.randint(2, 14)
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

        # Save the chat result in JSON format
        transcript_file_name_json = f"{transcript_file_name_json.rsplit('.', 1)[0]}_{uuid.uuid4()}.json"
        with open(transcript_file_name_json, 'w') as file:
            json.dump(chat_result.__dict__, file, indent=4)
            file.flush()
            os.fsync(file.fileno())
        logger.info(f"Chat result saved in JSON format as {transcript_file_name_json}.")

        # Convert the JSON file to a TXT and Markdown file
        with open(transcript_file_name_json, 'r') as json_file:
            data = json.load(json_file)
            transcript_file_name_txt = f"{transcript_file_name_txt.rsplit('.', 1)[0]}_{uuid.uuid4()}.txt"
            transcript_file_name_md = f"{transcript_file_name_txt.rsplit('.', 1)[0]}_{uuid.uuid4()}.md"
            with open(transcript_file_name_txt, 'w') as txt_file, open(transcript_file_name_md, 'w') as md_file:
                for key in ["chat_history", "chat_id", "cost", "human_input", "summary"]:
                    if key in data:
                        if key == "chat_history":
                            for i, chat in enumerate(data[key]):
                                txt_file.write(f"{chat['role'].capitalize()}: {chat['content']}\n\n")
                                md_file.write(f"**{chat['role'].capitalize()}**: {chat['content']}\n\n")
                        else:
                            txt_file.write(f"{key.capitalize()}: {data[key]}\n\n")
                            md_file.write(f"**{key.capitalize()}**: {data[key]}\n\n")
        logger.info(f"Chat result converted to TXT and Markdown formats. Files: {transcript_file_name_txt}, {transcript_file_name_md}")

        # Push the files to GitHub using github3
        with open(transcript_file_name_json, 'rb') as file:
            content = file.read()
            repo.create_file(path=f"interviews/automation/results/{transcript_file_name_json}", message=f"Add interview transcript for topic {topic[0]} with problem {problem[0]} in JSON format", content=content)
        with open(transcript_file_name_txt, 'rb') as file:
            content = file.read()
            repo.create_file(path=f"interviews/automation/results/{transcript_file_name_txt}", message=f"Add interview transcript for topic {topic[0]} with problem {problem[0]} in TXT format", content=content)
        with open(transcript_file_name_md, 'rb') as file:
            content = file.read()
            repo.create_file(path=f"interviews/automation/results/{transcript_file_name_md}", message=f"Add interview transcript for topic {topic[0]} with problem {problem[0]} in Markdown format", content=content)
        logger.info(f"--- Interview Completed. Transcript for topic {topic[0]} with problem {problem[0]} saved as {transcript_file_name_json}, {transcript_file_name_txt}, and {transcript_file_name_md} and pushed to GitHub ---")
    except Exception as e:
        logger.error(f"An error occurred during the interview. Details: ", exc_info=True)

logger.info("\nAll Interviews completed.")
