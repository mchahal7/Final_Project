# Tweet Hashtag Analysis Program

import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample data: list of tweets
tweets = [
    "Learning Python is fun! #coding #python",
    "INST126 gives you a good introduction to Python! #coding #python #datascience",
    "Data science with #python is cool #datascience #coding",
    "Matplotlib makes plotting easy! #python #matplotlib",
    "#numpy is powerful for numerical computations #python",
    "Regular expressions in #python #coding"
]