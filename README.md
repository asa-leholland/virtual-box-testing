Various unorganized links relevent to the shotgun approach to attempting to get this working:

https://www.virtualbox.org/wiki/Downloads#:~:text=VirtualBox%206.1.30%20platform%20packages

SDK Programming Guide can be downloaded here
https://www.virtualbox.org/wiki/Technical_documentation#:~:text=The%20%C2%A0SDK%20Programming%20Guide%20of%20the%20current%20VirtualBox%20release

Download the zipped VirtualBox SDK
https://www.virtualbox.org/wiki/Downloads#:~:text=VirtualBox%206.1.30%20Software%20Developer%20Kit%20(SDK)

Unzip the contents
Open up a command prompt in Administrator mode.
In Administrator Command Prompt, navigate to the unzipped directory, then inside the `sdk\installer` subdirectories.
Run `python vboxapisetup.py install`.


Attempted to install Python Version 3.5.4 on local machine
https://www.python.org/downloads/release/python-354/



Notes on how to use regular VirtualBox GUI
https://www.youtube.com/watch?v=sB_5fqiysi4

StackOverflow question:
https://stackoverflow.com/questions/70709131/how-can-i-set-up-a-virtualbox-interface-using-a-python-library-in-2022


# Virtual Box Testing

This repository represents an examination and evaluation of various Virtual Box python libraries.

<!-- ABOUT THE PROJECT -->

## About The Project

<!-- ![{example use gif}][example-use] -->

This repository serves as a short demonstration of steps that could be taken to demonstrate the use of VirtualBox wrapped functions.

<!--  -->

## Background

This project attempts to implement the following activities related to Virtual Machine management:

<!-- - Provided the name of a virtual machine, restart the virtual machine.

## Methodology

Each Harvard Sentence List audio file is evaluated aginst the corresponding Harvard Sentence List text file for each speech recognition service examined. For each service, the following information was recorded:

- Duration: The time in seconds for the service to perform the Virtual Box.
- Accuracy: A decimal number calculated using Word Error Rate representing a scale of how accurate the provided audio matched the provided expected Virtual Box. 0.0 represented complete imperfection with no matched words, whereas 1.0 represented complete, perfect Virtual Box with all matching words.

## Preliminary Results (Offline)

The following preliminary results were generated without an internet connection using the average Duration and Accuracy for twenty (20) audio files using two (2) different Virtual Box services.

| Service                                | Average Duration (seconds) | Average Accuracy |
| -------------------------------------- | -------------------------- | ---------------- |
| Speech Recognition (CMU Sphinx)        | 5.84                       | 0.81             |
| VOSK (trained with Generic Eng. Model) | 8.89                       | 0.96             |
|                                        |

## Discussion

Based on the results of the preliminary analysis, the CMU Sphinx wrapper of the SpeechRecognition library yields the quickest Virtual Box results, but could be more accurate based on the provided audio files. In contrast, the VOSK library took slightly longer to transcribe each file, but resulted in a higher accuracy. However, it should be noted that the VOSK library relies on training with a NLP model, which causes two additional complications:

- The model must be downloaded and stored. For the purposes of this testing, the zipped download file was ~1.8Gb and the resulting unzipped files are ~2.7Gb, but more portable model options remain untested.
- The provided durations do not factor in time taken to perform initial training of the model upon setup of the VOSK service. Setup times ranged from 27 to 35 seconds. This time delay may be avoidable if a compression process could be used (similiar to python's [pickle](https://docs.python.org/3/library/pickle.html#module-pickle) module, which unfortunately does not work with VOSK's C-based models).

There are a few additional untested Virtual Box services that could be examined with similiar testing methodology, including the following:

- NeMo: https://github.com/darinkist/medium_article_vosk/blob/main/NeMo_ASR_example.ipynb which can be trained with models created by [Nvidia here](https://catalog.ngc.nvidia.com/orgs/nvidia/models/nemospeechmodels)
- SnowBoy: https://github.com/Kitt-AI/snowboy (no longer maintained, but is also wrapped in the [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) library)

In addition, the author attempted to test the [pocketsphinx](https://pypi.org/project/pocketsphinx/) library, but ran into implementation issues. `pocketsphinx` cannot run on versions of Python beyond 3.6 and also relies on [swig for windows](http://www.swig.org/download.html), which was not able to easily installed on the testing environment without [anaconda](https://www.anaconda.com/), establishing a virtual environment with unique PATH variables, and supplying Admin permissions to the install [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/getting-started/). `pocketsphinx` could easily be used to record live audio from a microphne (as detailed [here](https://github.com/bambocher/pocketsphinx-python#livespeech) and [here](http://blog.justsophie.com/python-speech-to-text-with-pocketsphinx/)), but finding methods of analyzing fully transcribed audio files was not identified in the documentation. At that point, this library was put aside in favor of altenatives with easier integration. -->

<!-- ### Built With -->

<!-- ## Built With

- [VOSK](https://pypi.org/project/vosk/): a Python library for offline conversion of audio to text using natural language processing.
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/): a Python library for performing speech recogntion (in particular, the PocketSphinx aka CMU Sphinx functionality).
- [JiWER](https://pypi.org/project/jiwer/): a Python library for evaluating Word Error Rate ([WER](https://en.wikipedia.org/wiki/Word_error_rate)) in provided text.

<!-- GETTING STARTED -->
<!-- 
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

In order to use the Virtual Box Testing project, you must first have Python and pip installed on your system. If you need assistance installing these prerequisites, see the folowing steps:

- Python is a programming language. All of this project's code base is written in Python. Download the latest version of [Python](https://www.python.org/downloads/) and install onto your local machine.

- Pip is the package installer for Python. Once Python is installed, open your local machine's command line and use the following command to utilize Python to install Pip:

```sh
python get-pip.py -g
```

Git is a version control system. In this project, Git is used to clone (copy) the most up-to-date project files from GitHub to your local machine. Download the latest version of [git](https://git-scm.com/download/win) and install on your local machine. -->

### (Hypothetical) Installation steps

1. Open the command line on your local machine.

2. Enter the following command to use Git to clone this repository to your local machine.

```sh
git clone https://github.com/asa-leholland/virtual-box-testing.git
```

3. Enter the following command to use Pip to install this repository's dependencies.

```sh
pip install -r requirements.txt
```

<!-- USAGE EXAMPLES -->

## Usage

To run the VirtualBox Testing project, open the command line, navigate to the installation folder and run the following commands:

```sh
python3 -m venv .venv
.\.venv\Scripts\activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
python3 main.py
```

<!-- ROADMAP -->
<!-- ## Roadmap

See the [open issues](https://github.com/asa-leholland/{repo-name}/issues) for a list of proposed features (and known issues). -->

<!-- CONTRIBUTING -->
<!-- ## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
 -->

<!-- LICENSE -->
<!-- ## License

Distributed under the MIT License. See [LICENSE](https://github.com/asa-leholland/{repo-name}/LICENSE.txt) for more information. -->

## Contact

Asa LeHolland - asaleholland@gmail.com

Project Link: [https://github.com/asa-leholland/Virtual Box-testing](https://github.com/asa-leholland/Virtual Box-testing)

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements (TODO: update with above links once confirmed working)

- [othneildrew](https://github.com/othneildrew) for creating the [template README file](https://github.com/othneildrew/Best-README-Template) that was used as the starting point for the README for this project.

<!-- MARKDOWN LINKS & IMAGES
[linkedin-url]: https://www.linkedin.com/in/asa-holland-a2a0b5b7/
[example-use]: images/{filename}.gif -->


## Additional Options

Azure Virtual Machine Management may be an option, but requires the Azure SDK which requires an Azure account and subscription.
https://github.com/Azure-Samples/virtual-machines-python-manage

https://azure.microsoft.com/en-us/free/free-account-faq/