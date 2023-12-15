# Selenium Python Framework Sample Project

<br>

## Selenium Python Framework Introduction

This is an automation framework supporting both UI and API testing. It's built on top of the following component
- Selenium(Automation tool)
- Pytest(Test runner)
- Allure(Test report)
- requests(Python libraries for executing rest API)
This automation framework support to select browser/test environment for running test, filter test cases and running test in parallel
<br>

## Installation

1. Download and Install [Python 3](https://www.python.org/ftp/python/3.7.0/python-3.7.0.exe "Python 3").
2. Add the Python installation directory to the **PATH** variable.
3. Add **Scripts** folder inside the **Python** installation directory into the **PATH** variable.
4. Install dependencies package.
    `pip install -r requirements.txt`
5. Install [Allure report](https://docs.qameta.io/allure/#_installing_a_commandline) commandline


## Example

Here, I have developed sample test cases for a sample web site [Demo QA Book Store](https://demoqa.com/books).

This project is developed to demontrate robot framework with selenium and page object model. Besides, we also implement some test cases for API and integrate API in UI test cases for prepare/cleaning test data.

<br>

## File organization
```
Selenium-Python Framework Demo/
|- DemoQABookStore/                                                  // Home folder for Demo QA Book Store automation project
  |core
     |- api                                                          // Common API helper
     |- const                                                        // Constant
     |- driver                                                       // Common driver keywords
        |-driver_types                                               // Implementation for various kinds of driver
        |-base_driver                                                // Driver interface
        |-driver-configuration                                       // Model for driver configuration
        |-driver_utils                                               // Driver utilities
     |- element                                                      // Selenium element wrapper
     |- env_info                                                     // Model for environement information
     |- utilities                                                    // Functions for file, random, wait
  |- data_object                                                     // Data model
  |- helper/api                                                      // API Helper for the Demo QA BookStore application
  |- page_object                                                     // Page object classes
  |- resources
     |- test_configuration                                        
        |-driver_conf.json                                           // Driver configuration
        |-env_conf.json                                              // Environment configuration
     |- test_data                                                    // Test Data                                   
  |- testcases/api                                                   // API test cases of the application
  |- testcases/ui                                                    // UI test cases of the application
|- .gitignore                                                        // Excluded the unnecessary files in the repo
|- README.md                                                         // This file
```
<br>

## Usage

The test file name and test cases name have to follow the convention of Pytest.
Firstly change your current directory into DemoQABookStore

     cd .\DemoQABookStore

The basic usage is giving a path to a test (or task) file or directory as an
argument with possible command line options before the path

     pytest --alluredir=allure_report .\testcases\ui\test_delete_book.py
     pytest --alluredir=allure_report .\testcases 

Run specific test cases by tag with 

     pytest --alluredir=allure_report -m "smoke" .\testcases\

Run test with crossed browser

     pytest --alluredir=allure_report --browser firefox_local  

Run test with specific environment

     pytest --alluredir=allure_report --test-env uat  

Run test cases in parallel

     pytest -n 2 --alluredir=allure_report  testcases\ui

Generate allure report with specific folder

     pytest --alluredir=allure_report
     allure serve ./allure_report

<br>

