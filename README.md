# Super Secure Tabulator Interface

# NOTE
As it is, this challenge is incredibly easy. To make it more difficult, different validations could be run on the equation parameter's input to check if it has banned characters, or to check if it returns an integer

This challenge requires solvers to realize that any user input passed into the equation parameter is rendered using Jinja2's templating engine, and can lead to command execution.

## Infra

The container installs flask to an Ubuntu 20.04 image, and hosts a super simple calculator app on port 80. 

## Solution

To get command execution, one needs to get access to the python 'object' class, which allows the user to access all of the defined python classes (by calling `__subclasses__()` on the object class), instead of the few made avalible in the sandbox. From there, they are able to access the subprocess.Popen class, which allows for ACE.
Example payload:
`equation=''.__class__.mro()[-1].__subclasses__()[301]('id', shell=True, stdout=-1).communicate()[0]`

## Troubleshooting

#### Have they identified that the server is run with flask?
This is done by looking at the Response headers indicating it's a python webapp

#### Have they identified that the equation parameter is vulnerable to SSTI?
This is done by putting in invalid math operations and noticing that any invalid python operation results in a 500 error, while valid python statements such as 'test' result in the string test being returned.

#### Are they copy and pasting payloads from online?
Remind them that every machine is different and to look at how the payload is constructed. The reason why online payloads don't work is because depending on which packages are imported, the index of the subprocess.Popen class is different.