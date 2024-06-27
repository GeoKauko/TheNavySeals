# TheNavySeals
The working repository of the Navy Seal project.

## Setting up the project for detection of seals using the UI
Follow these steps to use the application to detect seals on panchromatic images with a 30cm resolution.

### Set up the environment in Google Colab
To use the app in Google Colab

### Set up the environment locally
- Clone the GIT repository from https://github.com/GeoKauko/TheNavySeals.git on your local drive
- Set up the environment using [Anaconda](https://www.anaconda.com/download)
    - Open Anaconda Prompt
    - Navigate to your the root folder of your project directory
    - Create the environment from the `yaml` file: `conda env create --file project_env.yaml`
- Open the project from your preferred IDE and activate the environment "TheNavySeals"

### Start the app
- Run the 2_Postprocessing.ipynb up until folder creation
- Download [SealNN](https://drive.google.com/file/d/1IWb0OrisF4eLZvCWTsA2GrMwPeBPcd3M/view?usp=drive_link) and save it in the "TheNavySeals/data/2_deep_learning/2b_final_model
- Run the rest of the code until the app opens up
- Select your image and press process
- The app will tell you when the image is done processing and the location of the output heatmap and predicted mask 
