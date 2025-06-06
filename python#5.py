{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ff022509-b09d-4d98-b91a-520cdb44be5d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the filename:  sample.txt\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "File contents:\n",
      " Hello World!\n",
      "This is a sample file.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "filename = input(\"Enter the filename: \")\n",
    "try:\n",
    "    with open(filename, 'r') as file:\n",
    "        content = file.read()\n",
    "        print(\"File contents:\\n\", content)\n",
    "except FileNotFoundError:\n",
    "    print(\"The file does not exist.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "71b49db1-de2a-47cb-bb19-593ff51b92b0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the source filename:  sample.txt\n",
      "Enter the destination filename:  copy.txt\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "File copied successfully.\n"
     ]
    }
   ],
   "source": [
    "source = input(\"Enter the source filename: \")\n",
    "destination = input(\"Enter the destination filename: \")\n",
    "\n",
    "try:\n",
    "    with open(source, 'r') as src_file:\n",
    "        content = src_file.read()\n",
    "    with open(destination, 'w') as dest_file:\n",
    "        dest_file.write(content)\n",
    "    print(\"File copied successfully.\")\n",
    "except FileNotFoundError:\n",
    "    print(\"Source file not found.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "22099225-224c-473b-ad4b-58351aab5837",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the filename:  words.txt\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total number of words: 7\n"
     ]
    }
   ],
   "source": [
    "filename = input(\"Enter the filename: \")\n",
    "try:\n",
    "    with open(filename, 'r') as file:\n",
    "        content = file.read()\n",
    "        words = content.split()\n",
    "        print(\"Total number of words:\", len(words))\n",
    "except FileNotFoundError:\n",
    "    print(\"File not found.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "95e6cc91-57e5-41b1-a375-5517f4054172",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  70102\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Converted integer: 70102\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    user_input = input(\"Enter a number: \")\n",
    "    number = int(user_input)\n",
    "    print(\"Converted integer:\", number)\n",
    "except ValueError:\n",
    "    print(\"Invalid input! Please enter a valid integer.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3fcd6594-6339-49c9-b8de-14f7f87a6f82",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a list of integers separated by space:  1 2 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "All integers are non-negative.\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    numbers = list(map(int, input(\"Enter a list of integers separated by space: \").split()))\n",
    "    for num in numbers:\n",
    "        if num < 0:\n",
    "            raise ValueError(\"Negative integers are not allowed.\")\n",
    "    print(\"All integers are non-negative.\")\n",
    "except ValueError as ve:\n",
    "    print(\"Error:\", ve)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "373ee07f-5a47-450a-a443-c77cda9cd32d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a list of integers separated by space:  7 9 2 4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Average: 5.5\n",
      "Program has finished running.\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    numbers = list(map(int, input(\"Enter a list of integers separated by space: \").split()))\n",
    "    average = sum(numbers) / len(numbers)\n",
    "    print(\"Average:\", average)\n",
    "except ZeroDivisionError:\n",
    "    print(\"Cannot compute average of empty list.\")\n",
    "except ValueError:\n",
    "    print(\"Please enter only integers.\")\n",
    "finally:\n",
    "    print(\"Program has finished running.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "700c035e-5e65-4f50-98eb-15f17d0ca9a9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the filename to write to:  output.txt\n",
      "Enter the text to write:  This is 5th assignment using Python\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome! The text has been written to the file.\n"
     ]
    }
   ],
   "source": [
    "filename = input(\"Enter the filename to write to: \")\n",
    "text = input(\"Enter the text to write: \")\n",
    "\n",
    "try:\n",
    "    with open(filename, 'w') as file:\n",
    "        file.write(text)\n",
    "    print(\"Welcome! The text has been written to the file.\")\n",
    "except Exception as e:\n",
    "    print(\"An error occurred:\", e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d3363fd0-b26e-47a8-b170-225b411928b2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
