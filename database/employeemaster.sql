-- MySQL dump 10.13  Distrib 5.1.61, for Win32 (ia32)
--
-- Host: localhost    Database: employeemaster
-- ------------------------------------------------------
-- Server version	5.1.61-community

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tbl_admin`
--

DROP TABLE IF EXISTS `tbl_admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_admin` (
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_admin`
--

LOCK TABLES `tbl_admin` WRITE;
/*!40000 ALTER TABLE `tbl_admin` DISABLE KEYS */;
INSERT INTO `tbl_admin` VALUES ('admin','admin');
/*!40000 ALTER TABLE `tbl_admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_employee`
--

DROP TABLE IF EXISTS `tbl_employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_employee` (
  `userid` int(11) DEFAULT NULL,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `mailid` varchar(50) DEFAULT NULL,
  `dateofbirth` varchar(30) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `address` text,
  `city` varchar(20) DEFAULT NULL,
  `pincode` varchar(20) DEFAULT NULL,
  `mobilenumber` varchar(20) DEFAULT NULL,
  `keyskill` varchar(100) DEFAULT NULL,
  `qualification` varchar(20) DEFAULT NULL,
  `dateofjoin` varchar(15) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `emptype` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_employee`
--

LOCK TABLES `tbl_employee` WRITE;
/*!40000 ALTER TABLE `tbl_employee` DISABLE KEYS */;
INSERT INTO `tbl_employee` VALUES (1,'projectmanager','projectmanager','pm@gmail.com','1999-11-11','Male','Coimbatore','Gandhipuram','641012','1234567890','Java','MCA','2019-03-02','nothing','PM'),(2,'projectleader','projectleader','pl@gmail.com','1998-11-11','Male','coimbatore','Gandhipuram','641012','1122334455','Java','MCA','2019-03-02','nothing','PL'),(3,'projectdeveloper','projectdeveloper','pd@gmail.com','1997-11-11','Male','Coimbatore','Gandhipuram','641012','3344556677','Java','MCA','2019-03-02','nothing','PD'),(4,'developer2','developer2','developer2@gmail.com','1998-11-11','Male','Coimbatore','Gandhipuram','641012','6677554433','Java','MCA','2019-03-03','nothing','PD');
/*!40000 ALTER TABLE `tbl_employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_employee_allocation`
--

DROP TABLE IF EXISTS `tbl_employee_allocation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_employee_allocation` (
  `projectmanager` int(11) DEFAULT NULL,
  `projectleader` int(11) DEFAULT NULL,
  `projectname` varchar(100) DEFAULT NULL,
  `code` varchar(100) DEFAULT NULL,
  `projectdeveloper` int(11) DEFAULT NULL,
  `developername` varchar(20) DEFAULT NULL,
  `keyskill` varchar(100) DEFAULT NULL,
  `teamsize` int(11) DEFAULT NULL,
  `duration` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_employee_allocation`
--

LOCK TABLES `tbl_employee_allocation` WRITE;
/*!40000 ALTER TABLE `tbl_employee_allocation` DISABLE KEYS */;
INSERT INTO `tbl_employee_allocation` VALUES (1,2,'1-project1','Java',3,'projectdeveloper','Java',2,'3 Months'),(1,2,'1-project1','Java',4,'developer2','Java',2,'3 Months');
/*!40000 ALTER TABLE `tbl_employee_allocation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_feedback`
--

DROP TABLE IF EXISTS `tbl_feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_feedback` (
  `fid` int(11) DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  `username` varchar(20) DEFAULT NULL,
  `numeracy` int(11) DEFAULT NULL,
  `communication` int(11) DEFAULT NULL,
  `informationtechnology` int(11) DEFAULT NULL,
  `personalskill` int(11) DEFAULT NULL,
  `errorskill` int(11) DEFAULT NULL,
  `marksecured` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_feedback`
--

LOCK TABLES `tbl_feedback` WRITE;
/*!40000 ALTER TABLE `tbl_feedback` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_projectregister`
--

DROP TABLE IF EXISTS `tbl_projectregister`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_projectregister` (
  `projectid` int(11) DEFAULT NULL,
  `projectname` varchar(20) DEFAULT NULL,
  `codinglanguage` varchar(20) DEFAULT NULL,
  `databasename` varchar(20) DEFAULT NULL,
  `duration` varchar(20) DEFAULT NULL,
  `registerdate` varchar(20) DEFAULT NULL,
  `description` varchar(60000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_projectregister`
--

LOCK TABLES `tbl_projectregister` WRITE;
/*!40000 ALTER TABLE `tbl_projectregister` DISABLE KEYS */;
INSERT INTO `tbl_projectregister` VALUES (1,'project1','Java','MySQL','3 Months','2019-03-02','Maintain Client Details');
/*!40000 ALTER TABLE `tbl_projectregister` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_session`
--

DROP TABLE IF EXISTS `tbl_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_session` (
  `sessionid` varchar(20) DEFAULT NULL,
  `sessiontype` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_session`
--

LOCK TABLES `tbl_session` WRITE;
/*!40000 ALTER TABLE `tbl_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_task`
--

DROP TABLE IF EXISTS `tbl_task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_task` (
  `projectid` int(11) DEFAULT NULL,
  `projectname` varchar(20) DEFAULT NULL,
  `tokenno` int(11) DEFAULT NULL,
  `empid` int(11) DEFAULT NULL,
  `empname` varchar(20) DEFAULT NULL,
  `task` text,
  `completedtask` text,
  `result` text,
  `taskdate` varchar(15) DEFAULT NULL,
  `completiondate` varchar(15) DEFAULT NULL,
  `status` int(11) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_task`
--

LOCK TABLES `tbl_task` WRITE;
/*!40000 ALTER TABLE `tbl_task` DISABLE KEYS */;
INSERT INTO `tbl_task` VALUES (1,'project1',1,3,'projectdeveloper','Code to Display date in Python','import datetime\r\ntoday=datetime.datetime.now()\r\ngjhgfh\r\nfdgfdg\r\n','Pending','03-03-2019','03-03-2019',0),(1,'project1',2,4,'developer2','Code to Connect With MySQL','Import MySQLdb\r\ncon=MySQLdb.connect(\"127.0.0.1\",\"root\",\"root\",\"employeemaster\")\r\n','Completed','03-03-2019','03-03-2019',1);
/*!40000 ALTER TABLE `tbl_task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_teamleader_allocation`
--

DROP TABLE IF EXISTS `tbl_teamleader_allocation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_teamleader_allocation` (
  `tlallocationid` int(11) DEFAULT NULL,
  `projectmanager` int(11) DEFAULT NULL,
  `projectleader` int(11) DEFAULT NULL,
  `projectname` varchar(100) DEFAULT NULL,
  `code` varchar(20) DEFAULT NULL,
  `teamsize` int(11) DEFAULT NULL,
  `duration` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_teamleader_allocation`
--

LOCK TABLES `tbl_teamleader_allocation` WRITE;
/*!40000 ALTER TABLE `tbl_teamleader_allocation` DISABLE KEYS */;
INSERT INTO `tbl_teamleader_allocation` VALUES (1001,1,2,'1-project1','Java',2,'3 Months');
/*!40000 ALTER TABLE `tbl_teamleader_allocation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-03 13:30:27
