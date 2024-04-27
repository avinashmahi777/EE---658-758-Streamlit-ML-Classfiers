# EE-658-758-Streamlit-ML-Classfiers
In this assignment, you will develop a Python and Streamlit web application that allows users to interact with machine learning models. Your application will enable users to select between two datasets, the IRIS and Digits datasets, choose a machine learning classifier, input feature values, and obtain predictions.

### Video Explanation
[Click Here](https://photos.app.goo.gl/P7w4WiZ5uksExKVz7)

## Application Walkthrough 
1. The Entire Web application has Python, CSS (for styling)

2. In this application we are going to Build 3 Machine Learning Classifiers 
					1. Logistic Regression
					2. Neural Networks and 
					3. Naïve Bayes
   Integrating with Web applications using streamlit (Python framework)

3. ML Classifiers are built on 2 Datasets (IRIS, Digits) downloaded from the Sckit learn library


4. Below are the Techstack (frameworks, libraries) we are using in this project
   For Building ML Classfiers, Datasets - Scikit learn 
                   Web application      - Streamlit
                   Styling             - CSS


5. Code Walk through / Process : 
	5.1. Import & Download required libraries 
		a. Import & Download required libraries 
		b. Download streamlit using this command "pip install streamlit"
		c. Download 2 Datasets (IRIS, Digits ) from Scikit-learn
		d. Import 3 required ML Classifiers using from Sciki-learn
	


5.2. Loading Datasets
	1. Load the datasets from the imported sci-kit learn library "datasets"

5.3. Assigning Classifiers
	1. Create a dictionary for 3 classifiers key as name, value as classifier calling method

5.4. Adding a Radio button for choosing Dataset

5.5. Splitting Data for every model in an 80:20 Ratio with random seed as 42

5.6. Choosing Classifier by using the drop-down option

5.7. Giving Input Feature values by using Horizontal bars

5.8. Prediction of Classes using Predict functionality + Creating Radio Button 

5.9. Adding HTML & CSS for Prediction Button 
5.10 Adding Accuracy Check Option for Each Classifier 


6. Running Web Application 

	1. copy the streamlit.py or your .py extension python file 
	2. use this command to run the application 
              streamlit run YOURFILEPATH
	      streamlit run app.py (my code)


7. Checking Values in Web Applications 

	1. Choose Dataset
	2. Choose Classifier
	3. Change Input Features as per your requirement
	4. Click the Predict button
	5. Observe Predictive class in Application
