-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Хост: std-mysql
-- Время создания: Дек 07 2023 г., 10:14
-- Версия сервера: 5.7.26-0ubuntu0.16.04.1
-- Версия PHP: 8.1.15

CREATE DATABASE Apjcps1;
USE Apjcps1;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `std_1865_sokap`
--

-- --------------------------------------------------------

--
-- Структура таблицы `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('8878d9d57d88');

-- --------------------------------------------------------

--
-- Структура таблицы `genres`
--

CREATE TABLE `genres` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `genres`
--

INSERT INTO `genres` (`id`, `name`) VALUES
(2, 'ПОП'),
(3, 'РЕП'),
(1, 'РОК'),
(4, 'ХИП-ХОП');

-- --------------------------------------------------------

--
-- Структура таблицы `images`
--

CREATE TABLE `images` (
  `id` varchar(100) NOT NULL,
  `file_name` varchar(100) NOT NULL,
  `mime_type` varchar(100) NOT NULL,
  `md5_hash` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `images`
--

INSERT INTO `images` (`id`, `file_name`, `mime_type`, `md5_hash`) VALUES
('336c4304-a65b-4657-b7ff-00059e7b759d', '2332.png', 'image/png', '40fa290a28b968b429d38dc0f318fab5'),
('4895f791-085f-45f3-af43-9ed281222ca4', '324.png', 'image/png', 'd5fc021287a522d5228550e76ed184e9'),
('b44859c3-4579-472b-98bb-8b3c2ca37935', 'photo_2023-03-30_01-23-25.jpg', 'image/jpeg', '192ffb55103591ba9eab6e093658f839'),
('dd428ed0-4126-4b70-bf3d-9e13fcfc3b52', '200x200.png', 'image/png', '517c14698a945529547b168f312626ee');

-- --------------------------------------------------------

--
-- Структура таблицы `plastinkas`
--

CREATE TABLE `plastinkas` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` text NOT NULL,
  `year` int(11) NOT NULL,
  `publisher` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `volume` int(11) NOT NULL,
  `rating_sum` int(11) NOT NULL,
  `rating_num` int(11) NOT NULL,
  `id_image` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `plastinkas`
--

INSERT INTO `plastinkas` (`id`, `name`, `description`, `year`, `publisher`, `author`, `volume`, `rating_sum`, `rating_num`, `id_image`) VALUES
(3, 'Evanescence \"Виниловая пластинка Evanescence Synthesis\"', 'Состояние носителя: S. Состояние конверта: S. Synthesis. Виниловая пластинка . 2 lp A 1 Overture 0:57 A 2 Never Go Back 4:50 A 3 Hi-Lo 5:07 A 4 My Heart Is Broken 4:34 B 1 Lacrymosa 3:42 B 2 The End Of The Dream 4:54 B 3 Bring Me To Life 4:15 B 4 Unraveling (Interlude) 1:40 B 5 Imaginary 4:03 C 1 Secret Door 3:48 C 2 Lithium 4:05 C 3 Lost In Paradise 4:43 C 4 Your Star 4:38 D 1 My Immortal 4:25 D 2 The In-Between (Piano Solo) 2:11 D 3 Imperfection 4:22 Тип носителя: Виниловая пластинка\n\nhehe ц222', 2017, 'Sony', 'Evanescence', 11, 9, 2, '336c4304-a65b-4657-b7ff-00059e7b759d');

-- --------------------------------------------------------

--
-- Структура таблицы `plastinka_genre`
--

CREATE TABLE `plastinka_genre` (
  `plastinka_id` int(11) NOT NULL,
  `genre_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `plastinka_genre`
--

INSERT INTO `plastinka_genre` (`plastinka_id`, `genre_id`) VALUES
(3, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `plastinka_visits`
--

CREATE TABLE `plastinka_visits` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `plastinka_id` int(11) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `plastinka_visits`
--

INSERT INTO `plastinka_visits` (`id`, `user_id`, `plastinka_id`, `created_at`) VALUES
(1, 1, 3, '2023-10-22 15:08:15'),
(2, 1, 3, '2023-10-22 15:09:00'),
(3, 1, 3, '2023-10-22 15:11:00'),
(6, 2, 3, '2023-10-22 15:13:44'),
(7, 2, 3, '2023-10-22 15:14:19'),
(11, 2, 3, '2023-10-26 22:06:40'),
(12, 1, 3, '2023-11-11 15:03:31');

-- --------------------------------------------------------

--
-- Структура таблицы `reviews`
--

CREATE TABLE `reviews` (
  `id` int(11) NOT NULL,
  `rating` int(11) NOT NULL,
  `text` text NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `plastinka_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `reviews`
--

INSERT INTO `reviews` (`id`, `rating`, `text`, `created_at`, `plastinka_id`, `user_id`) VALUES
(1, 5, 'Wake me up! Wake me up inside!\r\n\r\n', '2023-10-22 15:09:00', 3, 1),
(3, 4, 'душевно :]', '2023-10-22 15:14:19', 3, 2);

-- --------------------------------------------------------

--
-- Структура таблицы `roles`
--

CREATE TABLE `roles` (
  `id` int(11) NOT NULL,
  `role_name` text NOT NULL,
  `role_description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `roles`
--

INSERT INTO `roles` (`id`, `role_name`, `role_description`) VALUES
(1, 'Администратор', 'Суперпользователь, имеет полный доступ к системе, в том числе к созданию и удалению книг.'),
(2, 'Исполнитель', 'Может редактировать данные пластинок'),
(3, 'Пользователь', 'Может оставлять рецензии.');

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `middle_name` varchar(100) DEFAULT NULL,
  `login` varchar(100) NOT NULL,
  `password_hash` varchar(200) NOT NULL,
  `role_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`id`, `last_name`, `first_name`, `middle_name`, `login`, `password_hash`, `role_id`) VALUES
(1, 'Иван1', 'Иван', 'Иван', 'user1', 'pbkdf2:sha256:260000$27BcLLQ2MQaRZol0$4e025114ebee24145526a7c53daad887a46bf596a6732062a0d310740132b7a2', 1),
(2, 'Иван2', 'Иван', 'Иван', 'user2', 'pbkdf2:sha256:260000$A6Glt2hNts8WDdfi$f083b9b343d517266c9fb0e783cd6fd86e1ae6d555206b4f247e365b6c5bde95', 2),
(3, 'Иван3', 'Иван', 'Иван', 'user3', 'pbkdf2:sha256:260000$mq5ognJXFGpAVv1m$a5470501e243454970771afd37af2c238699ff81a732aeaaf3a7f18fc0ba6cc3', 3),
(8, 'qwerty', 'Иван', 'qwerty', 'user4', 'pbkdf2:sha256:260000$RwjkzkbYW4VlwlKZ$ca3e906cf6b13c97cb7dd188542e277ac3319c60cebe2ea608b0e7927049c77e', 3);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Индексы таблицы `genres`
--
ALTER TABLE `genres`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Индексы таблицы `images`
--
ALTER TABLE `images`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `md5_hash` (`md5_hash`);

--
-- Индексы таблицы `plastinkas`
--
ALTER TABLE `plastinkas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_image` (`id_image`);

--
-- Индексы таблицы `plastinka_genre`
--
ALTER TABLE `plastinka_genre`
  ADD PRIMARY KEY (`plastinka_id`,`genre_id`),
  ADD KEY `genre_id` (`genre_id`);

--
-- Индексы таблицы `plastinka_visits`
--
ALTER TABLE `plastinka_visits`
  ADD PRIMARY KEY (`id`),
  ADD KEY `plastinka_id` (`plastinka_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Индексы таблицы `reviews`
--
ALTER TABLE `reviews`
  ADD PRIMARY KEY (`id`),
  ADD KEY `plastinka_id` (`plastinka_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Индексы таблицы `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `login` (`login`),
  ADD KEY `role_id` (`role_id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `genres`
--
ALTER TABLE `genres`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `plastinkas`
--
ALTER TABLE `plastinkas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `plastinka_visits`
--
ALTER TABLE `plastinka_visits`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT для таблицы `reviews`
--
ALTER TABLE `reviews`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `plastinkas`
--
ALTER TABLE `plastinkas`
  ADD CONSTRAINT `plastinkas_ibfk_1` FOREIGN KEY (`id_image`) REFERENCES `images` (`id`) ON DELETE CASCADE;

--
-- Ограничения внешнего ключа таблицы `plastinka_genre`
--
ALTER TABLE `plastinka_genre`
  ADD CONSTRAINT `plastinka_genre_ibfk_1` FOREIGN KEY (`genre_id`) REFERENCES `genres` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `plastinka_genre_ibfk_2` FOREIGN KEY (`plastinka_id`) REFERENCES `plastinkas` (`id`) ON DELETE CASCADE;

--
-- Ограничения внешнего ключа таблицы `plastinka_visits`
--
ALTER TABLE `plastinka_visits`
  ADD CONSTRAINT `plastinka_visits_ibfk_1` FOREIGN KEY (`plastinka_id`) REFERENCES `plastinkas` (`id`),
  ADD CONSTRAINT `plastinka_visits_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Ограничения внешнего ключа таблицы `reviews`
--
ALTER TABLE `reviews`
  ADD CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`plastinka_id`) REFERENCES `plastinkas` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `reviews_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Ограничения внешнего ключа таблицы `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
