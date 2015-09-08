# dnf-URPM

## Introduction
The dnf-URPM project aims to reimplement the URPM tool suite on top of DNF,
a next generation repository manager and dependency resolver with a
well-defined and tested CLI and API.

The hope is to implement as much of the functionality of `urpmi`, 
`urpmi.addmedia`, `urpmi.removemedia`, `urpmi.update`, 
`urpme`, `urpmq`, `urpmf`, and any other tools in the URPM tool suite
as possible on top of DNF, and potentially expose extra functionality 
that DNF provides through the urpm* command format that many people prefer.

## What is working now

* An extremely minimal implementation of `urpmi` exists as `dnf-urpmi`

## What is not working now

* Everything else
