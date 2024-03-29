---
title: Scripting Reference
layout: lab
nav_exclude: true
---

# Scripting with the Bourne-Again Shell (Bash)

While most programmers are likely familiar with `bash` in its popular capacity 
as a command line interpreter, it is in fact a powerful and full-featured 
programming language. Moreover, `bash` has a uniquely qualified claim to the 
title of _scripting_ language in that programs written in `bash` are simply 
series of shell commands which `bash` reads off and executes line-by-line. Or, 
conversely, one might say that `bash` command line entries are simply short 
one-line scripts. So really, you've been `bash` scripting all along!

## Shebang!

Shell scripts typically begin with the **shebang** line: 
`#!path/to/interpreter`.

`#!` is a human-readable representation of a [magic number][1] `0x23 0x21` 
which can tell the shell to pass execution of the rest of the file to a 
specified interpreter. If your script is run as an executable (e.g. 
`./awesome_shell_script`) with a shebang line, then the shell will invoke the 
executable (usually an interpreter) at `path/to/interpreter` to run your 
script. If your script is passed as an argument to an interpreter e.g. `bash 
awesome_shell_script`, then the shebang has no effect and `bash` will handle 
the script's execution.

**Why is this important?** The shebang line can be considered a useful piece of 
metadata which passes the concern of _how_ a script is executed from the user 
to the program's author. `awesome_shell_script` could be a `bash` script, a 
`python` script, a `ruby` script, etc. The idea is that only the script's 
behavior, not its implementation details, should matter to the user who calls 
the script.

You may have seen some variant of `#!/bin/sh`. Although initially referencing 
the Bourne shell, on modern systems `sh` has come to reference to the [Shell 
Command Language][2], which is a POSIX specification with many implementations. 
`sh` is usually symlinked to one of these POSIX-compliant shells which 
implement the Shell Command Language. On Debian, for instance, `sh` is 
symlinked to the shell `dash`. It is important to note that `bash` does **not** 
comply with this standard, although running `bash` as `bash --posix` makes it 
more compliant.

**Why is this important?** If `awesome_shell_script` uses _bashisms_ (i.e. 
non-POSIX bash-specific features) but includes a shebang line pointing to `sh`, 
then trying to run the script as an executable e.g. `./awesome_shell_script` 
will likely fail. So if you plan to use bashisms in your script, the shebang 
line should point to `bash`, not `sh`. Note that this will sacrifice 
portability, as only systems with `bash` installed will be able to execute your 
script. A list of common bashisms and specification differences between common 
shells can be found [here][13]. The commonly installed `checkbashisms` program 
can help to identify bashisms.

In contexts other than the **shebang** line, `#` indicates the beginning of a 
comment. Everything to the right of a `#` on a line will not be executed.

## Shell Variables and Types

Like most other programming languages, `bash` facilitates stateful assignment 
of names to values as variables.

Variables can be assigned in `bash` with the syntax: `NAME=value`. Note the 
lack of spaces between the assignment operator `=` and its operands. Assignment 
is whitespace-sensitive.

You can retrieve the value of a variable by prepending a `$` to it's name. 
Getting the value of `NAME` must be done with `$NAME`. This is called variable 
interpolation.

```bash
$ NAME = "Tux" # Incorrect
-bash: NAME: command not found 
$ NAME="Tux" # Correct
$ echo NAME # Incorrect. We want the value we assigned to NAME, not the text 
# NAME itself.
NAME
$ echo $NAME # Correct
Tux
```

`$?` holds the exit code of the most recently executed command. In this 
context, exit code `0` generally means that a program has executed 
successfully. Other [exit codes][14] refer to the nature of the error which 
caused the program to fail.

Special _positional parameters_ allow arguments to be passed into your script. 
`$0` is the name of the script, `$1` is the first argument passed to the 
script, `$2` is the second argument passed to the script, `$3` is the third 
argument, etc. `$#` gives the number of arguments passed to the script.

So `./awesome_shell_script foo bar` could access `foo` from `$1` and `bar` from 
`$2`.

Bash variables are _untyped_. They are usually treated as text (strings), but a 
variable can be treated as a number if it contains digits and arithmetic 
operations are applied to it. Note that this is different from most programming 
languages. _Variables_ don't have types themselves, but _operators_ will treat 
their values differently in different contexts. In other words, `bash` 
variables are text and don't have any inherent behaviors or properties beyond 
that of text which can be manipulated, but operators will interpret this text 
according to its content (digits or no digits?) and the context of the 
expression.

## Arithmetic

Bash supports integer arithmetic with the `let` builtin.

```bash
$ x=1+1
$ echo $x # Incorrect. We wanted 2, not the text 1+1.
1+1
$ let x=1+1
$ echo $x # Correct
2
```

Note that `let` is whitespace sensitive. Operands and operators must not be 
separated by spaces.

`bash` does not natively support floating point arithmetic, so we must rely on 
external utilities if we want to deal with decimal numbers. A common choice for 
this is `bc`. Fun fact: `bc` is actually it's own complete language!

We commonly access `bc` via a _pipe_ (represented as `|`), which allows the 
output of one command to be used as the input for another. We include the `-l` 
option for `bc` in order to enable floating point arithmetic.

```bash
$ echo 1/2 | bc -l
.50000000000000000000
```

## `test`

Bash scripts frequently use the `[` (a synonym for `test`) shell builtin for 
the conditional evaluation of expressions. `test` evaluates an expression and 
exits with either status code `0` (true) or status code `1` (false).

`test` supports the usual string and numeric operators, as well as a number of 
additional binary and unary operators which don't have direct analogs in most 
other programming languages. You can see a list of these operators, along with 
other useful information, by entering `help test` in your shell. The output of 
this is shown below. Note that `help` is similar to `man`, except it is used for
bash functions instead of other programs.

```
$ help test
test: test [expr]
    Exits with a status of 0 (true) or 1 (false) depending on
    the evaluation of EXPR.  Expressions may be unary or binary.  Unary
    expressions are often used to examine the status of a file.  There
    are string operators as well, and numeric comparison operators.

    File operators:

        -a FILE        True if file exists.
        -b FILE        True if file is block special.
        -c FILE        True if file is character special.
        -d FILE        True if file is a directory.
        -e FILE        True if file exists.
        -f FILE        True if file exists and is a regular file.
        -g FILE        True if file is set-group-id.
        -h FILE        True if file is a symbolic link.
        -L FILE        True if file is a symbolic link.
        -k FILE        True if file has its `sticky' bit set.
        -p FILE        True if file is a named pipe.
        -r FILE        True if file is readable by you.
        -s FILE        True if file exists and is not empty.
        -S FILE        True if file is a socket.
        -t FD          True if FD is opened on a terminal.
        -u FILE        True if the file is set-user-id.
        -w FILE        True if the file is writable by you.
        -x FILE        True if the file is executable by you.
        -O FILE        True if the file is effectively owned by you.
        -G FILE        True if the file is effectively owned by your group.
        -N FILE        True if the file has been modified since it was last 
read.

      FILE1 -nt FILE2  True if file1 is newer than file2 (according to
                       modification date).

      FILE1 -ot FILE2  True if file1 is older than file2.

      FILE1 -ef FILE2  True if file1 is a hard link to file2.

    String operators:

        -z STRING      True if string is empty.

        -n STRING
        STRING         True if string is not empty.

        STRING1 = STRING2
                       True if the strings are equal.
        STRING1 != STRING2
                       True if the strings are not equal.
        STRING1 < STRING2
                       True if STRING1 sorts before STRING2 lexicographically.
        STRING1 > STRING2
                       True if STRING1 sorts after STRING2 lexicographically.

    Other operators:

        -o OPTION      True if the shell option OPTION is enabled.
        ! EXPR         True if expr is false.
        EXPR1 -a EXPR2 True if both expr1 AND expr2 are true.
        EXPR1 -o EXPR2 True if either expr1 OR expr2 is true.

        arg1 OP arg2   Arithmetic tests.  OP is one of -eq, -ne,
                       -lt, -le, -gt, or -ge.

    Arithmetic binary operators return true if ARG1 is equal, not-equal,
    less-than, less-than-or-equal, greater-than, or greater-than-or-equal
    than ARG2.
```

We can test integer equality

```bash
$ [ 0 -eq 0 ]; echo $? # exit code 0 means true
0
$ [ 0 -eq 1 ]; echo $? # exit code 1 means false
1
```

string equality

```bash
$ [ zero = zero ]; echo $? # exit code 0 means true
0
$ [ zero = one ]; echo $? # exit code 1 means false
1
```

and a number of other string and numeric operations which you are free to 
explore.

## Flow Control

`bash` includes control structures typical of most programming languages -- 
`if-then-elif-else`, `while` `for-in`, etc. You can read more about 
[conditional statements][3] and [iteration][4] in the [Bash Guide for 
Beginners][5] from the Linux Documentation Project (LDP). You are encouraged to 
read those sections, as this guide provides only a brief summary of some 
important features.

### if-then-elif-else

The general form of an if-statement in `bash` is

```bash
if TEST-COMMANDS; then

  CONSEQUENT-COMMANDS

elif MORE-TEST-COMMANDS; then

  MORE-CONSEQUENT-COMMANDS

else 

  ALTERNATE-CONSEQUENT-COMMANDS;

fi
```

Indentation is good practice, but not required.

For example, if we write

```bash
#!/bin/bash
# contents of awesome_shell_script

if [ $1 -eq $2 ]; then
  echo args are equal
else
  echo args are not equal
fi
```

we see

```bash
$ ./awesome_shell_script 0 0
args are equal
$ ./awesome_shell_script 0 1
args are not equal
```

### while

The general form of a while loop in `bash` is

```bash
while TEST-COMMANDS; do

  CONSEQUENT-COMMANDS

done
```

If `TEST-COMMANDS` exits with status code `0`, `CONSEQUENT-COMMANDS` will 
execute. These steps will repeat until `TEST-COMMANDS` exits with some nonzero 
status.

For example, if we write

```bash
#!/bin/bash
# contents of awesome_shell_script

n=$1
while [ $n -gt 0 ]; do
  echo $n
  let n=$n-1
done
```

we see

```bash
$ ./awesome_shell_script 5
5
4
3
2
1
```

## Functions

`bash` supports functions, albeit in a crippled form relative to many other 
languages. Some notable differences include:

- Functions dont _return_ anything, they just produce output streams (e.g. 
`echo` to stdout)
- `bash` is strictly call-by-value. That is, only atomic values (strings) can 
be passed into functions.
- Variables are not lexically scoped. `bash` uses a very simple system of local 
scope which is close to dynamic scope.
- `bash` does not have first-class functions (i.e. no passing functions to 
other functions), anonymous functions, or closures.

Functions in `bash` are defined by

```bash
name_of_function() {

  FUNCTION_BODY

}
```

and called by

```bash
name_of_function $arg1 $arg2 ... $argN
```

Note the lack of parameters in the function signature. Parameters in `bash` 
functions are treated similarly to global positional parameters, with `$1` 
containing the `$arg1`, `$2` containing `$arg2`, etc.

For example, if we write

```bash
#!/bin/bash
# contents of awesome_shell_script

foo() {
  echo hello $1
}

foo $1
```

we see

```
$ ./awesome_shell_script world
hello world
```

--------------------------------------------------------------------------------

# Examples

Despite `bash`'s clumsiness, recursion and more complex programming logic are 
possible (read: painful).

```bash
#!/bin/bash
# contents of fibonacci

if [ $# -eq 0 ]; then
    echo "fibonacci needs an argument"
    exit 1
fi

fib() {
    N="$1"
    if [ -z "${N##*[!0-9]*}" ]; then
        echo "fibonacci only makes sense for nonnegative integers"
        exit 1
    fi

    if [ "$N" -eq 0 ]; then
        echo 0
    elif [ "$N" -eq 1 ]; then
        echo 1
    else
        echo $(($(fib $((N-2))) + $(fib $((N-1)))))
    fi
}

fib "$1"
```

`bash` can give us a recursive solution to finding the `n`th Fibonacci number.

```
$ ./fibonacci 10
55
```

--------------------------------------------------------------------------------

# Python for Sysadmins

Although `bash` scripts can be a simple and straightforward way to automate 
tasks involving the sequential execution of some shell commands, you may have 
already gathered that venturing beyond trivial conditional logic and simple 
functions introduces unnecessary syntactic complexity as compared to many other 
modern interpreted languages. For this reason, more complex scripts are 
popularly written in another, more general, programming language like `python`. 
Scripting with `python` is increasingly popular among sysadmins.

Countless great [tutorials][7] for learning `python` are available online. 
Alternatively, Berkeley offers several courses that teach or use `python`,
notably [CS 61A][8] and [Data 8][data8].

Adapting `python` to command-line scripting is only a matter of using relevant 
modules. Here are some tips:

- The [`argparse`][9] module in the `python` standard library is a popular way 
to implement command-line interfaces for `python` scripts
- [`fabric`][10] simplifies some sysadmin tasks, mostly in regard to 
application deployment
- [`salt`][11] is useful for general infrastructure management
- [`psutil`][12] provides an interface to system information monitoring

In practice, the decision to write a script in either `python` or `bash` is 
largely dependent on the context of the task at hand. Generally, tasks solvable 
with simple shell commands and those requiring simple file reading, writing, 
and appending are often a good fit for a `bash` script. Those with complex 
control logic, recursion, and other more general programming patterns are a 
better fit for a `python` script.

--------------------------------------------------------------------------------

[1]: https://en.wikipedia.org/wiki/Shebang_(Unix)#Magic_number
[10]: http://docs.fabfile.org/en/1.14/
[11]: https://saltstack.com/community/
[12]: https://github.com/giampaolo/psutil
[13]: https://mywiki.wooledge.org/Bashism
[14]: http://tldp.org/LDP/abs/html/exitcodes.html
[2]: http://pubs.opengroup.org/onlinepubs/009695399/utilities/xcu_chap02.html
[3]: http://tldp.org/LDP/Bash-Beginners-Guide/html/chap_07.html
[4]: http://tldp.org/LDP/Bash-Beginners-Guide/html/chap_09.html
[5]: http://tldp.org/LDP/Bash-Beginners-Guide/html/index.html
[6]: https://wiki.python.org/moin/BeginnersGuide/Programmers
[7]: http://www-inst.eecs.berkeley.edu/~selfpace/python/
[8]: https://cs61a.org
[9]: https://docs.python.org/3/library/argparse.html
[data8]: http://data8.org/