# CS-32-Final-Project
CS 32 Final Project with Sydney Lu and Carlie Rose

For our project we have decided to create a swim meet simulator (a swimulator). Using swimmer best times, we will create a simulator that will predict the outcome of the swim meet. We would show not just the outcome scores, but also, the event lineups that lead to the highest potential points. This optimal lineup would be compared with other teams' optimal lineups in order to determine the most likely outcome of the meet. While not a completely fool-proof simulator, it would give a good idea of how to approach a meet lineup/outcomes to expect.


Features of the Swimulator 
  - take two ivy league swim teams and predict which team will win based off of personal best times 
      - each swimmer can only swim four events 
      - read in swimmer data from a file 
      - perhaps introduce randomness (prediction)
  - utilize load_data() function to create dictionaries including events, swimmers, and times 
      - reference problem set 5 for potential format 
  - use a class to combine data and functions to produce an output (result of a race and swim meet) 
Roadmap 
  - High Priority 
      - create a data structure that can hold a swimmer 
      - simulate a swim meet between two teams
      - calculate number of points 
      - print the winners, detailed statistic info, results from events 
  - Medium Priority 
      - read in the swimmers from a file 
      - allow swimmers to not particpate in certain events (only participate in four)
      - add randomness (not always assumed to get best times)
  - Low Priority (if we have time) 
      - incorporate relays and diving 
      - optimizer
        - find combinations of events that give a team the highest chance of winning 
      - simulations (run many trials as opposed to one single meet）


