##  **A Simple Language Compiler**

This document describes a Python program that implements a compiler for a very simple language. The language allows you to declare variables (`ye`), assign values to them (`=`), and print them (`bol`).

###  **Files**

The code consists of four main functions spread across two Python files:

* `lexer.py`: Contains the `lexer` function which takes the source code as input and breaks it down into tokens (keywords, identifiers, operators, numbers).
* `compiler.py`: Contains the remaining three functions (`parser`, `codegen`, and `compiler`).
    * `parser`: Takes a list of tokens from the lexer and builds an Abstract Syntax Tree (AST) representing the program structure.
    * `codegen`: Takes the AST and generates executable Python code.
    * `compiler`: The main function that ties everything together. It calls the lexer, parser, and code generator to compile the source code.

###  **Running the Compiler**

1. Save the code in two files named `lexer.py` and `compiler.py`.
2. The source code is defined within a variable named `code` in `compiler.py`. You can modify this string to represent your program. 3. Run the script:

```bash
python compiler.py
```

This will execute the compiled code.

###  **Example**

The provided code snippet demonstrates a simple program that declares two variables (`x` and `y`), assigns them values, calculates their sum, and then prints the result.

**Source Code:**

```python
ye x = 10
ye y = 20
ye sum = x + y
bol sum
```

**Compiled and Executed Code:**

```python
print(x + y)
```

This will print the value `30`.

###  **Limitations**

This is a very basic compiler and has several limitations:

* It only supports a small subset of language constructs (variable declaration, assignment, printing).
* It does not perform any error checking beyond variable assignment.

This code serves as a simple example of how a compiler works and can be a foundation for building more complex language processors.
