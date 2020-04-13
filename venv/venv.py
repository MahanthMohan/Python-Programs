import sys

# Path to virtualenv
venv_path = os.path.join('/home', 'sixdays', '.virtualenvs', 'test32')

# Save old values
old_os_path = os.environ['PATH']
old_sys_path = list(sys.path)
old_sys_prefix = sys.prefix


def deactivate():
    # Change back by setting values to starting values
    os.environ['PATH'] = old_os_path
    sys.prefix = old_sys_prefix
    sys.path[:0] = old_sys_path


# Activate the virtualenvironment
activate_this = os.path.join(venv_path, 'bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))


# Print list of pip packages for virtualenv for example purpose
import pip
print str(pip.get_installed_distributions())

# Unload pip module
del pip

# Deactivate/switch back to initial interpreter
deactivate()

# Print list of initial environment pip packages for example purpose
import pip
print str(pip.get_installed_distributions())