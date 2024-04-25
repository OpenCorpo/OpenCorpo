
import json
import datetime
from libopencorpo import *


if __name__ == "__main__":
    # Setup logging
    setup_logging()
    formatter = create_colored_logging()
    add_handlers_to_logger(formatter)

    # Initialize GitHub
    g, repo = initialize_github()

    # Fetch all GitHub data
    try:
        username = "opencorpo"  # Add the username here
        user, repos, gists, followers, following, starred, subscriptions, issues = fetch_all_github_data(g, username)
    except ValueError as e:
        logger.error("Error fetching GitHub data: ", exc_info=True)
        exit(1)

    # Define model configurations
    gemma_config, llama_config = define_model_configurations()

    # Initialize agents
    Gemma_Agent, Llama_Agent = initialize_agents(gemma_config, llama_config)
    logger.info(f"Gemma_Agent and Llama_Agent initialized with configurations: {gemma_config}, {llama_config}")

    # Generate full report
    full_report = generate_full_report(
        user=user, 
        repos=repos, 
        gists=gists, 
        followers=followers, 
        following=following, 
        starred=starred, 
        subscriptions=subscriptions, 
        issues=issues
    )
    logger.info(f"Full report generated for {username} on {datetime.datetime.now().isoformat()}")

    # Initiate GitHub report generation with Gemma_Agent and generate final results with Llama_Agent

    # Process each section of the report individually
    for section in full_report:
        if isinstance(full_report[section], list) and full_report[section]:
            # Sort the key values in each section and unique them, remove duplicate urls
            full_report[section] = sorted(full_report[section], key=lambda x: str(x))

            # Convert the section into a string
            section_string = json.dumps(full_report[section], indent=4, sort_keys=True)

            # Use a try-except block to handle any JSON errors
            try:
                # Load the string back into a Python object
                section_object = json.loads(section_string)

                # Check if the section_object is not empty
                if section_object:
                    # Create a message for the report
                    message = "As OpenCorpo Employees, analyze this segment of our latest github api data here:  \n\n\n ```json \n\n" + json.dumps(section_object, indent=4, sort_keys=True) +"\n\n```\n\n Write a report on this data, keeping in mind the goals of OpenCorpo and producing actionable items."
                    # Use initiate_github_report_generation_with_agents
                    group_chat = initiate_github_report_generation_with_agents(Gemma_Agent, Llama_Agent, message)
                    if group_chat is not None:
                        # Create report directory
                        i = 1  # Define i as per your requirement
                        report_dir = create_report_directory(i)
                        # Save report result in JSON format
                        report_file_name_json = save_report_result_in_JSON_format(report_dir, group_chat)

                        # Convert JSON to TXT and Markdown
                        report_file_name_txt, report_file_name_md = convert_JSON_to_TXT_and_Markdown(report_file_name_json)

                        # Push files to GitHub
                        push_files_to_GitHub(repo, report_file_name_json, report_file_name_txt, report_file_name_md)

            except json.JSONDecodeError:
                logger.error(f"Error processing section {section}: Invalid JSON")
                continue  # Skip this section if it's not valid JSON
