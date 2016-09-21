
<div align=center>
<h1> Smart Search for Education - Web Application </h1>

<h2> Feasibility Study report </h2>
</div> 

## Overview of Document

The Feasibility Study report covers economic and technical feasibility of the application.

The report consists of the following data:

- Background of the problem (What problem is being addressed by the Application)
- Limitations and Constraints
- Economic Feasibility
- Public survey conducted to validate our assumptions


## Analysis of problem (Why do we need this software?)

In this digitized mode of learning(e-learning) almost all of us use soft-copies suggested by friends, teachers and others for learning or reading. All the time searching the content inside the scanned documents is very difficult as search is not supported in images. Only the name of the image can be queried but not the content carried by the image.
And also most of the times we want a particular concept/topic, and we download the whole book but end up not understanding or founding it not useful. 

So, the application we develop addresses the above problems in this way as follows:
- We upload the scanned documents ( books/notes/articles/research papers) and using OCR (Optical Character Recognition) extract the content (text) out of it.
- We use this text(converted to json) to feed Elastic Search and make the documents searchable.
- If user searches for any concept/topic/book/notes the most relevant suggestion is shown along with the reviews of the document.
- User can view/download the document if it is useful(scanned original document).
Also, user can create personal libraries out of the documents which are useful.


## Limitations and Constraints

- The application requires Internet connection and a web browser to access the application independent of the device.
- The appication is initially built only for (Enlish US). Therefore it is searchable in the same language only.
- The application is built keeping in mind the user has basic knowledge in using Web Applications.


## Economic Feasibility
The application is developed using all open-source softwares/libraies on Linux (Ubuntu). The developers will be making this available freely for anyone to download and reuse under GNU General Public License V3.


## Conclusions From Our Survey

##### We surveyed 127 people, belonging to different diverse sectors like Educational Institutions (teachers/professors), students, book-lovers and general public.


#### 1. <center><img src="https://cloud.githubusercontent.com/assets/14366356/18721359/bcc41ef0-804d-11e6-854c-9a106620de4a.PNG" height = auto width = "600px" ></center>


#### Result: Around 

#### 2. <center><img src="https://cloud.githubusercontent.com/assets/14366356/18721360/bd379b32-804d-11e6-8445-70f7a60c2ac9.PNG" height = auto width = "600px"></center>

#### Result:


#### 3. <center><img src="https://cloud.githubusercontent.com/assets/14366356/18721361/be2f6e02-804d-11e6-81f5-e41ca2a8e0c7.PNG" height = auto width = "600px" ></center>

#### Result: 

Final result from the Survey: Among 127 people, 106 people (83.5%) showed interest in using the application.
