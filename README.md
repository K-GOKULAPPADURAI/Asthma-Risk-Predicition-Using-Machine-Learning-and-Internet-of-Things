# Asthma-Predicition-Using-Machine-Learning-and-Internet-of-Things

## ABSTRACT 
            In this project, we present an asthma risk prediction tool based on machine learning. The entire tool is implemented on a smartphone as a mobile-health application using the resources of Internet-of-Things (IoT). **Peak Expiratory Flow Rates (PEFR)** are commonly measured using external instruments such as peak flow meters and are well known asthma risk predictors. In this work, we find a correlation between the particulate matter found indoors and the outside weather with the PEFR. Convolutional neural network architecture is used to map the relationship between the indoor PM and weather data to the PEFR values. The proposed method is compared with the state-of-the-art deep neural network-based techniques in terms of the root mean square and mean absolute error accuracy measures. These performance measures are better for the proposed method than other methods discussed in the literature surveys. The entire setup is implemented on a smartphone as an app. An IoT system including a Raspberry Pi is used to collect the input data. This assistive tool can be a cost-effective tool for predicting the risk of asthma attacks.

## OBJECTIVE

       In this section, we discuss the proposed asthma risk prediction method. The data and the deep learning network used for the model training are discussed. The block diagram of the proposed system is shown. The weather data and the indoor air pollution characterized by **PM2.5 and PM10** data are the input to the Deep learning model and the peak expiratory flow rate (PEFR) provides the labels used in training the model. we discuss the tools and the steps involved in IoT implementation. The real-time data collection, the utilization of the data and the smartphone app are explained in this section.

## ALGORITHM :

Algorithm explaining the proposed system working in real-time 
Input: PM2.5, PM10, outdoor temperature, humidity. 
Output: Safe, Moderate or High asthma risk prediction. 
Data processing stage on the Raspberry Pi: 
Collect PM2.5, PM10 using SDS011; Collect weather data using Openweather map; Data hosting the input features to server; 
Real-time stage on the Smartphone: 

	while App ON 
		 do Collect data from Web;
		 CNN prediction;
		 if PEFR > 80% then 
			Safe; 
		else if 50% < PEFR < 80% then 
			Moderate risk;
		 else 
			High risk;
		 end
	end

## WORKING

The patient want to take the best PEFR value 
The application deployed in the edge device is installed with the model we trained by the asthma patients 
The inputs are give to the model using the text field
The result calculated and the status will be displayed
By the methodology 1 we will fetch the air quality data using sensors which is connected to raspberry pi 
By the methodology 2 we will fetch the air quality data using the online weather API called OPENWEATHER.
As per the resulted PEFR value the result will any of SAFE, MODERATE, RISK.

## GRAPHICAL USER INTERFACE 

Application using python KIVY Frame work 
With sensor input manually given method
&
Without sensor inputs and using openweather api call by the geological coordinates 

![image](https://user-images.githubusercontent.com/77343301/209463411-f62bb76a-4261-4a26-a463-a40b12db2169.png)

Output for the both methods 

![image](https://user-images.githubusercontent.com/77343301/209463449-63218158-f066-4f6e-970b-bd1930fe5fda.png)

## CONCLUSION 

In this project, we presented an asthma risk prediction tool based on a convolutional neural network. The PEFR readings are predicted using simple PM and weather data. The performance improvement of the proposed method is observed using objective evaluations. This cost-effective tool involves an edge device, sensors and an IoT platform. The entire tool is implemented on a smartphone as application using several resources of IoT. The tool can be successfully used to predict asthma risk of individual patients.

## CONTACT

Feel free to ping me 

phone : 9025421765
gmail : k.gokulappaduraikjgv@gmail.com 

 


