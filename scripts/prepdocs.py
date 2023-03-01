
import os
import argparse
import glob
import io
import re
import time
from pypdf import PdfReader, PdfWriter
from azure.identity import DefaultAzureCredential
from azure.core.credentials import AzureKeyCredential
from azure.storage.blob import BlobServiceClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import *
from azure.search.documents import SearchClient

MAX_SECTION_LENGTH = 1000