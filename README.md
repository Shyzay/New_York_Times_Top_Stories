# New_York_Times_Top_Stories
This application will display the 5 most popular articles (most viewed over the last 3 hours) 
from the New York Times nytimes.com website. 
It will have the title of the article, a link to the article, the byline, and the published date.
It will be able to cache data fetched from the external API into a local database, also render data from its database 
if it is not older than 5 mins, but If the data is older than 5 mins, 
it will refetch it from the API and update the cache with the new data
This application will be developed with flask and python language.
Database will be designed with MongoDB
