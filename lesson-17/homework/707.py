{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0b735fec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "First 3 rows:\n",
      "   first_name  age           City\n",
      "0      Alice   25       New York\n",
      "1        Bob   30  San Francisco\n",
      "2    Charlie   35    Los Angeles\n",
      "\n",
      "Mean age: 32.5\n",
      "\n",
      "Name and City:\n",
      "   first_name           City\n",
      "0      Alice       New York\n",
      "1        Bob  San Francisco\n",
      "2    Charlie    Los Angeles\n",
      "3      David        Chicago\n",
      "\n",
      "DataFrame with Salary:\n",
      "   first_name  age           City  Salary\n",
      "0      Alice   25       New York    4860\n",
      "1        Bob   30  San Francisco    9390\n",
      "2    Charlie   35    Los Angeles    9226\n",
      "3      David   40        Chicago    9191\n",
      "\n",
      "Summary statistics:\n",
      "              age       Salary\n",
      "count   4.000000     4.000000\n",
      "mean   32.500000  8166.750000\n",
      "std     6.454972  2206.206001\n",
      "min    25.000000  4860.000000\n",
      "25%    28.750000  8108.250000\n",
      "50%    32.500000  9208.500000\n",
      "75%    36.250000  9267.000000\n",
      "max    40.000000  9390.000000\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "# Dataset\n",
    "data = {\n",
    "    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],\n",
    "    'Age': [25, 30, 35, 40],\n",
    "    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']\n",
    "}\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "# 1. Rename columns\n",
    "df.rename(columns={'First Name': 'first_name', 'Age': 'age'}, inplace=True)\n",
    "\n",
    "# 2. Print first 3 rows\n",
    "print(\"First 3 rows:\\n\", df.head(3))\n",
    "\n",
    "# 3. Mean age\n",
    "print(\"\\nMean age:\", df['age'].mean())\n",
    "\n",
    "# 4. Select and print 'first_name' and 'City'\n",
    "print(\"\\nName and City:\\n\", df[['first_name', 'City']])\n",
    "\n",
    "# 5. Add random Salary column\n",
    "np.random.seed(42)  \n",
    "df['Salary'] = np.random.randint(4000, 10000, size=len(df))\n",
    "print(\"\\nDataFrame with Salary:\\n\", df)\n",
    "\n",
    "# 6. Summary statistics\n",
    "print(\"\\nSummary statistics:\\n\", df.describe())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c7c0bbb8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Max Sales: 8000\n",
      "Max Expenses: 4500\n",
      "Min Sales: 5000\n",
      "Min Expenses: 3000\n",
      "Average Sales: 6625.0\n",
      "Average Expenses: 3750.0\n"
     ]
    }
   ],
   "source": [
    "\n",
    "\n",
    "# Dataset\n",
    "data = {\n",
    "    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],\n",
    "    'Sales': [5000, 6000, 7500, 8000],\n",
    "    'Expenses': [3000, 3500, 4000, 4500]\n",
    "}\n",
    "sales_and_expenses = pd.DataFrame(data)\n",
    "\n",
    "# 1. Maximum sales and expenses\n",
    "print(\"Max Sales:\", sales_and_expenses['Sales'].max())\n",
    "print(\"Max Expenses:\", sales_and_expenses['Expenses'].max())\n",
    "\n",
    "# 2. Minimum sales and expenses\n",
    "print(\"Min Sales:\", sales_and_expenses['Sales'].min())\n",
    "print(\"Min Expenses:\", sales_and_expenses['Expenses'].min())\n",
    "\n",
    "# 3. Average sales and expenses\n",
    "print(\"Average Sales:\", sales_and_expenses['Sales'].mean())\n",
    "print(\"Average Expenses:\", sales_and_expenses['Expenses'].mean())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "529c6c7b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Max per Category:\n",
      " Category\n",
      "Rent             1500\n",
      "Utilities         250\n",
      "Groceries         350\n",
      "Entertainment     180\n",
      "dtype: int64\n",
      "\n",
      "Min per Category:\n",
      " Category\n",
      "Rent             1200\n",
      "Utilities         200\n",
      "Groceries         300\n",
      "Entertainment     150\n",
      "dtype: int64\n",
      "\n",
      "Average per Category:\n",
      " Category\n",
      "Rent             1350.0\n",
      "Utilities         227.5\n",
      "Groceries         325.0\n",
      "Entertainment     165.0\n",
      "dtype: float64\n"
     ]
    }
   ],
   "source": [
    "\n",
    "# Dataset\n",
    "data = {\n",
    "    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],\n",
    "    'January': [1200, 200, 300, 150],\n",
    "    'February': [1300, 220, 320, 160],\n",
    "    'March': [1400, 240, 330, 170],\n",
    "    'April': [1500, 250, 350, 180]\n",
    "}\n",
    "expenses = pd.DataFrame(data)\n",
    "\n",
    "# Set index to Category\n",
    "expenses = expenses.set_index('Category')\n",
    "\n",
    "# 1. Maximum expense per category\n",
    "print(\"Max per Category:\\n\", expenses.max(axis=1))\n",
    "\n",
    "# 2. Minimum expense per category\n",
    "print(\"\\nMin per Category:\\n\", expenses.min(axis=1))\n",
    "\n",
    "# 3. Average expense per category\n",
    "print(\"\\nAverage per Category:\\n\", expenses.mean(axis=1))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a94b4733",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "effd3eac",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
