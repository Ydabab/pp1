'''
13.	An array movie_titles contains any five movie titles. 
Write a program that writes the movie titles to the movies.txt file, each title on a separate line. 
After executing the program, open the created text file and check its content.
'''

movie_titles = ["a", "b", "c", "d", "e"]
movies = open("movies.txt", "w")
i = 0
while i < len(movie_titles):
    for k in movie_titles:
        movies.write(k + "\n")
        i += 1
movies.close()