import pkg_resources
from subprocess import call

installed = pkg_resources.working_set
for dist in installed:
    call("pip install --upgrade " + dist.project_name, shell=True)
