import openai
from approaches.approach import Approach
from azure.search.documents import SearchClient
from azure.search.documents.models import QueryType
from langchain.llms.openai import AzureOpenAI
from langchain.prompts import PromptTemplate, BasePromptTemplate
from langchain.callbacks.base import CallbackManager
from langchain.agents import Tool, AgentExecutor
from langchain.agents.react.base import ReActDocstoreAgent
from langchainadapters import HtmlCallbackHandler
from text import nonewlines
from typing import List

class ReadDecomposeAsk(Approach):
    def __init__(self, search_client: SearchClient, openai_deployment: str, sourcepage_field: str, content_field: str):
        self.search_client = search_client
        self.openai_deployment = openai_deployment
        self.sourcepage_field = sourcepage_field
        self.content_field = content_field

    def search(self, q: str, overrides: dict) -> str:
        use_semantic_captions = True if overrides.get("semantic_captions") else False
        top = overrides.get("top") or 3
        exclude_category = overrides.get("exclude_category") or None
        filter = "category ne '{}'".format(exclude_category.replace("'", "''")) if exclude_category else None

        if overrides.get("semantic_ranker"):
            r = self.search_client.search(q,
                                          filter=filter,
                                          query_type=QueryType.SEMANTIC, 
                                          query_language="en-us", 
                                          query_speller="lexicon", 
                                          semantic_configuration_name="default", 
                                          top = top,
                                          query_caption="extractive|highlight-false" if use_semantic_captions else None)
        else:
            r = self.search_client.search(q, filter=filter, top=top)
        if use_semantic_captions:
            self.results = [doc[self.sourcepage_field] + ":" + nonewlines(" . ".join([c.text for c in doc['@search.captions'] ])) for doc in r]
        else:
            self.results = [doc[self.sourcepage_field] + ":" + nonewlines(doc[self.content_field][:500]) for doc in r]
        return "\n".join(self.results)

    def lookup(self, q: str) -> str:
        r = self.search_client.search(q,
                                      top = 1,
                                      include_total_count=True,
                                      query_type=QueryType.SEMANTIC, 
                                      query_language="en-us", 
                                      query_speller="lexicon", 
                                      semantic_configuration_name="default",
                                      query_answer="extractive|count-1",
                                      query_caption="extractive|highlight-false")
        
        answers = r.get_answers()
        if answers and len(answers) > 0:
            return answers[0].text
        if r.get_count() > 0:
            return "\n".join(d['content'] for d in r)
        return None        

    def run(self, q: str, overrides: dict) -> any:
        # Not great to keep this as instance state, won't work with interleaving (e.g. if using async), but keeps the example simple
        self.results = None

        # Use to capture thought process during iterations
        cb_handler = HtmlCallbackHandler()
        cb_man