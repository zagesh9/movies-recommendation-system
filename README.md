## Movies Recommendation System
#### https://mrs-9.herokuapp.com/
1. Business Context
● Content based recommendation system.
2. Problem Statement
● Get recommendations on a movie or get similar types of movies.
3. Solution Developed
● Downloaded 5000 tmdb movies dataset and 5000 tmdb credits from kaggle. Merged
both the datasets on ‘Title’. Multiple columns were a list of dictionaries so did some
preprocessing on those columns. Made a function to get the top 3 casts of each movie.
Made a function to extract only the Director from the crew column. After removing the
spaces for all these columns, ‘Johnny Depp’ becomes ‘JohnnyDepp’.
● Made a new column named ‘tags’ and it included genres, keywords, cast and crew. Used
lambda function to convert list into string for tags column and then again applied lambda
for lowercase.
● Stemming is the process of producing morphological variants of a root/base word.
Stemming programs are commonly referred to as stemming algorithms or stemmers. A
stemming algorithm reduces the words “chocolates”, “chocolatey”, and “choco” to the
root word, “chocolate” and “retrieval”, “retrieved”, “retrieves” reduce to the stem
“retrieve”. Applied stemming on the tags columns.
● Used CountVectorizer to transform the tags column into vectors. Made an array of those
vectors. Now it was time to apply the Cosine Similarity on those vectors.
● Cosine similarity is a metric used to
measure how similar the documents are
irrespective of their size. Mathematically, it
measures the cosine of the angle between
two vectors projected in a
multi-dimensional space. The cosine
similarity is advantageous because even if
the two similar documents are far apart by
the Euclidean distance (due to the size of
the document), chances are they may still
be oriented closer together. The smaller
the angle, higher the cosine similarity.
● Made a function to recommend movies based on the selected movie. Also used lambda
function to get the top 10 similar movies.
● Made use of pickle to save the model and the similarity. So now if I put a movie name in
the recommended function it will return me top 10 similar movies.
4. Improvements to the Solution
● The model was ready and was able to return top 10 similar movies based on the tags
columns which included genres, keywords, cast and crew. I thought of taking it to a next
level and making it an end to end project. I found multiple platforms where I could deploy
my model but I chose Heroku.
● Now it was time to choose a framework for the web application. I did some research and
found Streamlit is good for web applications as you just need to use the functions that
are already built for you in streamlit. So I made all the necessary files that would be
required to deploy the model on Heroku.
● The web application was up and running now it was time to add some styling but in
Streamlit you don’t need to make html or css. And the only styling you could do was just
change the font size and color. But I found a way to make a css file and attach it to the
main python file. So I did all the styling in that css file.
● Then I made use of the API to fetch the movie posters from the TMDB website. I just had
to make a function that would just make a list of all the movie id and from those movie id
I could fetch the posters for those recommended movies.
● I load the pickle files that I made for the model and the similarity in the main python file.
Made use of the Streamlit functions to get the movie name from the selectbox and then
use that movie name to get the recommendations with the posters.
5. Link to the working project demo/prototype developed
● https://mrs-9.herokuapp.com/
