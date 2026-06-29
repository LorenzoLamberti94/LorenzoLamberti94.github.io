---
title: 'TinyDEVO: Deep Event-Based Visual Odometry on Ultra-Low-Power Multi-Core Microcontrollers'
authors:
- Alessandro Marchei
- Lorenzo Lamberti
- Daniele Palossi
- Luca Benini
author_notes:
  - 'Equal contribution'
  - 'Equal contribution'
publication: '*Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
  Recognition (CVPR) Workshops*'
date: '2026-06-01'
publishDate: '2026-06-29T14:12:03.791687Z'
publication_types:
- paper-conference
# Awards, honors, and recognitions. Surfaced as badges on the page and in listings.
awards:
  - name: "Best Paper Award"
    level: winner
funding:
  - funder: "SNSF Robomix2 project"
    grant: "10004854"
abstract: A key task in embedded vision is visual odometry (VO), which estimates camera motion from visual sensors, and it is a core component in many embedded power-constrained systems, from autonomous robots to augmented and virtual reality wearable devices. The newest class of VO systems combines deep learning models with bio-inspired event-based cameras, which are robust to motion blur and lighting conditions. However, state-of-the-art (SoA) event-based VO algorithms require significant memory and computation. For example, the leading approach DEVO requires 733 MB of memory and 155 billion multiply-accumulate (MAC) operations per frame. We present TinyDEVO, an event-based VO deep learning model designed for resource-constrained microcontroller units (MCUs). We deploy TinyDEVO on an ultra-low-power (ULP) 9-core RISC-V-based MCU, achieving a throughput of approximately 1.2 frames per second with an average power consumption of only 86 mW. Thanks to our neural network architectural optimizations and hyperparameter tuning, TinyDEVO reduces the memory footprint by 11.5x (to 63.8 MB) and the number of operations per frame by 29.7x (to 5.2 billion MACs per frame) compared to DEVO, while maintaining an average trajectory error of 27 cm, i.e., only 19 cm higher than DEVO, on three state-of-the-art datasets. Our work demonstrates, for the first time, the feasibility of an event-based VO pipeline on ultra-low-power devices.
links:
  - type: pdf
    url: "https://arxiv.org/abs/2604.08060"
  - type: video
    url: https://youtu.be/wUx0V9psvUk
---
