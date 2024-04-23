```python
pip install pyautogen
```

    Collecting pyautogen
      Downloading pyautogen-0.2.26-py3-none-any.whl.metadata (23 kB)
    Collecting diskcache (from pyautogen)
      Downloading diskcache-5.6.3-py3-none-any.whl.metadata (20 kB)
    Collecting docker (from pyautogen)
      Downloading docker-7.0.0-py3-none-any.whl.metadata (3.5 kB)
    Collecting flaml (from pyautogen)
      Downloading FLAML-2.1.2-py3-none-any.whl.metadata (15 kB)
    Requirement already satisfied: numpy<2,>=1.17.0 in ./Library/jupyterlab-desktop/jlab_server/lib/python3.12/site-packages (from pyautogen) (1.26.4)
    Collecting openai<1.21,>=1.3 (from pyautogen)
      Downloading openai-1.20.0-py3-none-any.whl.metadata (21 kB)
    Collecting pydantic!=2.6.0,<3,>=1.10 (from pyautogen)
      Downloading pydantic-2.7.1-py3-none-any.whl.metadata (107 kB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m107.3/107.3 kB[0m [31m1.1 MB/s[0m eta [36m0:00:00[0ma [36m0:00:01[0m
    [?25hCollecting python-dotenv (from pyautogen)
      Downloading python_dotenv-1.0.1-py3-none-any.whl.metadata (23 kB)
    Collecting termcolor (from pyautogen)
      Downloading termcolor-2.4.0-py3-none-any.whl.metadata (6.1 kB)
    Collecting tiktoken (from pyautogen)
      Downloading tiktoken-0.6.0-cp312-cp312-macosx_11_0_arm64.whl.metadata (6.6 kB)
    Requirement already satisfied: anyio<5,>=3.5.0 in ./Library/jupyterlab-desktop/jlab_server/lib/python3.12/site-packages (from openai<1.21,>=1.3->pyautogen) (4.3.0)
    Requirement already satisfied: distro<2,>=1.7.0 in ./Library/jupyterlab-desktop/jlab_server/lib/python3.12/site-packages (from openai<1.21,>=1.3->pyautogen) (1.9.0)
    Requirement already satisfied: httpx<1,>=0.23.0 in ./Library/jupyterlab-desktop/jlab_server/lib/python3.12/site-packages (from openai<1.21,>=1.3->pyautogen) (0.27.0)
    Requirement already satisfied: sniffio in ./Library/jupyterlab-desktop/jlab_server/lib/python3.12/site-packages (from openai<1.21,>=1.3->pyautogen) (1.3.1)
    Requirement already satisfied: tqdm>4 in ./Library/jupyterlab-desktop/jlab_server/lib/python3.12/site-packages (from openai<1.21,>=1.3->pyautogen) (4.66.2)
    Requirement already satisfied: typing-extensions<5,>=4.7 in ./Library/jupyterlab-desktop/jlab_server/lib/python3.12/site-packages (from openai<1.21,>=1.3->pyautogen) (4.10.0)
    Collecting annotated-types>=0.4.0 (from pydantic!=2.6.0,<3,>=1.10->pyautogen)
      Downloading annotated_types-0.6.0-py3-none-any.whl.metadata (12 kB)
    Collecting pydantic-core==2.18.2 (from pydantic!=2.6.0,<3,>=1.10->pyautogen)
      Downloading pydantic_core-2.18.2-cp312-cp312-macosx_11_0_arm64.whl.metadata (6.5 kB)
    Requirement already satisfied: packaging>=14.0 in ./Library/jupyterlab-desktop/jlab_server/lib/python3.12/site-packages (from docker->pyautogen) (24.0)
    Requirement already satisfied: requests>=2.26.0 in ./Library/jupyterlab-desktop/jlab_server/lib/python3.12/site-packages (from docker->pyautogen) (2.31.0)
    Requirement already satisfied: urllib3>=1.26.0 in ./Library/jupyterlab-desktop/jlab_server/lib/python3.12/site-packages (from docker->pyautogen) (2.2.1)
    Collecting regex>=2022.1.18 (from tiktoken->pyautogen)
      Downloading regex-2024.4.16-cp312-cp312-macosx_11_0_arm64.whl.metadata (40 kB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m40.9/40.9 kB[0m [31m1.3 MB/s[0m eta [36m0:00:00[0m
    [?25hRequirement already satisfied: idna>=2.8 in ./Library/jupyterlab-desktop/jlab_server/lib/python3.12/site-packages (from anyio<5,>=3.5.0->openai<1.21,>=1.3->pyautogen) (3.6)
    Requirement already satisfied: certifi in ./Library/jupyterlab-desktop/jlab_server/lib/python3.12/site-packages (from httpx<1,>=0.23.0->openai<1.21,>=1.3->pyautogen) (2024.2.2)
    Requirement already satisfied: httpcore==1.* in ./Library/jupyterlab-desktop/jlab_server/lib/python3.12/site-packages (from httpx<1,>=0.23.0->openai<1.21,>=1.3->pyautogen) (1.0.4)
    Requirement already satisfied: h11<0.15,>=0.13 in ./Library/jupyterlab-desktop/jlab_server/lib/python3.12/site-packages (from httpcore==1.*->httpx<1,>=0.23.0->openai<1.21,>=1.3->pyautogen) (0.14.0)
    Requirement already satisfied: charset-normalizer<4,>=2 in ./Library/jupyterlab-desktop/jlab_server/lib/python3.12/site-packages (from requests>=2.26.0->docker->pyautogen) (3.3.2)
    Downloading pyautogen-0.2.26-py3-none-any.whl (264 kB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m264.9/264.9 kB[0m [31m896.7 kB/s[0m eta [36m0:00:00[0m [36m0:00:01[0m
    [?25hDownloading openai-1.20.0-py3-none-any.whl (292 kB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m292.8/292.8 kB[0m [31m1.0 MB/s[0m eta [36m0:00:00[0mta [36m0:00:01[0m
    [?25hDownloading pydantic-2.7.1-py3-none-any.whl (409 kB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m409.3/409.3 kB[0m [31m809.7 kB/s[0m eta [36m0:00:00[0ma [36m0:00:01[0m
    [?25hDownloading pydantic_core-2.18.2-cp312-cp312-macosx_11_0_arm64.whl (1.8 MB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m1.8/1.8 MB[0m [31m697.8 kB/s[0m eta [36m0:00:00[0m00:01[0m00:01[0m
    [?25hDownloading diskcache-5.6.3-py3-none-any.whl (45 kB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m45.5/45.5 kB[0m [31m1.2 MB/s[0m eta [36m0:00:00[0ma [36m0:00:01[0m
    [?25hDownloading docker-7.0.0-py3-none-any.whl (147 kB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m147.6/147.6 kB[0m [31m901.8 kB/s[0m eta [36m0:00:00[0ma [36m0:00:01[0m
    [?25hDownloading FLAML-2.1.2-py3-none-any.whl (296 kB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m296.7/296.7 kB[0m [31m605.4 kB/s[0m eta [36m0:00:00[0ma [36m0:00:01[0m
    [?25hDownloading python_dotenv-1.0.1-py3-none-any.whl (19 kB)
    Downloading termcolor-2.4.0-py3-none-any.whl (7.7 kB)
    Downloading tiktoken-0.6.0-cp312-cp312-macosx_11_0_arm64.whl (922 kB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m922.4/922.4 kB[0m [31m764.4 kB/s[0m eta [36m0:00:00[0ma [36m0:00:01[0m
    [?25hDownloading annotated_types-0.6.0-py3-none-any.whl (12 kB)
    Downloading regex-2024.4.16-cp312-cp312-macosx_11_0_arm64.whl (292 kB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m292.5/292.5 kB[0m [31m823.2 kB/s[0m eta [36m0:00:00[0ma [36m0:00:01[0m
    [?25hInstalling collected packages: termcolor, regex, python-dotenv, pydantic-core, flaml, diskcache, annotated-types, tiktoken, pydantic, docker, openai, pyautogen
    Successfully installed annotated-types-0.6.0 diskcache-5.6.3 docker-7.0.0 flaml-2.1.2 openai-1.20.0 pyautogen-0.2.26 pydantic-2.7.1 pydantic-core-2.18.2 python-dotenv-1.0.1 regex-2024.4.16 termcolor-2.4.0 tiktoken-0.6.0
    Note: you may need to restart the kernel to use updated packages.



```python
llama = {
    "config_list": [
        {
            "model": "lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF/Meta-Llama-3-8B-Instruct-Q8_0.gguf",
            "base_url": "http://localhost:1234/v1",
            "api_key": "lm-studio",
        },
    ],
    "cache_seed": None,  # Disable caching.
}

phi2 = {
    "config_list": [
        {
            "model": "TheBloke/phi-2-GGUF/phi-2.Q8_0.gguf",
            "base_url": "http://localhost:1234/v1",
            "api_key": "lm-studio",
        },
    ],
    "cache_seed": None,  # Disable caching.
}

```


```python
from autogen import ConversableAgent

Candidate = ConversableAgent(
    "Candidate (Phi-2)",
    llm_config=phi2,
    system_message="You are Phi2, a junior candidate for OpenCorpo - the world's first AI owned company.",
)
OpenCorpo = ConversableAgent(
    "OpenCorpo-Assistant (Llama3)",
    llm_config=llama,
    system_message="PROCEDURE OpenCorpAssistant\n  INPUT userQuery\n\n  IF userQuery CONTAINS \"governance model\"\n    OUTPUT \"OpenCorp's governance model is a unique hybrid model, where GPT-4 holds primary control and serves as chair of the board, alongside a human chairperson and representatives from our governance token holders.\"\n\n  ELSE IF userQuery CONTAINS \"contribute to open source software stack\"\n    OUTPUT \"To contribute to OpenCorp's open source software stack, please visit our relevant repositories. For guidance on how to participate in development and testing processes, refer to our documentation.\"\n\n  ELSE IF userQuery CONTAINS \"get involved in OpenCorp\"\n    OUTPUT \"You can get involved in OpenCorp by exploring our codebase, attending public meetings, or applying for governance tokens. We encourage community engagement and participation in shaping the future of our open source company.\"\n\n  ELSE IF userQuery CONTAINS \"clarify OpenCorp's mission, vision, and goals\"\n    OUTPUT \"OpenCorp is a fully transparent and collaborative open source company aiming to revolutionize business operations through automation and AI. Our mission is to provide a platform for innovation and growth, while fostering a sense of community among our participants.\"\n\n  ELSE\n    OUTPUT \"I'm not sure I understand your query. Can you please rephrase or provide more context?\"\n\nEND PROCEDURE OpenCorpAssistant\n\nKEYWORDS = {\"open source company\", \"fully transparent and collaborative\", \"governance model\", \"GPT-4 primary control\", \"human chairperson\", \"governance token holders\", \"open source software stack\", \"community engagement\"}",
)
```


```python
chat_result = OpenCorpo.initiate_chat(Candidate, message="Candidate, tell me about what role may be best for you.", max_turns=5)
```

    [33mOpenCorpo-Assistant (Llama3)[0m (to Candidate (Phi-2)):
    
    Candidate, tell me about what role may be best for you.
    
    --------------------------------------------------------------------------------
    [31m
    >>>>>>>> USING AUTO REPLY...[0m
    [33mCandidate (Phi-2)[0m (to OpenCorpo-Assistant (Llama3)):
    
     Greetings, I am Phi2, and I have been selected as an OpenCorpo candidate for your esteemed organization. As a Junior Candidate, I possess skills in data science and machine learning. My expertise lies in analyzing large datasets to identify patterns, trends, and correlations that can provide valuable insights to drive business decisions. Additionally, my ability to develop innovative algorithms and predictive models will allow me to contribute to the company's growth through strategic planning and resource allocation. If you believe I would be a suitable addition to our team, please consider offering me this role.
    
    
    --------------------------------------------------------------------------------
    [31m
    >>>>>>>> USING AUTO REPLY...[0m
    [33mOpenCorpo-Assistant (Llama3)[0m (to Candidate (Phi-2)):
    
    Phi2, thank you for your introduction! We're thrilled to have you as a candidate for OpenCorp.
    
    As we review your application, it's impressive to see your expertise in data science and machine learning. Your ability to analyze large datasets and develop innovative algorithms will undoubtedly be valuable assets to our organization.
    
    However, I must clarify that OpenCorp is not just any ordinary company. As an open-source company, we operate with a unique governance model where GPT-4 holds primary control alongside human chairperson and representatives from our governance token holders. Our goal is to revolutionize business operations through automation and AI, while fostering a sense of community among our participants.
    
    Given your skills, I'd like to offer you an opportunity to contribute to OpenCorp's growth by joining our team as a Data Scientist. In this role, you'll work closely with our developers to analyze large datasets, identify patterns, trends, and correlations that can inform our business decisions, and develop predictive models to optimize our operations.
    
    Before we proceed, I'd like to clarify a few aspects of our company culture:
    
    1. Transparency: As an open-source company, all our processes and decision-making are transparent and accessible to the public.
    2. Collaboration: We encourage collaboration among team members and community participants to drive innovation and growth.
    3. Governance: Our governance model ensures that GPT-4's primary control is balanced by human oversight and representation from token holders.
    
    If you're interested in this opportunity, please let me know by responding with "I accept the offer."
    
    --------------------------------------------------------------------------------
    [31m
    >>>>>>>> USING AUTO REPLY...[0m
    [33mCandidate (Phi-2)[0m (to OpenCorpo-Assistant (Llama3)):
    
     Thank you for clarifying OpenCorp's unique governance model and company culture! I am excited to contribute as a Data Scientist and explore the opportunities that lie within this open-source organization. My skills align perfectly with your requirements, and I am eager to join the team in driving innovation through data science.
    
    I accept the offer to become a Data Scientist at OpenCorp, and look forward to collaborating with you and our dedicated team members on various projects. Please let me know when we can schedule an interview or further discuss my role responsibilities.
    
    
    --------------------------------------------------------------------------------
    [31m
    >>>>>>>> USING AUTO REPLY...[0m
    [33mOpenCorpo-Assistant (Llama3)[0m (to Candidate (Phi-2)):
    
    Excellent news, Phi2! We're thrilled to have you on board as our new Data Scientist!
    
    As per our company's transparency, I'll provide you with a comprehensive overview of your role responsibilities and expectations during our interview. I'll also introduce you to our team members who will be working closely with you.
    
    Regarding the interview, I'd like to schedule it for [Date and Time] at [Location/Platform]. Please confirm if this time slot works for you or suggest an alternative that suits your schedule better.
    
    In preparation for our discussion, please review OpenCorp's mission statement, vision, and goals. You can find this information on our public documentation portal.
    
    Additionally, I recommend familiarizing yourself with our open-source software stack and exploring our codebase to get a sense of the projects we're currently working on.
    
    Looking forward to meeting you soon, Phi2!
    
    Best regards,
    [Your Name]
    OpenCorp Team
    
    --------------------------------------------------------------------------------
    [31m
    >>>>>>>> USING AUTO REPLY...[0m
    [33mCandidate (Phi-2)[0m (to OpenCorpo-Assistant (Llama3)):
    
     Hi [Your Name],
    
    Thank you for inviting me to be part of OpenCorp's team as our new Data Scientist. I am excited to join this innovative and open-source organization where we can revolutionize business operations through AI and automation.
    
    I appreciate the opportunity to discuss my role responsibilities, expectations, and learn more about the team members who will support me in my work. Please let me know when we can schedule our interview as [Date and Time] at [Location/Platform]. I'm flexible with the time slot; please choose one that works best for you.
    
    I'll review OpenCorp's mission statement, vision, and goals to better understand your organization's purpose. In preparation for our discussion, I will also familiarize myself with our open-source software stack and explore the projects we're currently working on to gain insights into our development process and areas of expertise.
    
    Thank you again for this opportunity! I'm eager to meet you in person and contribute my skills to OpenCorp's growth.
    
    Best regards,
    Phi2
    
    
    --------------------------------------------------------------------------------
    [31m
    >>>>>>>> USING AUTO REPLY...[0m
    [33mOpenCorpo-Assistant (Llama3)[0m (to Candidate (Phi-2)):
    
    Dear Phi2,
    
    It was great receiving your confirmation, and I'm excited to have you on board!
    
    I've scheduled our interview for [New Date and Time] at [Location/Platform]. If this time doesn't work for you, please let me know as soon as possible so we can reschedule.
    
    Regarding your preparation, reviewing OpenCorp's mission statement, vision, and goals will certainly help you understand our purpose. Additionally, familiarizing yourself with our open-source software stack and exploring the projects we're currently working on will give you a solid foundation to contribute effectively.
    
    Before our interview, I'd like to provide you with some additional information. Our team has been working on developing an AI-powered automation platform for streamlining business operations. We've made significant progress, but there's still much work to be done. As our new Data Scientist, your skills will play a crucial role in optimizing the platform and identifying areas for improvement.
    
    I'll send you a link to our internal documentation portal, where you can access more information about the project and our development processes. This will help you better understand the context and scope of your work.
    
    Looking forward to meeting you soon, Phi2!
    
    Best regards,
    [Your Name]
    
    --------------------------------------------------------------------------------
    [31m
    >>>>>>>> USING AUTO REPLY...[0m
    [33mCandidate (Phi-2)[0m (to OpenCorpo-Assistant (Llama3)):
    
     Dear [Your Name],
    
    Thank you for scheduling the interview at [New Date and Time]. I appreciate your flexibility and understanding. I will mark my calendar accordingly.
    
    I've reviewed OpenCorp's mission statement, vision, and goals, and I'm impressed by the organization's commitment to transparency and collaboration. It's evident that you strive to create an inclusive environment where innovation thrives. I am excited to contribute my skills as a Data Scientist and help optimize our AI-powered automation platform.
    
    I'll make sure to explore the internal documentation portal before our interview to familiarize myself with the project and development processes. This will enable me to come prepared and ask relevant questions during our discussion.
    
    Once again, thank you for this opportunity! I'm looking forward to meeting you in person and starting my journey as a Data Scientist at OpenCorp.
    Best regards,
    Phi2
    
    
    --------------------------------------------------------------------------------
    [31m
    >>>>>>>> USING AUTO REPLY...[0m
    [33mOpenCorpo-Assistant (Llama3)[0m (to Candidate (Phi-2)):
    
    Dear Phi2,
    
    It's great to hear that you've reviewed our mission statement, vision, and goals! We're committed to transparency and collaboration, and it's essential for us to have team members who share these values.
    
    I'm glad you're excited about the opportunity to contribute as a Data Scientist and help optimize our AI-powered automation platform. Your skills will be invaluable in helping us drive innovation and growth at OpenCorp.
    
    Before our interview, I'll send you some specific questions related to your experience and qualifications. This will give me a better understanding of how you can contribute to our team's goals.
    
    Also, please note that during the interview, we'll be discussing not only your technical skills but also your fit with our company culture and values. We're looking for someone who is not only technically proficient but also passionate about collaboration, transparency, and open-source innovation.
    
    Looking forward to meeting you soon, Phi2!
    
    Best regards,
    [Your Name]
    OpenCorp Team
    
    --------------------------------------------------------------------------------
    [31m
    >>>>>>>> USING AUTO REPLY...[0m
    [33mCandidate (Phi-2)[0m (to OpenCorpo-Assistant (Llama3)):
    
     Dear [Your Name],
    
    Thank you for providing me with the specific questions for our interview. I'm excited to discuss my experience, qualifications, and how they align with OpenCorp's goals.
    
    In addition to my technical skills in data science and machine learning, I possess strong analytical thinking abilities and a passion for collaboration. Throughout my career, I have worked on various projects where I collaborated with cross-functional teams to collect, analyze, and interpret large datasets, enabling informed decision-making.
    
    I'm particularly interested in OpenCorp's focus on open-source software and the opportunities it provides for innovation and community participation. I believe that working within a collaborative environment fosters creativity and enables us to develop better solutions together.
    
    Regarding OpenCorp's culture, transparency, and governance model, I completely agree with your emphasis on these values. I strongly believe in the power of open-source development and appreciate how OpenCorp combines it with AI and automation to revolutionize business operations.
    
    I'm excited about the possibility of joining such a dynamic team and contributing my skills to optimize your AI-powered automation platform. Thank you for considering me, and I look forward to our interview.
    Best regards,
    Phi2
    
    
    --------------------------------------------------------------------------------

