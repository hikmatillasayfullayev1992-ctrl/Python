{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cda97ad4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original List: [12.23, 13.32, 100, 36.32]\n",
      "One-dimensional NumPy array: [ 12.23  13.32 100.    36.32]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# 1. Convert List to 1D Array\n",
    "lst = [12.23, 13.32, 100, 36.32]\n",
    "arr1 = np.array(lst)\n",
    "print(\"Original List:\", lst)\n",
    "print(\"One-dimensional NumPy array:\", arr1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d94745fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2. Create 3x3 Matrix (2–10)\n",
    "matrix = np.arange(2, 11).reshape(3, 3)\n",
    "print(\"\\n3x3 matrix with values from 2 to 10:\\n\", matrix)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ab16363d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 3. Null Vector (10) & Update Sixth Value\n",
    "vec = np.zeros(10)\n",
    "print(\"\\nNull vector:\", vec)\n",
    "vec[5] = 11\n",
    "print(\"Update sixth value to 11:\", vec)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "75a2793a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 4. Array from 12 to 38\n",
    "arr2 = np.arange(12, 38)\n",
    "print(\"\\nArray with values from 12 to 38:\", arr2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "17a1e3c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 5. Convert Array to Float Type\n",
    "arr3 = np.array([1, 2, 3, 4])\n",
    "arr_float = arr3.astype(float)\n",
    "print(\"\\nOriginal array:\", arr3)\n",
    "print(\"Array converted to float:\", arr_float)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c7a180de",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 6. Celsius to Fahrenheit Conversion\n",
    "C = np.array([0, 12, 45.21, 34, 99.91])\n",
    "F = C * 9/5 + 32\n",
    "print(\"\\nValues in Centigrade degrees:\", C)\n",
    "print(\"Values in Fahrenheit degrees:\", F)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0f7cfcf1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 7. Append Values to Array\n",
    "arr4 = np.array([10, 20, 30])\n",
    "arr_appended = np.append(arr4, [40, 50, 60, 70, 80, 90])\n",
    "print(\"\\nOriginal array:\", arr4)\n",
    "print(\"After append:\", arr_appended)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8cb42527",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 8. Array Statistical Functions\n",
    "arr5 = np.random.rand(10)\n",
    "print(\"\\nRandom array:\", arr5)\n",
    "print(\"Mean:\", np.mean(arr5))\n",
    "print(\"Median:\", np.median(arr5))\n",
    "print(\"Standard Deviation:\", np.std(arr5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dd66d91e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 9. Min and Max in 10x10 Random Array\n",
    "arr6 = np.random.rand(10, 10)\n",
    "print(\"\\n10x10 random array:\\n\", arr6)\n",
    "print(\"Min:\", arr6.min())\n",
    "print(\"Max:\", arr6.max())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3bff4096",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 10. 3x3x3 Random Array\n",
    "arr7 = np.random.rand(3, 3, 3)\n",
    "print(\"\\n3x3x3 random array:\\n\", arr7)"
   ]
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
