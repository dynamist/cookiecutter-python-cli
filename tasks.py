#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Invoke tasks."""
import os
import json
import shutil

from invoke import task

HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, 'cookiecutter.json'), 'r') as fp:
    COOKIECUTTER_SETTINGS = json.load(fp)
COOKIECUTTER_SETTINGS['repo_name'] = COOKIECUTTER_SETTINGS['app_title'].replace(' ','').lower()
COOKIE = os.path.join(HERE, COOKIECUTTER_SETTINGS['repo_name'])

@task
def build(ctx):
    """Build the cookiecutter."""
    ctx.run('cookiecutter {0} --no-input'.format(HERE))

@task
def clean(ctx):
    """Clean out generated cookiecutter."""
    print(COOKIE)
    if os.path.exists(COOKIE):
        shutil.rmtree(COOKIE)
        print('Removed {0}'.format(COOKIE))
    else:
        print('App directory does not exist. Skipping.')

@task(pre=[clean, build])
def test(ctx):
    """Run lint commands and tests."""
    os.chdir(COOKIE)
    ctx.run('pip install -e ."[test]"', echo=True)
    ctx.run('pytest', echo=True)
