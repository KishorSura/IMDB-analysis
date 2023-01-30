create database IMDB;
use IMDB;
create table movie_name(
Ranks int,
	Title varchar(50),
	Genre text,
	Description text,
	Director varchar(200),
	Actors text,
	Year text,
	Runtime int,
	Rating float,
	Votes int,
	Revenue float,
	Metascore float);
 
 
 select * from movie_name; 
 
-- "Number of movies released in particulat year "

 select year,count(year) as total_movies  from movie_name  group by year order by total_movies desc ;
 -- "Number of movies released in particulat year " using windows function 
 with movie11 as 
( select (year) as years,count(year) over (partition by year order by year  rows between unbounded preceding and unbounded following) as total_movies 
from movie_name)
select distinct(years) as years ,total_movies from movie11 order by years desc;
 
 -- top revenue from directors
 select director ,sum(revenue) as total_revenue from movie_name group by director order by total_revenue desc
 limit 5; 
  -- top revenue from directors by using window function
 with movie1 as 
 (select director,sum(revenue) over (partition by director rows between unbounded preceding and unbounded following) as total_revenue from movie_name)
 select distinct (director),total_revenue from movie1 order by total_revenue desc limit 5;
 
 
 -- #movies with metascore greater than 95

 select ranks,title,votes,genre from movie_name where Metascore>95;
 

 -- movies rating greater than 8.5
 select ranks,title,votes,genre,rating from movie_name where rating >8.5; 
 
 -- movie wih highest rating
select * from movie_name where rating = (select max(rating) from movie_name); 

-- movie with lowest rating
select * from movie_name where rating =(Select min(rating) from movie_name);