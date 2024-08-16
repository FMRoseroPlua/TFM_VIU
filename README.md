## Análisis de datos sensoriales para una aplicación de monitoreo de condiciones de una instalación industrial. 
### Descripción
El presente trabajo de fin de máster trata sobre el análisis de datos sensoriales para
una aplicación de monitoreo de condiciones de una instalación industrial. Los datos
utilizados provienen del conjunto de datos de referencia de acceso público “PRONTO”,
los cuales fueron recopilados de una instalación de flujo multifásico de alta presión,
totalmente automatizada y a escala industrial, en varias condiciones operativas con y
sin fallas. Las condiciones operativas de estudio, consisten en cuatro escenarios uno
que corresponde a un estado de condiciones normales, y los otros tres que
corresponden a fallas por fuga de aire, bloqueo de aire y desviación de flujo. Los datos
para cada escenario fueron medidos por sensores a través de un sistema SCADA
(Supervisión, Control y Adquisición de Datos). 

 Durante el desarrollo de este trabajo se utilizó el conjunto de datos “PRONTO”, para
aplicar diversas técnicas de preprocesado y análisis de datos, como reducción de
características, análisis de correlación, transformación de datos y análisis estadísticos,
entre otros. Los modelos se desarrollaron utilizando varios algoritmos de aprendizaje
supervisado para tareas de clasificación, exactamente: “K-Nearest Neighbors, Decison
Trees, Suport Vector Classifier, Random Forest, AdaBoost, Gradient Boosting y Voting
Classifier”, con el objetivo de encontrar el algoritmo que presente una mayor exactitud
para clasificar correctamente las cuatro condiciones operativas mencionadas
anteriormente. Adicionalmente se desarrolló una aplicación que permita visualizar el
funcionamiento del modelo en un posible escenario de toma de datos de la instalación
industrial, y representar su comportamiento para predicción en tiempo real.  
