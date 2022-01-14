# Python Project Template
Short template for python projects 

https://www.virtualbox.org/wiki/Downloads#:~:text=VirtualBox%206.1.30%20platform%20packages

# Transcription Testing
This repository represents an examination and evaluation of various transcription services and APIs.


<!-- ABOUT THE PROJECT -->
## About The Project

<!-- ![{example use gif}][example-use] -->

This repository serves as a short demonstration of steps that could be taken to demonstrate the accuracy of a speech recognition service. 

**Note: The Transcription Testing project only supports the Windows platform at the moment. However, the author intends to perform similiar testing using alternate operating systems using the [Oracle VirtualBox](https://www.virtualbox.org/) tool. **


<!--  -->
## Sources of Sample Audio
This project utilizes sample audio generated from a subset of 20 lists taken from [the Harvard Sentences](https://en.wikipedia.org/wiki/Harvard_sentences), a compilation of sample phrases used as a standard for efficacy evaluation of audio-based systems, such as cellular networks. Each list consists of phonetically balanced sentences which consist of specific phoneme (speech component) frequencies matching those that appear in the spoken English language.

Harvard sentence `.wav` audio files were obtained from an open souce library [here](https://www.voiptroubleshooter.com/open_speech/american.html), and the `.txt` transcripts of those files are copied from Columbia University's Harvard Sentence documentation [here](https://www.cs.columbia.edu/~hgs/audio/harvard.html).

## Methodology

Each Harvard Sentence List audio file is evaluated aginst the corresponding Harvard Sentence List text file for each speech recognition service examined. For each service, the following information was recorded:
* Duration: The time in seconds for the service to perform the transcription.
* Accuracy: A decimal number calculated using Word Error Rate representing a scale of how accurate the provided audio matched the provided expected transcription. 0.0 represented complete imperfection with no matched words, whereas 1.0 represented complete, perfect transcription with all matching words.

## Preliminary Results (Offline)

The following preliminary results were generated without an internet connection using the average Duration and Accuracy for twenty (20) audio files using two (2) different transcription services.

| Service                                | Average Duration (seconds) | Average Accuracy |
| -------------------------------------- | -------- | -------- |
| Speech Recognition (CMU Sphinx)        | 5.84     | 0.81     |
| VOSK (trained with Generic Eng. Model) | 8.89     | 0.96     |
|                                        |



## Discussion
Based on the results of the preliminary analysis, the CMU Sphinx wrapper of the SpeechRecognition library yields the quickest transcription results, but could be more accurate based on the provided audio files. In contrast, the VOSK library took slightly longer to transcribe each file, but resulted in a higher accuracy. However, it should be noted that the VOSK library relies on training with a NLP model, which causes two additional complications:
* The model must be downloaded and stored. For the purposes of this testing, the zipped download file was ~1.8Gb and the resulting unzipped files are ~2.7Gb, but more portable model options remain untested.
* The provided durations do not factor in time taken to perform initial training of the model upon setup of the VOSK service. Setup times ranged from 27 to 35 seconds. This time delay may be avoidable if a compression process could be used (similiar to python's [pickle](https://docs.python.org/3/library/pickle.html#module-pickle) module, which unfortunately does not work with VOSK's C-based models).

There are a few additional untested transcription services that could be examined with similiar testing methodology, including the following:
* NeMo: https://github.com/darinkist/medium_article_vosk/blob/main/NeMo_ASR_example.ipynb which can be trained with models created by [Nvidia here](https://catalog.ngc.nvidia.com/orgs/nvidia/models/nemospeechmodels)
* SnowBoy: https://github.com/Kitt-AI/snowboy (no longer maintained, but is also wrapped in the [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) library)

In addition, the author attempted to test the [pocketsphinx](https://pypi.org/project/pocketsphinx/) library, but ran into implementation issues. `pocketsphinx` cannot run on versions of Python beyond 3.6 and also relies on [swig for windows](http://www.swig.org/download.html), which was not able to easily installed on the testing environment without [anaconda](https://www.anaconda.com/), establishing a virtual environment with unique PATH variables, and supplying Admin permissions to the install [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/getting-started/). `pocketsphinx` could easily be used to record live audio from a microphne (as detailed [here](https://github.com/bambocher/pocketsphinx-python#livespeech) and [here](http://blog.justsophie.com/python-speech-to-text-with-pocketsphinx/)), but finding methods of analyzing fully transcribed audio files was not identified in the documentation. At that point, this library was put aside in favor of altenatives with easier integration.



<!-- ### Built With -->

## Built With
* [VOSK](https://pypi.org/project/vosk/): a Python library for offline conversion of audio to text using natural language processing.
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/): a Python library for performing speech recogntion (in particular, the PocketSphinx aka CMU Sphinx functionality).
* [JiWER](https://pypi.org/project/jiwer/): a Python library for evaluating Word Error Rate ([WER](https://en.wikipedia.org/wiki/Word_error_rate)) in provided text.

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

In order to use the Transcription Testing project, you must first have Python and pip installed on your system. If you need assistance installing these prerequisites, see the folowing steps:
* Python is a programming language. All of this project's code base is written in Python. Download the latest version of [Python](https://www.python.org/downloads/) and install onto your local machine.

* Pip is the package installer for Python. Once Python is installed, open your local machine's command line and use the following command to utilize Python to install Pip:
```sh
python get-pip.py -g
```

Git is a version control system. In this project, Git is used to clone (copy) the most up-to-date project files from GitHub to your local machine. Download the latest version of [git](https://git-scm.com/download/win) and install on your local machine.


### Installation

1. Open the command line on your local machine.

2. Enter the following command to use Git to clone this repository to your local machine.
```sh
git clone https://github.com/asa-leholland/transcription-testing.git
```
3. Enter the following command to use Pip to install this repository's dependencies.
```sh
pip install -r requirements.txt
```
4. To use the VOSK library, you must also download an audio dataset to train the NLP model. The author used `vosk-model-en-us-0.22.zip` available [here](https://alphacephei.com/vosk/models). This was extracted into a `\dependencies` folder in the root directory of this project.



<!-- USAGE EXAMPLES -->
## Usage

To run the Transcription Testing project, open the command line, navigate to the installation folder and run the following commands:


```sh
python3 -m venv .venv 
.\.venv\Scripts\activate
python3 transcriptionTesting.py
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


# Additional Testing
Initially, a few additional services were examined, but since they required internet connection access to the APIs, further analysis was not performed. Following are the results of this additional testing. 

## Preliminary Results (Connection Required)

The following preliminary results were generated using the average Duration and Accuracy for twenty (20) audio files using two (2) different transcription services.

| Service                            | Average Duration | Average Accuracy |
| ---------------------------------- | -------- | -------- |
| SpeechRecognition.recognize_google | 3.09     | 0.99     |
| google-cloud-speech                | 4.44     | 0.16     |
|                                    |

## Discussion of Additional Results
Based on the results of the preliminary analysis, the recognize_google method of the SpeechRecognition library yields both the highest average accuracy and the shortest average duration for transcription processes using the provided audio files. However, it should be noted that the average accuracy result of the google-cloud-speech service is based on the provided audio files alone. In all twenty (20) of the provided audio files, google-cloud-speech stopped transcribing after encountering the pause following the first sentence of each recording. It may be possible to improve the accuracy of the google-cloud-speech by introducing pre-processing using white noise so that the silence does not prematurely cause transcription to end.

There are several additional transcription services that could be examined with similiar testing methodology, including the following:
* apiai: https://pypi.org/project/apiai/
* assemblyai: https://pypi.org/project/assemblyai/
* watson-developer-cloud: https://pypi.org/project/watson-developer-cloud/
* wit: https://pypi.org/project/wit/


In addition, the [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) library provides additional wrappers for the followiing untested transcription services:

* [Google Cloud Speech API](https://cloud.google.com/speech-to-text)
* [Wit.ai](https://wit.ai/)
* [Microsoft Bing Voice Recognition](https://azure.microsoft.com/en-us/services/cognitive-services/speech-services/)
* [Houndify API](https://www.houndify.com/)
* [IBM Speech to Text](https://www.ibm.com/thought-leadership/smart/)

<!-- ### Built With -->

## Additional Testing was Built With
* [Google Cloud Speech-to-Text](https://pypi.org/project/google-cloud-speech/): a Python library for converting audio to text using neural network models. More details can be found on the [Google API documentation](https://cloud.google.com/speech-to-text). 
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/): a Python library for performing speech recogntion (in particular, the Google Cloud Speech API).

<!-- CONTACT -->
## Contact

Asa LeHolland - asaleholland@gmail.com

Project Link: [https://github.com/asa-leholland/transcription-testing](https://github.com/asa-leholland/transcription-testing)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [othneildrew](https://github.com/othneildrew) for creating the [template README file](https://github.com/othneildrew/Best-README-Template) that was used as the starting point for the README for this project. 
* [David Amos](https://realpython.com/team/damos/) for his overview article with the Real Python organzition on [speech recognition and the SpeechRecognition package](https://realpython.com/python-speech-recognition/). 
* [Konstantin Rink](https://konstantin-rink.medium.com/) for [his tutorial on Real Data Science](https://towardsdatascience.com/transcribe-large-audio-files-offline-with-vosk-a77ee8f7aa28) on how to use the VOSK toolset.
* [AlphaCephei](https://alphacephei.com/) for providing OpenSource [audio model datasets](https://alphacephei.com/vosk/models) used to train VOSK.
* [Jie Jenn](https://www.youtube.com/c/JieJenn/about) for his Youtube video introduction to the [Google Cloud Speech-To-Text API](https://www.youtube.com/watch?v=lKra6E_tp5U). 






<!-- MARKDOWN LINKS & IMAGES
[linkedin-url]: https://www.linkedin.com/in/asa-holland-a2a0b5b7/
[example-use]: images/{filename}.gif -->
