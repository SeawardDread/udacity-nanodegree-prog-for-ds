import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter

    The nested while loops are used for error handling; until the user inputs a valid value, they will be prompted to input.
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        city = str(input('Specify your city of interest - Chicago, New York City or Washington: ')).lower()
        if city in ('chicago','new york city', 'washington'):
            while True:
                month = str(input('Specify your month of interest - All, January, February, ... , June: ')).lower()
                if month in ('all', 'january', 'february', 'march', 'april', 'may', 'june',):
                    while True:
                        day = str(input('Specify your day of interest - All, Monday, Tuesday, ... Sunday: ')).lower()
                        if day in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
                            return city, month, day
                        else:
                            print('Value not recognised. Please select from: All, Monday, Tuesday, ... Sunday.')
                else:
                    print('Value not recognised. Please select from: All, January, February, ... , June.')
        else:
             print('Value not recognised. Please select from Chicago, New York City or Washington.')
    print('-'*40)
    #return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day

    Note that the code for this function came from practice problem 3.
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':

    # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':

    # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Month'] = df['Start Time'].dt.month
    mode_month = int(df['Start Month'].mode())
    print("Most common month: \n{}\n".format(mode_month))

    # TO DO: display the most common day of week
    df['Start Day of Week'] = df['Start Time'].dt.weekday_name
    mode_dow = df['Start Day of Week'].mode().to_string(index=False)
    print("Most common day of the week: \n{}\n".format(mode_dow))

    # TO DO: display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    mode_start_hour = int(df['Start Hour'].mode())*100
    print("Most common start hour: \n{}\n".format(mode_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mode_start_station = df['Start Station'].mode().to_string(index=False)
    print("Most commonly used start station: \n{}\n".format(mode_start_station))

    # TO DO: display most commonly used end station
    mode_end_station = df['End Station'].mode().to_string(index=False)
    print("Most commonly used end station: \n{}\n".format(mode_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start-End Station Combo'] = df['Start Station'] + ' -> ' + df['End Station']
    mode_combo_station = df['Start-End Station Combo'].mode().to_string(index=False)
    print("Most commonly start/end station combination: \n{}\n".format(mode_combo_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time: \n{:,.2f}\n".format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time: \n{:,.2f}\n".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts().to_string()
    print("Count of user types: \n{}\n".format(user_types))

    # TO DO: Display counts of gender
    if 'Gender' in df:
        user_gender = df['Gender'].value_counts().to_string()
        print("Count of user gender: \n{}\n".format(user_gender))
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth year' in df:
        earliest_birth_year = df['Birth Year'].min()
        print("Earliest birth year: \n{:.0f}\n".format(earliest_birth_year))

        latest_birth_year = df['Birth Year'].max()
        print("Most recent birth year: \n{:.0f}\n".format(latest_birth_year))

        mode_birth_year = int(df['Birth Year'].mode())
        print("Most common birth year: \n{}\n".format(mode_birth_year))
    else:
        print('Birth year stats cannot be calculated because Gender does not appear in the dataframe')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """ This was adapted from https://stackoverflow.com/questions/50866850/ask-user-to-continue-viewing-the-next-5-lines-of-data. I have modified the variables to make more sense for      this usage, declared the rows variable in the function, added the number of dataframe rows to the user input prompt (to allow them to understand how far through the data they        are), changed the return to print 5 lines of df, and changed the elif to an else and break clause, in order to better handle errors"""
    rows = 0
    while True:
        raw_data = input('\nWould you like to see 5 rows of raw data for this filter (there are {} rows in total)? Enter yes or no.\n'.format(len(df.index)))
        if raw_data == 'yes':
            rows += 1
            print(df.iloc[(rows-1)*5:rows*5])
        else:
            break

def main():
    """Errors are handled in three stages:
            1. Handling user input errors (the first 'try/except/else/finally' block)
            2. Handling errors caused by filters which don't work, as a result of differences in datasets e.g. user gender for Washington dataset (the second, nested 'try/except'                    block)
            3. When the user inputs anything but 'yes' when requesting more raw data, the function break is called
       In all cases, the failsafe is asking whether the user wishes to restart"""
    while True:
        try:
            city, month, day = get_filters()
            df = load_data(city, month, day)
        except:
            print("Looks like you might have entered an incompatible value! Let's try again.")

        else:
            print('Calculating...')
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            #Stage 2 of error handling
            user_stats(df)
            #Stage 3 of error handling
            raw_data(df)

        finally:
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break

if __name__ == "__main__":
	main()
