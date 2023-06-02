import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

city_name=['chicago','new york city','washington']
month_name=['all','january','february','march','april','may','june']
day_name=['all','saturday','sunday','monday','tuesday','wednesday','thursday','friday']
print("Hello! let's explore some US bikeshare data!")
def check(input_name,input_type):
    while 1:
        read = str(input(input_name)).lower()
        try:
            if read in city_name and input_type == 1:
                break
            elif read in month_name and input_type == 2:
                break
            elif read in day_name and input_type == 3:
                break
            elif read in ['yes','no'] and input_type == 4:
                break
            else:
                if input_type == 1:
                    print("Error: Please Enter the city's name in a correct way.")
                elif input_type == 2:
                    print("Error: Please Enter the month in a correct way.")
                elif input_type ==3:
                    print("Error: Please Enter the name in a correct way.")
                elif input_type == 4:
                    print("Error: Please Choose between yes/no.")
        except ValueError:
            print("Error: Strings only!")
    return read

def get_filters():
    city=check(f'Choose City: {", ".join(city_name)}: ',1)
    month=check(f'Choose Month: {", ".join(month_name)}: ',2)
    day=check(f'Choose Day: {", ".join(day_name)}: ',3)
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        df = df[df['month'] == month.title()]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most comman month is: ",df['month'].mode()[0])

    # display the most common day of week
    print("The most comman day is: ",df['day_of_week'].mode()[0])

    # display the most common start hour
    print("The most comman start hour is: ",df['hour'].mode()[0])
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most comman start station is: ",df['Start Station'].mode()[0])


    # display most commonly used end station
    print("The most comman end station is: ",df['End Station'].mode()[0])


    # display most frequent combination of start station and end station trip
    most_stations=df['Start Station']+","+df['End Station']
    print("The most comman station is: ",most_stations.mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total Travel Duration: ",int(df['Trip Duration'].sum().round()))

    # display mean travel time
    print("Average Travel Duration: ",int(df['Trip Duration'].mean().round()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())

    if city != 'washington':
        # Display counts of gender
        print(df['User Type'].value_counts())

        # Display earliest, most recent, and most common year of birth
        print("Most comman year of birth: ",int(df['Birth Year'].mode()[0]))
        print("Most recent year of birth: ",int(df['Birth Year'].max()))
        print("Most earliest year of birth: ",int(df['Birth Year'].min()))
    else:
        print("There is no more data to show!")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def get_random_date(df):
    print("Random data available to see...")
    user_input=check("Would you like to see 5 random data? yes/no: ",4)
    if user_input != 'yes':
        print("See You Again!")
    else:
        i=0
        while i+5<df.shape[0]:
            print(df.iloc[i:i+5])
            i+=5
            user_input=check("Would you like to see more 5 random data? yes/no: ",4)
            if user_input != 'yes':
                print("Thanks!")
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.head())
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        get_random_date(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("See You Again!")
            break


if __name__ == "__main__":
	main()
    