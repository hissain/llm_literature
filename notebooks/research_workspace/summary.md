# Project Summary

## ../../generated/arxiv_search_results.json
[
  {
    "title": "A Multi-In-Single-Out Network for Video Frame Interpolation without Optical Flow",
    "authors": [
      "Jaemin Lee",
      "Minseok Seo",
      "Sangwoo Lee",
      "Hyobin Park",
      "Dong-Geol Choi"
    ],
    "published": "2023-11-20",
    "updated": "2023-12-05",
    "abstract": "In general, deep learning-based video frame interpolation (VFI) methods have\npredominantly focused on estimating motion vectors between two input frames and\nwarping them to the target time.

## ../../generated/google_search_results.json
[
  {
    "title": "Video Object Segmentation-aware Video Frame Interpolation - Jun .

## ../../python/semanticscholars.py
# from semanticscholar import SemanticScholar
# sch = SemanticScholar()
# query = "BCG Signal Processing"
# search_results = sch.

## ../../python/custom_agent.py
import autogen
from semanticscholar import SemanticScholar

class TechnicalReviewAgent(autogen.

## ../../python/google_search.py

import os
import time
import json

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

def google_search(query: str, num_results: int = 10, max_chars: int = 1000) -> list:
    
    api_key = os.

## ../../python/project_md.py
import os
import autogen
from typing import List, Dict, Any
from dotenv import load_dotenv

from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
import autogen

load_dotenv()

config_list_file_name = ".

## ../../python/arxiv_search.py

import json
import arxiv
from rich.

## ../tools.ipynb
from autogen_core.

## ../researcher_langchain.ipynb
import os
from dotenv import load_dotenv
from langchain_google_vertexai import ChatVertexAI
from langchain.

## ../researcher_md.ipynb
import os
import autogen
from typing import List, Dict, Any
from dotenv import load_dotenv

from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
import autogen

load_dotenv()

config_list_file_name = ".

## clean.py
import re
ansi_escape = re.

## ../project_markdown.ipynb
import os
import autogen
from dotenv import load_dotenv

from autogen import config_list_from_json
import autogen

load_dotenv()

config_list_file_name = ".

## ../pdf.ipynb
import os
import time
import markdown2
from reportlab.

## ../background.ipynb
# Some required prior steps

1.

## ../researcher_autogen.ipynb

import os
import autogen
from autogen.

## ../researcher_autogen_agentchat.ipynb
import os
import json
from typing import List, Dict, Any
from dotenv import load_dotenv

# Import from the proper autogen packages
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
from autogen.

## ../researcher_semanticscholars.ipynb
from dotenv import load_dotenv

from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
import autogen

load_dotenv()

config_list_file_name = ".

## ../autogen_gemini.ipynb
from dotenv import load_dotenv
import os

load_dotenv()

from autogen_ext.

