#!/bin/bash

# This script handles some basic QA checks on the source

TERM=${TERM:="xterm-256color"}

success() {
	echo -e "$(tput setaf 2)$1$(tput sgr0)"
}

inform() {
	echo -e "$(tput setaf 6)$1$(tput sgr0)"
}

warning() {
	echo -e "$(tput setaf 1)$1$(tput sgr0)"
}
inform "Checking for trailing whitespace..."
if grep -IUrn --color "[[:blank:]]$" --exclude-dir=dist --exclude-dir=.tox --exclude-dir=.git --exclude=PKG-INFO; then
    warning "Trailing whitespace found!"
    exit 1
else
    success "No trailing whitespace found."
fi
printf "\n"

inform "Checking for DOS line-endings..."
if grep -lIUrn --color $'\r' --exclude-dir=dist --exclude-dir=.tox --exclude-dir=.git --exclude=Makefile; then
    warning "DOS line-endings found!"
    exit 1
else
    success "No DOS line-endings found."
fi
printf "\n"
