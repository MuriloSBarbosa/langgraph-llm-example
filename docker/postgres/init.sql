CREATE SCHEMA IF NOT EXISTS langgraph;

create table langgraph.book (
  id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  title varchar(255),
  genre varchar(255),
  director varchar(255),
  release_date timestamp,
  rating decimal(2,1),
  description varchar(255)
);


INSERT INTO langgraph.book (
  title,
  genre,
  director,
  release_date,
  rating,
  description
) VALUES
('1984', 'Dystopian', 'George Orwell', '1949-06-08', 4.8, 'A dystopian novel about totalitarian surveillance.'),
('Brave New World', 'Dystopian', 'Aldous Huxley', '1932-01-01', 4.6, 'A futuristic society driven by technology and control.'),
('Fahrenheit 451', 'Dystopian', 'Ray Bradbury', '1953-10-19', 4.5, 'A world where books are banned and burned.'),
('To Kill a Mockingbird', 'Classic', 'Harper Lee', '1960-07-11', 4.9, 'A novel about racial injustice in the Deep South.'),
('Pride and Prejudice', 'Romance', 'Jane Austen', '1813-01-28', 4.7, 'A romantic novel about manners and marriage.'),
('The Catcher in the Rye', 'Classic', 'J.D. Salinger', '1951-07-16', 4.2, 'A teenager’s struggle with identity and alienation.'),
('Moby-Dick', 'Adventure', 'Herman Melville', '1851-10-18', 4.1, 'An obsessive quest to hunt a giant white whale.'),
('The Great Gatsby', 'Classic', 'F. Scott Fitzgerald', '1925-04-10', 4.4, 'A critique of the American Dream in the Jazz Age.'),
('The Hobbit', 'Fantasy', 'J.R.R. Tolkien', '1937-09-21', 4.8, 'A fantasy adventure preceding The Lord of the Rings.'),
('Crime and Punishment', 'Philosophical', 'Fyodor Dostoevsky', '1866-01-01', 4.6, 'A psychological exploration of guilt and morality.'),
('The Lord of the Rings', 'Fantasy', 'J.R.R. Tolkien', '1954-07-29', 4.9, 'An epic fantasy battle between good and evil.'),
('Animal Farm', 'Political Satire', 'George Orwell', '1945-08-17', 4.7, 'A satirical allegory of political revolutions.'),
('War and Peace', 'Historical', 'Leo Tolstoy', '1869-01-01', 4.5, 'A historical novel set during the Napoleonic wars.'),
('The Alchemist', 'Philosophical', 'Paulo Coelho', '1988-01-01', 4.3, 'A journey of self-discovery and personal legend.');