# 1. math_operations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b

# 2. string_utils.py

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# 3. geometry/circle.py
import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius

from .circle import calculate_area, calculate_circumference

# 4. file_operations/file_reader.py

def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "File not found."

# 5. file_operations/file_writer.py

def write_file(file_path, content):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    return "File written successfully."

from .file_reader import read_file
from .file_writer import write_file

# 6. main.py
from math_operations import add, subtract, multiply, divide
from string_utils import reverse_string, count_vowels
from geometry import calculate_area, calculate_circumference
from file_operations import read_file, write_file

# Math operations
print("Add:", add(5, 3))
print("Subtract:", subtract(10, 4))
print("Multiply:", multiply(6, 7))
print("Divide:", divide(20, 5))

# String utils
print("Reversed:", reverse_string("Python"))
print("Vowel count:", count_vowels("OpenAI ChatGPT"))

# Geometry
print("Circle area:", calculate_area(5))
print("Circle circumference:", calculate_circumference(5))

# File operations
file_path = "test.txt"
write_file(file_path, "Hello, this is a test file!")
print("File content:", read_file(file_path))
