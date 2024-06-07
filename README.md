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
