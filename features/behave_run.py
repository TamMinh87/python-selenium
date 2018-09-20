from behave import configuration
from behave import __main__

# Adding my wanted option to parser.
configuration.parser.add_argument('-u', '--url', help="Address of your url")

# command that run behave.
__main__.main()