from setuptools import setup, find_packages

setup(
    name='mkdocs-step-helper-plugin',
    version='0.0.1',
    description='An MkDocs plugin',
    long_description='An MkDocs plugin that automagically generates step numbers in markdown pages',
    entry_points={
        'mkdocs.plugins': [
            'step_helper = step_helper.plugin:StepHelperPlugin',
        ]
    }
)