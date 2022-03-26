D:
cd D:\ejagruti_selenium_python\selenium_finsys\FINSYS\
behave -f allure_behave.formatter:AllureFormatter -o Allure/Results ./FEATURES
allure serve Allure/Results
