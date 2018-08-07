import media
import fresh_tomatoes



avatar = media.Movie("Avatar",
                     "a marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/ar/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY","2002")

les_misrables =media.Movie("Les Misrables",
                           "The film takes place in France during the early 19th century and tells the story of Jean Valjean who, while being hunted for decades by the ruthless policeman Javert after breaking parole, agrees to care for a factory worker's daughter. The story reaches resolution against the background of the June Rebellion",
                           "https://upload.wikimedia.org/wikipedia/en/b/b0/Les-miserables-movie-poster1.jpg",
                           "https://www.youtube.com/watch?v=YmvHzCLP6ug","2002")

Breaking_Bad = media.Movie("Breaking Bad",
                           "To make sure his family is financially secure, he teams up with a former student Jesse Pinkman and turns to a life of crime to make and distribute the purest crystal meth on the streets. A once loyal father and chemistry teacher, Walter White, turns to a life of crime due to developing stage 3 terminal lung cancer.",
                           "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-VksLObHrsz8REV1baEm2t73YZaDqKEFJ77Vgm8oMdTZZcQ3s",
                           "https://www.youtube.com/watch?v=HhesaQXLuRY","2006")



Pride_Prejudice =media.Movie ("Pride & Prejudice ","Sparks fly when spirited Elizabeth Bennet meets single, rich, and proud Mr. Darcy. But Mr. Darcy reluctantly finds himself falling in love with a woman beneath his class. Can each overcome their own pride and prejudice?",
                                  "https://cdn.egy.best/serve/movies/art-0030279873-x300.jpg",
                                  "https://www.youtube.com/watch?v=06wvXUJZAxQ","2005")
Inception =media.Movie ("Inception",
                        "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
                        "https://is2-ssl.mzstatic.com/image/thumb/Video7/v4/5f/51/75/5f5175bf-5f14-39e7-9e37-30548c2d3044/source/1200x630bb.jpg",
                        "https://www.youtube.com/watch?v=d3A3-zSOBT4","2010")
hotel_transylvania = media.Movie ("hotel transylvania",
                                  "Dracula, who operates a high-end resort away from the human world, goes into overprotective mode when a boy discovers the resort and falls for the count's teenaged daughter.",
                                  "https://m.media-amazon.com/images/M/MV5BMTM3NjQyODI3M15BMl5BanBnXkFtZTcwMDM4NjM0OA@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                                  "https://www.youtube.com/watch?v=FYgzizpCTKU","2012")

movies =[avatar,les_misrables,Breaking_Bad,Pride_Prejudice,Inception ,hotel_transylvania]
fresh_tomatoes.open_movies_page(movies)
