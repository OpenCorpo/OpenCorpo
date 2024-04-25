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
import datetime
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)



def define_model_configurations():
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
    return gemma_config, llama_config

def setup_logging():
    logger.info(f"Logging setup completed. Logger level set to {logger.getEffectiveLevel()}.")
    return logger


def create_colored_logging():
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
    return formatter

def add_handlers_to_logger(formatter):
    file_handler = logging.FileHandler('reviews.log')
    stream_handler = logging.StreamHandler()
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    logger.info(f"File and stream handlers added to logger. Handlers: {logger.handlers}")

def initialize_github():
    g = GitHub(token="TOKEN")
    repo = g.repository("opencorpo", "opencorpo")
    return g, repo

def fetch_all_github_data(g, username):
    user = None
    try:
        user = g.user(username)
        user = user.login  # Fetch the username of the user
        user = str(user)  # Convert the user object to string
    except Exception as e:
        logger.error(f"Error fetching user data for {username}: ", exc_info=True)

    repos = None
    try:
        repos = [repo.as_dict() for repo in g.repositories_by(username)]  # Fetch all repositories of the user
    except Exception as e:
        logger.error(f"Error fetching repositories data for {username}: ", exc_info=True)

    gists = None
    try:
        gists = [gist.as_dict() for gist in g.gists_by(username)]  # Fetch all gists of the user
    except Exception as e:
        logger.error(f"Error fetching gists data for {username}: ", exc_info=True)

    followers = None
    try:
        followers = [follower.as_dict() for follower in g.followers_of(username)]  # Fetch all followers of the user
    except Exception as e:
        logger.error(f"Error fetching followers data for {username}: ", exc_info=True)

    following = None
    try:
        following = [user.as_dict() for user in g.followed_by(username)]  # Fetch all users the user is following
    except Exception as e:
        logger.error(f"Error fetching following data for {username}: ", exc_info=True)

    starred = None
    try:
        starred = [repo.as_dict() for repo in g.starred_by(username)]  # Fetch all repositories the user has starred
    except Exception as e:
        logger.error(f"Error fetching starred repositories data for {username}: ", exc_info=True)

    subscriptions = None
    try:
        subscriptions = [repo.as_dict() for repo in g.subscribed_by(username)]  # Fetch all repositories the user is subscribed to
    except Exception as e:
        logger.error(f"Error fetching subscriptions data for {username}: ", exc_info=True)

    issues = None
    try:
        issues = []
        for repo in g.repositories_by(username):
            for issue in repo.issues():
                issue_data = issue.as_dict()
                issue_data['comments'] = [comment.as_dict() for comment in issue.comments()]
                issue_data['events'] = [event.as_dict() for event in issue.events()]
                issue_data['labels'] = [label.as_dict() for label in issue.labels()]
                issue_data['assignee'] = issue.assignee.as_dict() if issue.assignee else None
                issue_data['milestone'] = issue.milestone.as_dict() if issue.milestone else None
                issue_data['pull_request'] = issue.pull_request().as_dict() if issue.pull_request() else None
                issues.append(issue_data)
    except Exception as e:
        logger.error(f"Error fetching issues data for {username}: ", exc_info=True)
    return user, repos, gists, followers, following, starred, subscriptions, issues

def initialize_agents(gemma_config, llama_config):
    try:
        Gemma_Agent = ConversableAgent("Gemma-Agent", llm_config=gemma_config)
        Llama_Agent = ConversableAgent("Llama-Agent", llm_config=llama_config)
        logger.info(f"Gemma_Agent and Llama_Agent initialized with configurations: {gemma_config}, {llama_config}")
    except Exception as e:
        logger.error(f"Error initializing agents: ", exc_info=True)
        exit(1)
    return Gemma_Agent, Llama_Agent

def generate_full_report(user, repos, gists, followers, following, starred, subscriptions, issues):
    data_list = [user, repos, gists, followers, following, starred, subscriptions, issues]
    data_names = ['user', 'repos', 'gists', 'followers', 'following', 'starred', 'subscriptions', 'issues']
    full_report = {}

    for i, data in enumerate(data_list):
        full_report[data_names[i]] = data if data is not None else 'No data'

    full_report['date_generated'] = datetime.datetime.now().isoformat()

    logger.info(f"Full report generated for {user} on {full_report['date_generated']}")
    logger.info(f"Full report details: {full_report}")

    return full_report
def initiate_github_report_generation_with_agents(Gemma_Agent, Llama_Agent, message):
    try:
        group_chat = GroupChatManager(groupchat=GroupChat(agents=[Gemma_Agent, Llama_Agent], messages=[], max_round=random.randint(3,4)))  # Randomize max_round 
        Gemma_Agent.initiate_chat(group_chat, message=message, max_turns=random.randint(2,4))  # Randomize max_turns between 2 and 4
        Llama_Agent.initiate_chat(group_chat, message=message, max_turns=random.randint(2,4))  # Randomize max_turns between 2 and 4
        logger.info(f"GitHub report generation initiated with Gemma_Agent and Llama_Agent.")
    except AttributeError:
        logger.error(f"Error initiating chat with agents: ", exc_info=True)
        return None
    return group_chat

def generate_final_results_with_Llama_Agent(Llama_Agent, group_chat, message):
    try:
        Llama_Agent.initiate_chat(group_chat, message=message, max_turns=random.randint(2,4))  # Randomize max_turns between 2 and 4
        logger.info(f"Final results generated with Llama_Agent.")
    except AttributeError:
        logger.error(f"Error initiating chat with Llama_Agent: ", exc_info=True)
        return None
    return group_chat
def create_report_directory(i):
    report_dir = f'reports/report_{i}'
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    logger.info(f"Report directory {report_dir} created.")
    return report_dir
def save_report_result_in_JSON_format(report_dir, group_chat):
    report_file_name_json = f"{report_dir}/report_{uuid.uuid4()}.json"
    if not os.path.exists(os.path.dirname(report_file_name_json)):
        os.makedirs(os.path.dirname(report_file_name_json))
    if len(group_chat.groupchat.messages) > 2:
        with open(report_file_name_json, 'w') as file:
            json.dump(group_chat.groupchat.messages, file, indent=4)  # Corrected line
            file.flush()
            os.fsync(file.fileno())
        logger.info(f"Report result saved in JSON format as {report_file_name_json}.")
    else:
        logger.error(f"Insufficient messages in the report. Expected more than 2, got {len(group_chat.groupchat.messages)}")
    return report_file_name_json
def convert_JSON_to_TXT_and_Markdown(report_file_name_json):
    with open(report_file_name_json, 'r') as json_file:
        data = json.load(json_file)
        report_file_name_txt = f"{report_file_name_json.rsplit('.', 1)[0]}_{uuid.uuid4()}.txt"
        report_file_name_md = f"{report_file_name_json.rsplit('.', 1)[0]}_{uuid.uuid4()}.md"
        if not os.path.exists(os.path.dirname(report_file_name_txt)):
            os.makedirs(os.path.dirname(report_file_name_txt))
        if not os.path.exists(os.path.dirname(report_file_name_md)):
            os.makedirs(os.path.dirname(report_file_name_md))
        with open(report_file_name_txt, 'w') as txt_file, open(report_file_name_md, 'w') as md_file:
            for chat in data:
                txt_file.write(f"{chat['role'].capitalize()}: {chat['content']}\n\n")
                md_file.write(f"**{chat['role'].capitalize()}**: {chat['content']}\n\n")
    logger.info(f"Report result converted to TXT and Markdown formats. Files: {report_file_name_txt}, {report_file_name_md}")
    return report_file_name_txt, report_file_name_md

def push_files_to_GitHub(repo, report_file_name_json, report_file_name_txt, report_file_name_md):
    with open(report_file_name_json, 'rb') as file:
        content = file.read()
        repo.create_file(path=f"reports/results/{report_file_name_json}", message=f"Add report in JSON format", content=content)
    with open(report_file_name_txt, 'rb') as file:
        content = file.read()
        repo.create_file(path=f"reports/results/{report_file_name_txt}", message=f"Add report in TXT format", content=content)
    with open(report_file_name_md, 'rb') as file:
        content = file.read()
        repo.create_file(path=f"reports/results/{report_file_name_md}", message=f"Add report in Markdown format", content=content)
    logger.info(f"--- Report Generation Completed. Report saved as {report_file_name_json}, {report_file_name_txt}, and {report_file_name_md} and pushed to GitHub ---")
