# lightnovels
Setup guide:

## Updating a repository
1. This is assuming you have an empty repository with the git_folder_handler.py and pdf_folder_maker.py
2. `git init`
3. `git remote add origin [enter remote link here]`
4. Set chunk size in `git_folder_handler.py` to your desired amount TOOD() file amt rather  than div
5. Run `git_folder_handler.py`
6. The program will prompt you if you wish to stop, and if not continue chunking through your entire repository.

## Adding new light novels
1. Create a folder named ".queue" inside the repo.
2. Add any light novels to this .queue folder
3. Run `pdf_folder_maker.py`
4. This will create new folders associated with those light novels in the .queue folder.
5. TOOD() Above behavior should add to similar title folders, rather than creating a new folder
