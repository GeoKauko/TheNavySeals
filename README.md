# TheNavySeals
The working repository of the Navy Seal project

# Python Environment
Download Anaconda and use Anaconda Prompt as a terminal. Navigate using `cd` commands to the cloned Git repository on your computer. In the root folder of the project, create the environment from the `yaml` file using this command: `conda env create --file project_env.yaml`. To activate the environment, use `conda activate TheNavySeals` command.\\
\\If you add another library to the `yaml` file, you need to recreate the environment. To do this, you first deactivate the environment, with the command `conda deactivate`. This should switch to the base environment. Run command `conda info --envs` to check your current environment. The current environment should have a `*` symbol in front of it. Now you can delete TheNavySeals environment, using the command `conda env remove -n TheNavySeals`.\\
\\Once you deleted it, you recreate and reactivate it, using the commands: `conda env create --file project_env.yaml` and `conda activate TheNavySeals`.