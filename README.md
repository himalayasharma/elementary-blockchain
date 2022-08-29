<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a>
    <img src="readme-assets/blockchain.jpg" alt="Logo">
  </a>

  <h1 align="center">Elementary blockchain</h1>
</div>

<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/himalayasharma/elementary-blockchain?style=social"> <img alt="GitHub forks" src="https://img.shields.io/github/forks/himalayasharma/elementary-blockchain?style=social"> <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/himalayasharma/elementary-blockchain"> <img alt="GitHub issues" src="https://img.shields.io/github/issues-raw/himalayasharma/elementary-blockchain">

A simple demonstration of how the blockchain words.

Checkout the web application [here](https://elementary-blockchain.herokuapp.com/).

NOTE: There could be some issues when viewing the current blockchain after mining/modifying a block. This is due to the browser cache. You can use the "Reset blockchain" button or alternatively open the app in incognito mode.

Project Organization
------------

    ├── LICENSE
    ├── Makefile              <- Makefile with commands like `make create_environment` or `make requirements`
    ├── README.md             <- The top-level README for developers using this project
    ├── readme-assets         <- Contains images to be used in README.md
    ├── static               
    │   └── css               <- Contains stylesheet for styling webpage
    │
    ├── templates             <- Contains html templates to be rendered
    ├── requirements.txt      <- The requirements file for reproducing the project environment
    ├── test_environment.py   <- Script to test virtual environment
    ├── blockchain.py         <- Contains blockchain class
    ├── Procfile              <- Deployment specific requirement (for Heroku)
    └── app.py                <- Contains code for application
    
Prerequisites
------------
Before you begin, ensure you have met the following requirements:
* You have a `Linux/Mac/Windows` machine.
* You have installed a `python` distribution. `conda` is preferred.
* You have installed `pip`.
* You have installed `make`.

Setup
------------
1. Clone the repo
	```
	git clone https://github.com/himalayasharma/elementary-blockchain.git
	```
2. Traverse into project directory.
3. Create virtual environment.
	```make
	make create_environment
	```
4. Activate virtual environment.
5. Download and install all required packages.
	```make
	make requirements
	```
6. Start application (in debug mode).
	```make
    make app
	```

Web Application Screenshots
------------

Screenshot 1: A brief introduction of what a blockchain is.

![alt text](https://github.com/himalayasharma/elementary-blockchain/blob/app-v2/readme-assets/1-app-brief-intro.png)

Screenshot 2: Functionality to mine block.

![alt text](https://github.com/himalayasharma/elementary-blockchain/blob/app-v2/readme-assets/2-app-mine-block.png)

Screenshot 3: Checks to ensure validity and view current blockchain.

![alt text](https://github.com/himalayasharma/elementary-blockchain/blob/app-v2/readme-assets/3-app-validity-status-current-blockchain.png)

Screenshot 4: Functionality to modify existing blockchain along with an option to reset it completely.

![alt text](https://github.com/himalayasharma/elementary-blockchain/blob/app-v2/readme-assets/4-modify-block-reset-blockchain.png)

Contributing
------------
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated. If you have a suggestion that would make this better, please fork the repo and create a pull request. Don't forget to give the project a star! Thanks again!

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

License
------------
Distributed under the MIT License. See `LICENSE.txt` for more information.

Ackowledgements
------------
* [Rithmic](https://www.youtube.com/c/rithmics)
* [MariyaSha](https://github.com/MariyaSha)
* [Caleb Curry](https://www.youtube.com/c/CalebTheVideoMaker2)
* [Teclado](https://www.youtube.com/c/tecladocode)
--------
