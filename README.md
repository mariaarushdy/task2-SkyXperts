# task2-SkyXperts
# Camera Feed and Image Sharpening Project

![Project Banner](project_banner.png)

## Overview

This project captures a camera feed using OpenCV and publishes it to a ROS (Robot Operating System) topic. Additionally, it includes a subscriber that performs image sharpening on the received image and publishes the sharpened image to another ROS topic. The project is designed for robotics or computer vision applications.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
  - [Dependencies](#dependencies)
  - [Installation](#installation)
- [Usage](#usage)
  - [Set Up ROS Environment](#set-up-ros-environment)
  - [Launch Camera Feed Node](#launch-camera-feed-node)
  - [Launch Image Sharpening Node](#launch-image-sharpening-node)
  - [View the Output](#view-the-output)
- [Output](#output)
  - [Camera Feed](#camera-feed)
  - [Sharpened Image](#sharpened-image)
- [Code Structure](#code-structure)
- [Troubleshooting](#troubleshooting)
- [Conclusion](#conclusion)
- [References](#references)
- [Contact Information](#contact-information)

## Requirements

### Dependencies

- OpenCV: 4.5.3
- ROS (Melodic or later)
- rospy: 1.15.9
- cv-bridge: 1.12.8
- sensor-msgs: 1.16.11

