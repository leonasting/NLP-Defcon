[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
# NLP-Devcon

## About the project:
We attempt to create a web-based solution for the public to make queries about the defense
contracts of the United States of America and provide them closest answer.
## Motivation:
We think this project will enable us to learn about the latest techniques used for
question-answering on unorganized data. Our project will provide a quick way to gather
information about the army’s available contracts.

## About Data Source:
We have used the defense contracts dataset (https://www.defense.gov/News/Contracts/) having
news and updates about the contract acquisitions for the US Army, Navy, and Air force. The
contracts’ information is updated daily, so we have to scrape the website for a particular period,
aggregating it into data set of 100+ documents.

## About Implementation
We have used python and libraries like beautiful soup, requests, and urllib3 to scrape, parse and
structure the contracts.
We have used Open AI GPT3 model to check transfer learning.
We have implemented multiple  BERT based Language models: Base BERT,


### Folder Structure
```shell
NLP-Defcon/
├── UI Base
│   ├── templates   
│   └── defcon_app.py
│         
├── data
│   ├── data_main.csv
│   ├── data_unique.csv
│   ├── data_url.csv
│   ├── def_qa.csv
│   ├── def_qa.json
│   ├── def_qa2.json
│   ├── val_qa.csv
│   └── val_qa.json
│
└── documentation   
│   └── Project Proposal.pdf
└── scripts
│   ├── 1.Data_Scraping_Page_link_.ipynb
│   ├── 2.Data Processing1.ipynb
│   ├── 3.GPT3_QnA.ipynb
│   ├── 4.BERT.ipynb
│   ├── 5.DeBertaV2.ipynb
│   ├── 6.DistilBert.ipynb
│   └── 7.Roberta.ipynb
│   
└── README.md

```

## About our code implementation.

### Scripts:
  
  1. Data Scrapper- Used to web scrape from provided url
  2. Data Processes - Data Processing over the scrapped data
  4. BERT - Takes manually created data for fine tuning the model and  checking accuracy over predifined question set.
  
  Note:
  3-7 Are separate impelmentation of different models to check their accuracy
 
 ### UI Base
  Contains the UI implementaion.
