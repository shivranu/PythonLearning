# Find all occurrences of the word "python" in a given text using Python's re module

import re

# Define the text
text = ("Python is a high level ,object oriented programming language."
        " I love Python because it's easy to learn and use."
        "Python has a huge community and many libraries.")

pattern = r'\bpython\b'
matches = re.findall(pattern, text, re.IGNORECASE)
print(matches)