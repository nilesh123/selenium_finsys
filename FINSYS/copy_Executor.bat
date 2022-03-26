#navigate to your project folder location
f:
cd MANUAL_WORKSHOP\MARKET_TREND_ANALYSIS_KAM_HYAVAR_SURU_AAHE\eJagruti
#run this command to execute your feature files and this will generate result.json in Allure/Results Folder
behave -f allure_behave.formatter:AllureFormatter -o Allure/Results ./features
#in order to generate the Report from the Result.json execute below command
allure serve Allure/Results
#make sure that Allure Framework Should be downloaded on your local machine and path upto the bin folder 
#should be stored in Environment Variable PATH
#if you dont wont to do that then the command would be like
###F:\SELENIUM_WORKSHOP\allure-2.14\bin\allure serve Allure/Results
#Note here we have stored Results in Allure/Results Folder
