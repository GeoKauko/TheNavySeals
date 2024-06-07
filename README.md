# TheNavySeals
The working repository of the Navy Seal project

# Python Environment
- Download Anaconda and use Anaconda Prompt as a terminal.
- Navigate using `cd` commands to the cloned Git repository on your computer.
- In the root folder of the project:
    - Create the environment from the `yaml` file: `conda env create --file project_env.yaml`
    - Activate environment: `conda activate TheNavySeals`
- When adding a library to the `yaml` file, recreate the environment:
    - Deactivate the environment: `conda deactivate`
    - Check if you are now in the `base` environment: `conda info --envs` - the base environment should have the `*` symbol in front of it
    - Delete TheNavySeals environment: `conda env remove -n TheNavySeals`
    - Recreate environment: `conda env create --file project_env.yaml`
    - Reactivate environment: `conda activate TheNavySeals`


# Git cheatsheet
## Create new branch
- Make sure you're on the main branch: `git checkout main`
- Create a new branch from main: `git checkout -b <new-branch-name> main`
- Publish branch: `git push -u origin <new-branch-name>`

## Delete branch
- Make sure you're on the main branch: `git checkout main`
- Delete branch locally: `git branch -d <branch-name>`
- Delete branch remotely: `git push origin --delete <branch-name>`

## Merge branch into main
- Make sure you're on the main branch: `git checkout main`
- Update main branch: `git pull origin main`
- Merge the branch into main: `git merge <your-branch>`
- Update the merge: `git push origin main`

