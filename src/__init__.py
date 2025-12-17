"""
Rick & Morty ETL pipeline Package
"""

__version__ = '0.1.0'
__author__ = 'Taghred'

from .etl_pipeline import main_request,get_all_characters
from .database.connection import db_connection, test_connection
