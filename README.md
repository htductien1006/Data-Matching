# Read datasets in Python

## Environment
Preparation Steps:
  1. Python3 (should be Python 3.10 version) and Pip
  2. Pyjnius package
     ```
     pip install pyjnius
     #or
     python -m pip install pyjnius
     ```
 3. Java SE Development (JDK - any version > 8) and Set its env as Java default.
 4. Jedai-core and its dependencies - jedai-core-3.0-jar-with-dependencies.jar
 
 ## Documentation of Jedai-core
 
 1. Java implementation code of **DataReader.EntityReader.EntitySerializationReader**:
 https://github.com/scify/JedAIToolkit/blob/master/src/main/java/org/scify/jedai/datareader/entityreader/EntitySerializationReader.java
 
 2. Java implementation code of **DataReader.GroundTruthReader.GtSerializationReader**:
 https://github.com/scify/JedAIToolkit/blob/master/src/main/java/org/scify/jedai/datareader/groundtruthreader/GtSerializationReader.java
 
 3. **Data model**: https://github.com/scify/JedAIToolkit/tree/master/src/main/java/org/scify/jedai/datamodel
 
## Check all JSO file on JedAI webapp
Open JedAI webapp using Docker
```
docker pull gmandi/jedai-webapp
docker run -p 8080:8080 gmandi/jedai-webapp
```
Let it run and wait for until you get like the below:
!(https://drive.google.com/file/d/12lhwDkge-WRRUwBERJpeMahIMalzUlKO/view?usp=share_link)
 
