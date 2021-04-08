"""
* What happens during execution of Python program.

* Python first compiles your source code (.py file) into a format known as byte code. Compilation is simply a translation step, and byte code is a lower-level, and platform-independent, representation of your source code.

* These are instructions similar in spirit to CPU instructions, but instead of being executed by the CPU, they are executed by software called a virtual machine.

* Compiled code is usually stored in .pyc files , and is regenerated when the source is updated, or when otherwise necessary.

* pyc files are simply the compiled python files which contain the bytecode representation of your source code.

* This byte code translation is performed to speed up the execution—byte code can be run much quicker than the original source code statements.

* Whenever a Python script is executed, the byte code is generated in memory and simply discarded when program exits.

* But, if a Python module is imported, a .pyc file for the module is generated (by default) which contains its bytecode.

* Thus, when the module is imported next time, the byte code from .pyc file is used. This makes loading of Python modules much faster because the compilation phase can be bypassed!

* In 3.2 and later, Python saves .pyc compiled byte code files in a sub-directory named __pycache__ located in the directory where your source files reside with filenames that identify the Python version that created them (e.g. script.cpython-38.pyc)

* In a CPython interpreter, The bytecode (.pyc file) is loaded into the Python runtime and interpreted by a Python Virtual Machine , which is a piece of code that reads each instruction in the bytecode and executes whatever operation is indicated. Technically, it's just the last step of what is called the Python interpreter.

* Since, pyc files contain nothing but bytecode representation of your source code, we can execute them directly (just like the normal py files)

* In order to distribute a program to people who already have Python installed, you can ship either the .py files or the .pyc files.*

* The **dis** module in the Python standard library is the disassembler that can show you Python bytecode.

* What is the difference between compilation process in java vs python.

* An important aspect of Python’s compilation to bytecode is that it’s entirely **implicit**. You never invoke a compiler, you simply run a .py file.The Python implementation compiles the files as needed.

* This is different than Java, where you have to run the Java compiler to turn Java source code into compiled class files. For this reason, Java is often called a compiled language, while Python is called an interpreted language. But both compile to bytecode, and then both execute the bytecode with a software implementation of a virtual machine.

* Python is called "interpreted" because it doesn't have an explicit compilation step, and it has an interactive prompt.

* Java requires you to run a compiler before you can run your program, and does not have an interactive prompt.

"""
