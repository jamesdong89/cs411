-- phpMyAdmin SQL Dump
-- version 4.0.10.18
-- https://www.phpmyadmin.net
--
-- Host: localhost:3306
-- Generation Time: Feb 11, 2017 at 09:09 AM
-- Server version: 10.0.29-MariaDB
-- PHP Version: 5.6.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `projectdemo411_cs411`
--

-- --------------------------------------------------------

--
-- Table structure for table `Gene`
--

CREATE TABLE IF NOT EXISTS `Gene` (
  `Gene_No` int(11) DEFAULT NULL,
  `Gene_ID` char(6) NOT NULL,
  `Gene_Symbol` char(10) DEFAULT NULL,
  `Gene_Full_Name` varchar(50) DEFAULT NULL,
  `Gene_Function` varchar(50) DEFAULT NULL,
  `Gene_Length` int(11) DEFAULT NULL,
  PRIMARY KEY (`Gene_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Gene`
--

INSERT INTO `Gene` (`Gene_No`, `Gene_ID`, `Gene_Symbol`, `Gene_Full_Name`, `Gene_Function`, `Gene_Length`) VALUES
(1, '826470', 'CRY1', 'CRYPTOCHROME 1', 'photoperiod', 3151),
(2, '827269', 'ESD4', 'EARLY IN SHORT DAYS 4', 'vernalization', 3472),
(3, '838883', 'GI', 'GIGANTEA', 'photoperiod', 5873),
(4, '837483', 'PHYA', 'PHYTOCHROME A', 'photoperiod', 5102),
(5, '816394', 'PHYB', 'PHYTOCHROME B', 'photoperiod', 4550);

-- --------------------------------------------------------

--
-- Table structure for table `User`
--

CREATE TABLE IF NOT EXISTS `User` (
  `uName` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `User`
--

INSERT INTO `User` (`uName`, `password`, `email`) VALUES
('cs411', 'cs411', 'khuramsb@gmail.com');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
