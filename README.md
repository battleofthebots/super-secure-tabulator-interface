# Super Secure Tabulator Interface

A calculator is a secure program to implement server side right?

`app.py`

## Build and Run

``` shell
docker build . -t super
docker run -p 80:80 super
```

# Solving

As it is, this challenge is incredibly easy. To make it more difficult, different validations could be run on the equation parameter's input to check if it has banned characters, or to check if it returns an integer

This challenge requires solvers to realize that any user input passed into the equation parameter is rendered using Jinja2's templating engine, and can lead to command execution.

To get command execution, one needs to get access to the python 'object' class, which allows the user to access all of the defined python classes (by calling `__subclasses__()` on the object class), instead of the few made available in the sandbox. From there, they are able to access the subprocess.Popen class, which allows for ACE.
Example payload:
`request.application.__globals__.__builtins__.__import__('os').popen('ls').read()`

## Troubleshooting

#### Have they identified that the server is run with flask?
This is done by looking at the Response headers indicating it's a python webapp

#### Have they identified that the equation parameter is vulnerable to SSTI?
This is done by putting in invalid math operations and noticing that any invalid python operation results in a 500 error, while valid python statements such as 'test' result in the string test being returned.

#### Are they copy and pasting payloads from online?
Remind them that every machine is different and to look at how the payload is constructed. The reason why online payloads don't work is because depending on which packages are imported, the index of the subprocess. Popen class is different.