import openai
from approaches.approach import Approach
from azure.search.documents import SearchClient
from azure.search.documents.models import QueryType
from langchain.llms.ope