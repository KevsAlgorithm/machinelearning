{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy\n",
    "\n",
    "def upshift(a,index,n):\n",
    "    col = []\n",
    "    for j in range(len(a)):\n",
    "        col.append(a[j][index])\n",
    "    shiftCol = numpy.roll(col,-n)\n",
    "    for i in range(len(a)):\n",
    "        for j in range(len(a[0])):\n",
    "            if(j==index):\n",
    "                a[i][j] = shiftCol[i]\n",
    "\n",
    "def downshift(a,index,n):\n",
    "    col = []\n",
    "    for j in range(len(a)):\n",
    "        col.append(a[j][index])\n",
    "    shiftCol = numpy.roll(col,n)\n",
    "    for i in range(len(a)):\n",
    "        for j in range(len(a[0])):\n",
    "            if(j==index):\n",
    "                a[i][j] = shiftCol[i]\n",
    "\n",
    "def rotate180(n):\n",
    "    bits = \"{0:b}\".format(n)\n",
    "    return int(bits[::-1], 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
