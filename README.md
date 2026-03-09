# PyTorch Distributed Demo on Kubernetes

This project demonstrates running a **PyTorch distributed training demo** with multiple workers on **Kubernetes** using CPU (or GPU if available). The demo uses `torch.distributed` with the Gloo backend for collective communication.

---

## Features

- Distributed PyTorch demo with **master + multiple workers**
- Runs on **Kubernetes** (local or cloud)
- Works on **CPU**, MPS (Mac), or CUDA GPU if available
- Includes Dockerfile for building a container image
- Supports scaling number of workers dynamically
- Easy to push Docker image to Docker Hub

---

## Project Structure
