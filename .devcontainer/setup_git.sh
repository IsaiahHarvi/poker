#!/bin/bash

gh auth login --with-token < ~/.github-token
gh auth status || echo "GitHub auth failed, check your permissions."