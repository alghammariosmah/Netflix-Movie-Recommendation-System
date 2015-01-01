The codes and the files were intended to be used for educational purposes. 
The database used is taken from Netflix. The follwoing link is the dataset download:
http://www.lifecrunch.biz/wp-content/uploads/2011/04/nf_prize_dataset.tar.gz

So, my project was:
A “Movie Recommendation System” based on Netflix dataset. Obtaining the Netflix movie dataset. Converted the dataset to the format used in Collective Intelligence (the “critics” dataset from the first chapter of the textbook page 8). Then I wrote a program which recommends movies to people, by using the different techniques (user-based, item-based, etc.)

The dataset format:
- A short sample of the Movies and their numbers are extracted in a file called “ movie_titles”. The file contains the numbers followed by the publishing dates and the movie title as follows:

1,2003,Dinosaur Planet
2,2004,Isle of Man TT 2004 Review
3,1997,Character
4,1994,Paula Abdul's Get Up & Dance
5,2004,The Rise and Fall of ECW
6,1997,Sick
7,1992,8 Man
8,2004,What the #$*! Do We Know!?
9,1991,Class of Nuke 'Em High 2
10,2001,Fighter


-  After extracting the data from the previous file, now I had this challenge of extracting the data from different files. Each file contains of, first, the movie number followed by a semi-colon. Then the customer ID, the ranking and the date of that ranking. A short-listed file excerpted as follows:

1488844,3,2005-09-06
822109,5,2005-05-13
885013,4,2005-10-19
30878,4,2005-12-26

- After training the whole dataset. I made the ultimate version of it which looks exactly like the "Critics" dicitionary in Collective Intelligence textbook. 

The after the critics I made were extracted from Collective Intelligence textbook. The codes work the same, but the sim_pearson code doesn't work properly with my big dataset. It always gives 0 as a result. Therefore, it is advised to use sim_distance or Jaccard_distance. 

- Ultimately, within running the code, it will ask you to enter the User-ID so it recommends movies to people, by using the different techniques (user-based, item-based)

Enjoy.