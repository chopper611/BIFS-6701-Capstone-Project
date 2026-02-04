#BIOT6701 Capstone Project- Custom LLM for BIFS614

This project will create a custom LLM for students in BIFS614. The LLM will act as a tutor and guide for students who need help understanding the material. The LLM will be created with a pretrained LLM, most likely an open-source ChatGPT style model. The LLM will be used as a tutor, study assistant, and exam-style proctor. 

##Team Members
Leroy Daniels 
Silvia Escamilla 
Nick Lawson 
Alyssa Moser 
Stephanos Mulder-Stoupakis 

##Project Overview 
The goal of this project is to create a ChatGPT-like model for students in BIFS614. The model should help students with knowledge gaps, guiding study sessions, assisting with complex concepts, asking practice or assessment questions, and tutoring opposed to just giving answers.

##Objectives 
-Create a LLM that can be used as an interactive exam proctor for students
-The LLM will be used for verifying information in the BIFS614 class
-Testing will take the most time in the project
-Gauge users failure of knowledge 
-Will be used to question knowledge gaps
-Project will be graded more as how we work as a team/solve real word problems in real time when creating the LLM
-Distinguish between study mode and assessment mode
-Prioritize explanation and reasoning over direct answers

##Approach
-First define what the ChatGPT will do
-Determine the type of chatbot to use 
-Decide how we would like the LLM to respond to questions and conversations 
-Add BIFS614 information to the LLM to store it- includes notes, class materials, exams 
-Evaluate how LLM will function and make necessary adjustments 
-Test out LLM and improve response results until results are satisfactory

##Action Plan
1. Course Data Prep
-Gather BIF614 slides, nodes and readings 
-Convert files into usable text 

2. Embeddings and Retrieval 
-Generate embeddings from the prepared course text 
-Store embeddings in a vector database 
-Set up basic retrieval so the model can find relevant content 
-Test whether the correct course content is being returned 

3. Prompts and Model Instructions 
-Write system and user prompts.
-Set rules so the model stays within BIFS 614 material.
-Adjust prompts based on trial and error.
-Focus on improving answer clarity and relevance.

4. Application Flow
-Connect user input to retrieval and the model.
-Handle passing questions through the system.
-Display model responses in a simple interface.
-Keep focus on functionality.

5. Testing and Exam-Style Behavior
-Write practice and exam-style questions.
-Check model answers for accuracy and completeness.
-Experiment with simple exam rules like limited hints.
-Track common mistakes or weak areas.

