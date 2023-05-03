import pandas as csv
import random


def seconds_converter(timer):
    '''
    convert time into seconds, time is expected to be either a string of seconds or a sting of minutes:seconds
    '''
    if ':' not in timer:
        seconds_only = float(timer)
    else:
        minutes, seconds = timer.split(':')
        seconds_only = int(minutes) * 60 + float(seconds)
    return seconds_only

#verbose is the last argument, boolean value
#verbose set to False to skip printing (less spam)
#print statement can still run if verbose is set to True 
def sort_teams(teamfile1, teamfile2, verbose=False):
    '''
    merge two teams into a single dataframe that has grouped all of the events together, all copies of same event in the same location 
    '''
    #reads in the first two csv files (two seperate dataframes)
    team_1 = csv.read_csv(teamfile1)
    team_2 = csv.read_csv(teamfile2)
    #apply is a pandas method that takes function (seconds_converter) and passes it as an argument
    team_1['Time_in_seconds'] = team_1['Time'].apply(seconds_converter)
    team_2['Time_in_seconds'] = team_2['Time'].apply(seconds_converter)
    #remove all white space and capitalize all letters (case insensitive) so it doesn't create different events 
    #store team names so we can refer to them later
    team_1['Event'] = team_1['Event'].apply(str.strip).apply(str.upper)
    team_2['Event'] = team_2['Event'].apply(str.strip).apply(str.upper)
    #converting code so that we use the actual names of the teams rather than indicator 
    team1_name = team_1['Team'][0]
    team2_name = team_2['Team'][0]
    team_1['Team'] = 'Team 1'
    team_2['Team'] = 'Team 2'
    #stuck two teams together and sorted the swimmers by events 
    teams_merged = csv.concat([team_1, team_2])
    teams_sorted = teams_merged.sort_values(by= ['Event', 'Time_in_seconds'])
    teams_sorted.to_csv('merged_file.csv', index=False)
    #print dataframe
    if verbose:
        print('Best times\n')
        print(teams_sorted)
        print()
    return(teams_sorted, team1_name, team2_name)



def choose_swimmers(teams_sorted, event_entries_per_school=3):
    '''
    iterates through the events and picks best swimmers for that event so no school will enter too many swimmers in one event 
    and no swimmer will swim too many events
    '''
    #dictionaries that track how many swimmers each school sent to each event and no swimmer can participate in too many events 
    swimmers_events = {}
    team_entries = {'Team 1': {}, 'Team 2': {}}
    for event in teams_sorted['Event'].unique():
        team_entries['Team 1'][event] = 0
        team_entries['Team 2'][event] = 0
    #constant value makes it obvious what the 2 is being used for 
    MAX_EVENTS_PER_SWIMMER = 2
    #place swimmer who won the event in a list, grouping events together and running through them in alphabetical order
    #find top three swimmers for each team and mark them as participants in the event (skip swimmers who already swim two events)
    #for loops iterating over every event and every swimmer who can participate 
    for event, event_csv in teams_sorted.groupby('Event'):
        for name, row in event_csv.iterrows():
            name = row['Name']
            team = row['Team']
            if name not in swimmers_events:
                swimmers_events[name] = []
            #removes magic numbers by assigning to variables
            #magic numbers are constants that are hardcoded into function 
            if len(swimmers_events[name]) < MAX_EVENTS_PER_SWIMMER and team_entries[team][event] < event_entries_per_school:
                swimmers_events[name].append(event)
                team_entries[team][event] += 1
        

    #print(swimmers_events)
    #events dictionary: matches events to swimmers 
    #swimmers_events dictionary matches swimmers to events 
    #reversing list --> find out who is swimming each event 
    events = {}
    for name, swimmer_event in swimmers_events.items():
        for event in swimmer_event:
            if event in events:
                events[event].append(name)
            else:
                events[event] = [name]
    return events

#event results dictionary: getting times that each swimmer got and apending to the results array the time and athlete combo 
#max_percent_error assumes that every swimmer performs their best, set to zero as default 
def get_results(events, teams_sorted, verbose= False, max_percent_error=0):
    '''
    take a list of who swims in each event and turn it into a list of how people place relative to each other 
    '''
    event_results = {}
    for event, names in events.items():
        results = []
        for athlete in names:
            times = teams_sorted[(teams_sorted['Name'] == athlete) & (teams_sorted['Event'] == event)]['Time_in_seconds']
            if not times.empty:
                time = times.iloc[0]
                #random.random gives a number from zero to one
                #multiply by max_percent_error
                #best time plus a potential random factor 
                swimmer_error = random.random()* max_percent_error
                results.append((athlete, time*(1+swimmer_error/100)))
    #sorting athletes by time
        sorted_results = sorted(results, key=lambda x: x[1])
        sorted_athletes = [result[0] for result in sorted_results]
        #dictionary of how people placed 
        event_results[event] = sorted_athletes
    if verbose:
        print('Event Results\n')
        print(event_results)
        print()
    return event_results


def points(teamfile1, teamfile2, verbose=False, max_percent_error=0):
    '''
    loads in files, calculates who won each race, calculates points based off placing, prints which school won, returns score
    '''
    teams_sorted, team1_name, team2_name = sort_teams(teamfile1, teamfile2, verbose)
    events = choose_swimmers(teams_sorted)
    event_results = get_results(events, teams_sorted, verbose, max_percent_error)
    team_points = {team1_name: 0, team2_name: 0}
    #global constant, value will not change 
    POINTS = [9, 4, 3, 2, 1, 0]
    for event, names in event_results.items():
        for i, swimmer in enumerate(names):
            if i == 0:
                print(f'{event} won by {swimmer}!')
            team = teams_sorted[teams_sorted['Name'] == swimmer]['Team'].iloc[0]
            team = team1_name if team == 'Team 1' else team2_name
            team_points[team] += POINTS[i]
    #print winner
    if team_points[team1_name] > team_points[team2_name]:
        print(f'\n{team1_name} won!\n') 
    else:
        print(f'\n{team2_name} won!\n')
    return(team_points)


#main function in python 
#causes the code to run when the file is run 
#causes code to not run when the file is imported 
#Assuming 10% error -- swimmer whose best time is 52 seconds is assumed to get at worst 57 
if __name__ == '__main__':
    Teamfile1 = input('Team 1 csv file: ')
    Teamfile2 = input('Team 2 csv file: ')
    if Teamfile1 == Teamfile2:
        print('You entered the 2 same teams! Please try again.')
    else:
        print(points(Teamfile1, Teamfile2, verbose= True, max_percent_error=10))
    