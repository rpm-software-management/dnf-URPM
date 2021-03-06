# dnf-URPM

## Introduction
The dnf-URPM project aims to reimplement the URPM tool suite on top of 
[DNF](http://dnf.baseurl.org/), a next generation repository manager 
and dependency resolver with a well-defined and tested CLI and API.

The hope is to implement as much of the functionality of `urpmi`, 
`urpmi.update`, `urpme`, `urpmq`, and `urpmf` as possible on top of DNF.

## What is working now

* An extremely minimal implementation of `urpmi` exists as `dnf-urpmi`
* An extremely minimal implementation of `urpme` exists as `dnf-urpme`

## What is not working now

* Everything else

## More information

### DNF information

* [DNF documentation](http://dnf.readthedocs.org/en/latest/)
* [DNF core plugins documentation](http://dnf-plugins-core.readthedocs.org/en/latest/)
* [DNF extras plugins documentation](http://dnf-plugins-extras.readthedocs.org/en/latest/)

### URPM information

* urpm* man pages