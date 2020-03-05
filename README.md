# ManyToOne

## Description
Python tool to convert many markup files into one master markup file, more specifically css and js. Written to work only on Windows platform at the moment.

## Instructions
1. Replace input folder with your own css and javascript files. File structure doesn't matter as long as your files are inside the input folder.
2. Activate virtual environment.
3. Run main.py
4. If no errors, success! Check the output folder. Input directory integrity should have been saved as well.

## Notice
Be aware that this is the initial build and documentation and reporting of errors are still in a work in progress. These are coming soon.

## Changelog
***March 4 2020***
- Removed duplicated code inside the Collector, favoring having a extension passed to it upon creation instead of handling them all at once.
- Changed private functions in the Collector class to public as suggested by [badge](https://www.reddit.com/r/learnpython/comments/fd8jbm/feedback_on_manytoone_file_reduction_program/fjg5ecs/)