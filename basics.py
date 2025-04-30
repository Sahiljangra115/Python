{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f606737d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "console.log(\"hello\")\n"
     ]
    }
   ],
   "source": [
    "print('hello')\n",
    "print('console.log(\"hello\")')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "926c3986",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "Hoonigan\n",
      "Hoonigan\n"
     ]
    }
   ],
   "source": [
    "def chai(n):\n",
    "    print(n)\n",
    "chai(4)\n",
    "chai(\"Hoonigan\")\n",
    "chai(\"Hoonigan\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e2ef15ee",
   "metadata": {},
   "source": [
    "Python compiles to bytecode(low level and platfrom independent)\n",
    "Python is an interpreted language\n",
    "format(extension) = .pyc(frozen binaries)   ===> __pycache__\n",
    "Byte code is not a Machine Code its python specific intpretation\n",
    "Types:\n",
    "cpython, jpython, ironpython, stackless, PyPy etc.\n",
    "\n",
    "\n",
    "\n",
    "IMMUTABLE AND MUTABLE:\n",
    "immutables means if a memory refrence is created for a immutable object now the value cannot be altered an another memory refrence is generated and variable point to that refrence.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "baef90a1",
   "metadata": {},
   "source": [
    "DATA TYPES:\n",
    "1. Numer = 1234, 3.14, 3+4j, 0b101010, Decimal(), Fraction()\n",
    "2. String = 'hello', \"hello's\", b'a/x01cbc\", u'ncud/0x1'\n",
    "3. List = [1, 2, [3, '4', 'a', 5]], list(range(10)), list('hello')\n",
    "4. Tuple = (1, 2, 3, 4), tuple('hello')\n",
    "5. Set = {1, 2, 3, 4}, set('hello'), set(range(10))\n",
    "6. Dict = {'a': 1, 'b': 2, 'c': 3}, dict(a=1, b=2, c=3), dict(zip('abc', range(3)))  values/index donot start from 0\n",
    "\n",
    "===> dictionaries have key:values\n",
    "\n",
    "7. Frozenset = frozenset('hello'), frozenset(range(10))\n",
    "8. Bytes = b'hello', bytes(range(10)), bytes('hello', encoding='utf-8') \n",
    "9. Bytearray = bytearray('hello', encoding='utf-8'), bytearray(range(10))\n",
    "10. Boolean = True, False\n",
    "11. None = None\n",
    "12. file = open('file.txt', 'r'), open('file.txt', 'w'), open('file.txt', 'a'), open('file.txt', 'b')\n",
    "13. Functions, modules, classes\n",
    "14. Advance types: Decorators, generators, iterators, Metaprogramming"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f98fab87",
   "metadata": {},
   "source": [
    "Important note: the datatype is never assigned to a variable it is always assigned to a refrence in memory.\n",
    "\n",
    "Python is a number powerfull language that's why it donot collect hte refrence of a number or String immediately this is an exception in python\n",
    "and it is called as \"String interning\" and \"Number interning\" in python."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1674e969",
   "metadata": {},
   "outputs": [],
   "source": [
    "# use all these commands in python shell as it prints without print command\n",
    "username = \"Hoonigan\"\n",
    "len(username)\n",
    "username[0]\n",
    "username[-1] #it will give the last character of the string\n",
    "username[0:3] #it will start from 0th index and go upto 2nd index\n",
    "# this is called \"slicing\"\n",
    "\n",
    "# we cannot do something like below:\n",
    "#  username[0] = 'A' # it will give an error bcoz strings are immutable\n",
    "# we can do something like this:        \n",
    "username = 'A' + username[1:] # it will change the first character of the string"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "41518e2a",
   "metadata": {},
   "source": [
    "Note: the list is a muttable datatype and the below behaviour only happens in muttable datatypes\n",
    "\n",
    ">> mylist = [2,3,4,5]\n",
    ">>> mylisttwo = mylist\n",
    ">>> mylisttwo\n",
    "[2, 3, 4, 5]\n",
    ">>> mylist[0] = 54\n",
    ">>> mylisttwo\n",
    "[54, 3, 4, 5]  Here you can see that if we donot reassign the refrence of the list then the value of the list is changed\n",
    "\n",
    "\n",
    ">>> mylist = [2,3,4,5]\n",
    ">>> mylist[0] = 57\n",
    ">>> mylisttwo\n",
    "[54, 3, 4, 5]\n",
    ">>> mylist\n",
    "[57, 3, 4, 5] Here you can see if we reassign the refrence of the list then the value of the list is not changed in mylisttwo\n",
    "\n",
    "==> bcoz the reference of the list is changed and now it points to a new memory location\n",
    "\n",
    "\n",
    "Lets talk a bit more:\n",
    ">>> a = [1, 2, 3] \n",
    ">>> b = a\n",
    ">>> b\n",
    "[1, 2, 3]\n",
    ">>> b == a #we are checking if value of b is same as a\n",
    "True\n",
    ">>> b is a\n",
    "True\n",
    ">>> b = [1, 2, 3]\n",
    ">>> b == a\n",
    "True\n",
    ">>> b is a\n",
    "False"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "385d41c6",
   "metadata": {},
   "source": [
    "Important trick: The list can also be copied like below\n",
    ">>> mylist = [2,3,4,5]\n",
    ">>> mylisttwo = mylist[:] if we donot define a start point and a end point than it start from the starting point and go to the end point\n",
    ">>> mylisttwo\n",
    "[2, 3, 4, 5]\n",
    ">>> mylisttwo[0] = 54\n",
    ">>> mylisttwo\n",
    "[54, 3, 4, 5]\n",
    ">>> mylist\n",
    "[2, 3, 4, 5] \n",
    "\n",
    "\n",
    "import copy\n",
    ">>> mylist = [2,3,4,5]\n",
    ">>> mylisttwo = copy.copy(mylist)\n",
    ">>> mylisttwo = copy.deepcopy(mylist)  #deepcopy is used to copy the list and its refrence\n",
    ">>> mylisttwo\n",
    "[2, 3, 4, 5]\n",
    ">>> mylisttwo[0] = 54\n",
    ">>> mylisttwo\n",
    "[54, 3, 4, 5]\n",
    ">>> mylist\n",
    "[2, 3, 4, 5]"
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
   "version": "3.13.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
