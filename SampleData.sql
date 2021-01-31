


INSERT INTO `Restaurant` (`start`, `end`, `address`, `rating`, `name`) VALUES
('10:45:00', '21:00:00', NULL, 6, 'Chipotle'),
('10:30:00', '22:30:00', '1400 Lake Ave, Pasadena, CA', 10, 'Pop Eyes'),
('15:00:00', '23:00:00', 'Austin', 5, 'Pour House');


INSERT INTO `RestaurantPoints` (`Restaurant.id`,`position_x`,`position_y`) VALUES
(1, 0, 0),
(1, 0, 10),
(1, 10, 10),
(1, 10, 0),
(2, 0, 0),
(2, 0, 10),
(2, 10, 10),
(2, 10, 0),
(3, 0, 0),
(3, 0, 10),
(3, 10, 10),
(3, 10, 0);


INSERT INTO `Table` (`color`, `position_x`, `position_y`, `radius`) VALUES
('blue', 0, 0, 4.0),
('sparklez', 6, 7, 2.0),
('turtle', 13, 11, 3.14),
('cyan', 360, 12, 2.718);
