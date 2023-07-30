# CS416FinalProj


## Git website url: https://xingyifei2016.github.io/CS416FinalProj/

 The essay should contain the following sections.

•	Messaging. What is the message you are trying to communicate with the narrative visualization?

The message that I am trying to communicate with the narrative visualization is that COVID19 is a very infectious disease with a noticeable death rate, as well as things to do and not to do when the virus is spreading. In the website, I try to give out information about local covid cases and deaths in the U.S., followed by things that will incur high COVID risks, incur medium COVID risks and things that incur low COVID risks. Then, I give out global trends for confirmed cases and deaths, followed by the distribution of globally confirmed cases spread across 2020 to 2022, for users to gain an overview of the spread and distribution of COVID19, informing users that they need to be vary of the pandemic. The narrative visualization also allows users to make several observations such as how the geographical distribution of states and countries affect the spread and death rate of the disease, allowing them to make connections about geographical locations and international governmental policies and regulations that either prevent or worsen the spread of the disease. For instance, users can infer from the graph that northern states in the U.S. typically have less infections and death rates, possibly due to the virus being weakened from the cold. They may also infer from the graphs that China’s extremely strict COVID policies are very effective in detering the spread of the disease, compared to other Asian countries. Since time is also considered in the narrative visualization, it also allows users to see how the virus develops through time. 

•	Narrative Structure. Which structure was your narrative visualization designed to follow (martini glass, interactive slide show or drop-down story)? How does your narrative visualization follow that structure? (All of these structures can include the opportunity to "drill-down" and explore. The difference is where that opportunity happens in the structure.)

I used the martini glass technique to show the narrative structure. I used 5 scenes that are connected with back and next buttons. The entire narrative consists of 5 different scenes to show covid-relevant information, that consists of geographical distribution of deaths and confirmed cases in the U.S., ways for low/medium/high risk activities for Covid19, global trends for death and confirmed cases, and global distribution of cases per continent; which have different drill-down buttons for further interaction of the respective scene. 

•	Visual Structure. What visual structure is used for each scene? How does it ensure the viewer can understand the data and navigate the scene? How does it highlight to urge the viewer to focus on the important parts of the data in each scene? How does it help the viewer transition to other scenes, to understand how the data connects to the data in other scenes?

The visual structure is ultimately maintained by the back and next buttons for users to navigate on their own, but preferably in the order that I presented the slides(leaving room for individual exploration). Visual consistency is maintained through having similar templates and a uniform white background, as well as meaningful colors. The structure is also similar in that each svg is sitting on the middle of the screen, with small annotations on the side or bottom of the svg, to make each page as consistent as possible. The use of colored bars for legends and scrollbars also give users a sense of where they are in terms of the visualization, and each scene is dedicated to a specific portion of the visual narrative. Many of the scenes are intuitive and connected with each other. On scenes 2 and 3, for instance, I used the same template, which makes users transition more smoothly among the two narrative visualizations.   

•	Scenes. What are the scenes of your narrative visualization? How are the scenes ordered, and why

There are a total of 5 scenes in my narrative visualization. I have ordered them as the way I want to present the problem and story to the audience: first, I show them in scene 1 an overall overview of the different continents on COVID confirmed cases to show them the severity of COVID that is affecting the world. Then, I transition to scenes 2 and 3 for more general global statistics of COVID19, for them to understand the severity of the disease in terms of overall confirmed cases and death numbers. Hopefully, these statistics will give users a better understanding of the pandemic as a global issue. On scene 4, I transition the location to focus on the United States, as this is where I assume that the readers are located at. The interactive interface lets users input a state and a county for them to see how their local community is doing against COVID19 in 2022. Lastly, I offer a more hands-on gadget in scene 5 for users to play around and see ways and activities that incur low, medium and high risk for COVID exposure, such that they can get educated on what to do and what not to do to avoid getting infected. 

All in all, I want the users to acknowledge the severity of COVID in the states, make further observations about different governmental policies, geographical locations, and other factors that affect the infection rate of COVID19, and understand different ways to prevent it. 

•	Annotations. What template was followed for the annotations, and why that template? How are the annotations used to support the messaging? Do the annotations change within a single scene, and if so, how and why

There are several ways I have implemented annotations on the narrative visualization. First is plain text that offers some observations over the data such as the boxed text in scenes 2 and 3. Second are legends and variable names such as year numbers depicted on the scene 1, that highlights the respective years when hovered. I also used tooltips for scene 1, 2, and 3, which gives out exact numbers in confirmed cases/deaths when users hover over the respective bars on the graph. This can help users better understand spatially the number of cases and deaths that happened, without the need to manually approximate the numbers as shown in the graph. The annotations remain constant in the scenes, which allows users to have some grounding on the overall message presented by each scene. 

•	Parameters. What are the parameters of the narrative visualization? What are the states of the narrative visualization? How are the parameters used to define the state and each scene?

For scene 4, I create a histogram based on user input. When they enter a state name and a county name via the dropdown menu, I will generate a histogram detailing the COVID19 statistics for that county. Thus the state name and county names serve as parameters for this scene. For scene 5, I created a custom scroll-bar for users to scroll from left to right, where left is low-risk activities and right is high-risk activities. By dragging the bar, I used javascript to show the respective low-risk, medium-risk and high-risk activities to the users, making this visualization more interactive and fun. The user’s input on the scroll bar can be seen as controlling how the visualization is portrayed. In this case, the parameter that user is controlling is essentially low/medium or high-risk activities.  Furthermore, there are buttons on each page (ie 1-5), that the user clicks to transition to each scene. The numbers are also a form of parameter that controls which scene to show. 

•	Triggers. What are the triggers that connect user actions to changes of state in the narrative visualization? What affordances are provided to the user to communicate to them what options are available to them in the narrative visualization?

There are also triggers in the different scenes that are implemented via events and callbacks (ie mouseover, mouseout). For instance, in scene 1, when the user hovers over the respective rectangle for a specific year, the histograms for that specific year will be shown, and the other histograms become opaque. Another sort of callback action I implemented is in scene 2 and 3, where I change the value of the # of confirmed cases or deaths on the plot by callbacking on the bar on which the user hovers on. There are also buttons in the scenes that trigger certain “back” actions when clicked. 


